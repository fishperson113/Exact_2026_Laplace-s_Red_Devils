"""Prepare Giancoli chapter 16-22 end-of-chapter solution data.

Stages:
  extract   -> app/data/Giancoli/raw/<chapter_slug>/*.pdf
  convert   -> app/data/Giancoli/processed/<chapter_slug>/*.md
  pair      -> app/data/Giancoli/processed/<chapter_slug>/problem_answer_pairs.jsonl
  transform -> app/data/Giancoli/golden/<chapter_slug>/*.md

The golden stage generates worked solutions from problem statements paired with
the odd-numbered answer appendix. Generated reasoning should be reviewed when
the source problem depends on figures, tables, or OCR-fragile notation.
"""

from __future__ import annotations

import argparse
import json
import os
import re
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable

import fitz


def find_repo_root(start: Path) -> Path:
    for path in (start, *start.parents):
        if (path / "pyproject.toml").exists() or (path / ".git").exists():
            return path
    raise RuntimeError(f"Could not locate repository root from {start}")


REPO_ROOT = find_repo_root(Path(__file__).resolve())
OUTPUT_ROOT = REPO_ROOT / "app" / "data" / "Giancoli"
SOURCE_PDF = OUTPUT_ROOT / "Giancoli-Physics-Principles-with-Applications-7th-c2014-txtbk-1.pdf"
RAW_ROOT = OUTPUT_ROOT / "raw"
PROCESSED_ROOT = OUTPUT_ROOT / "processed"
GOLDEN_ROOT = OUTPUT_ROOT / "golden"
CHAPTER_START = 16
CHAPTER_END = 22
BOOK_TITLE = "Giancoli Physics: Principles with Applications, 7th ed."

REQUIRED_GOLDEN_HEADINGS = [
    "## Question",
    "## Final answer from source",
    "## Worked solution",
    "## Key concepts used",
]


@dataclass(frozen=True)
class Chapter:
    number: int
    title: str
    toc_page: int
    next_toc_page: int
    problems_page: int
    general_problems_page: int
    search_page: int
    answer_start_page: int
    answer_end_page: int

    @property
    def slug(self) -> str:
        return f"ch{self.number:02d}_{slugify(self.title)}"


def slugify(value: str) -> str:
    value = value.lower().replace("&", " and ")
    value = re.sub(r"[^a-z0-9]+", "_", value)
    value = re.sub(r"_+", "_", value).strip("_")
    return value[:90].rstrip("_")


def ensure_parent(path: Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)


def load_env() -> None:
    try:
        from dotenv import load_dotenv
    except ImportError:
        env_path = REPO_ROOT / ".env"
        if env_path.exists():
            for line in env_path.read_text(encoding="utf-8").splitlines():
                if not line or line.lstrip().startswith("#") or "=" not in line:
                    continue
                key, value = line.split("=", 1)
                os.environ.setdefault(key.strip(), value.strip().strip('"').strip("'"))
        return
    load_dotenv(REPO_ROOT / ".env")


def get_openai_settings() -> tuple[str, str]:
    api_key = os.environ.get("OPENAI_API_KEY")
    model = os.environ.get("OPENAI_API_MODEL")
    if not api_key:
        raise RuntimeError("OPENAI_API_KEY is not set in .env or environment.")
    if not model:
        raise RuntimeError("OPENAI_API_MODEL is not set in .env or environment.")
    return api_key, model


def make_openai_client(api_key: str):
    from openai import OpenAI

    return OpenAI(api_key=api_key)


def chapter_title(raw_title: str) -> str:
    return re.sub(r"^\d+\s+", "", raw_title).strip().title()


def load_chapters(pdf_path: Path = SOURCE_PDF) -> list[Chapter]:
    with fitz.open(pdf_path) as doc:
        toc = doc.get_toc(simple=True)

    chapter_entries: list[tuple[int, str, int]] = []
    for level, title, page in toc:
        if level == 1:
            match = re.match(r"^(\d+)\s+(.+)$", title.strip())
            if match:
                chapter_entries.append((int(match.group(1)), match.group(2).strip(), page))

    answer_pages: dict[int, int] = {}
    for level, title, page in toc:
        if level == 2:
            match = re.fullmatch(r"ch\s+(\d+)", title.strip(), flags=re.IGNORECASE)
            if match:
                answer_pages[int(match.group(1))] = page

    chapters: list[Chapter] = []
    for index, (number, title, page) in enumerate(chapter_entries):
        if not (CHAPTER_START <= number <= CHAPTER_END):
            continue
        next_page = chapter_entries[index + 1][2]
        chapter_toc = [
            (level, item_title.strip(), item_page)
            for level, item_title, item_page in toc
            if level == 2 and page <= item_page < next_page
        ]

        def find_page(label: str) -> int:
            for _, item_title, item_page in chapter_toc:
                if item_title == label:
                    return item_page
            raise RuntimeError(f"Missing '{label}' TOC entry for chapter {number}")

        if number not in answer_pages:
            raise RuntimeError(f"Missing answer appendix TOC entry for chapter {number}")
        next_answer_page = answer_pages.get(number + 1, answer_pages[number] + 1)
        answer_end_page = max(answer_pages[number], next_answer_page)

        chapters.append(
            Chapter(
                number=number,
                title=chapter_title(title),
                toc_page=page,
                next_toc_page=next_page,
                problems_page=find_page("Problems"),
                general_problems_page=find_page("General Problems"),
                search_page=find_page("Search and Learn"),
                answer_start_page=answer_pages[number],
                answer_end_page=answer_end_page,
            )
        )

    expected = set(range(CHAPTER_START, CHAPTER_END + 1))
    found = {chapter.number for chapter in chapters}
    missing = sorted(expected - found)
    if missing:
        raise RuntimeError(f"Missing chapter TOC entries: {missing}")
    return chapters


def save_pdf_pages(source: fitz.Document, start_toc_page: int, end_toc_page: int, dest: Path) -> None:
    start_index = start_toc_page - 1
    end_index = end_toc_page - 1
    if start_index < 0 or end_index < start_index or end_index >= source.page_count:
        raise ValueError(f"Invalid page range {start_toc_page}-{end_toc_page} for {dest}")
    ensure_parent(dest)
    out = fitz.open()
    out.insert_pdf(source, from_page=start_index, to_page=end_index)
    out.save(dest)
    out.close()


def extract() -> None:
    chapters = load_chapters()
    with fitz.open(SOURCE_PDF) as doc:
        for chapter in chapters:
            out_dir = RAW_ROOT / chapter.slug
            save_pdf_pages(doc, chapter.toc_page, chapter.next_toc_page - 1, out_dir / f"ch{chapter.number:02d}.pdf")
            save_pdf_pages(doc, chapter.problems_page, chapter.general_problems_page - 1, out_dir / "problems.pdf")
            save_pdf_pages(doc, chapter.general_problems_page, chapter.search_page - 1, out_dir / "general_problems.pdf")
            save_pdf_pages(doc, chapter.answer_start_page, chapter.answer_end_page, out_dir / "answers.pdf")
    print(f"Extracted {len(chapters)} chapter folders into {RAW_ROOT}")


def convert_one_pdf(pdf_path: Path, md_path: Path, api_key: str, model: str) -> None:
    from markitdown import MarkItDown

    client = make_openai_client(api_key)
    converter = MarkItDown(llm_client=client, llm_model=model)
    result = converter.convert(str(pdf_path))
    text = getattr(result, "text_content", None) or getattr(result, "markdown", None) or str(result)
    ensure_parent(md_path)
    md_path.write_text(text.rstrip() + "\n", encoding="utf-8")


def iter_raw_pdfs() -> Iterable[Path]:
    if not RAW_ROOT.exists():
        return []
    return sorted(RAW_ROOT.glob("ch*/*.pdf"))


def convert(overwrite: bool = False) -> None:
    load_env()
    api_key, model = get_openai_settings()
    raw_pdfs = list(iter_raw_pdfs())
    if not raw_pdfs:
        raise RuntimeError(f"No PDFs found under {RAW_ROOT}. Run extract first.")

    converted = 0
    skipped = 0
    for pdf_path in raw_pdfs:
        md_path = PROCESSED_ROOT / pdf_path.parent.name / f"{pdf_path.stem}.md"
        if md_path.exists() and not overwrite:
            skipped += 1
            continue
        convert_one_pdf(pdf_path, md_path, api_key, model)
        converted += 1
    print(f"Converted {converted} PDFs into {PROCESSED_ROOT}; skipped {skipped} existing files.")


def normalize_text(text: str) -> str:
    replacements = {
        "\u2013": "-",
        "\u2014": "-",
        "\u2212": "-",
        "\ufb01": "fi",
        "\ufb02": "fl",
        "\u0000": "",
    }
    for old, new in replacements.items():
        text = text.replace(old, new)
    text = re.sub(r"[ \t]+", " ", text)
    return text


PROBLEM_START_RE = re.compile(r"^\s*\*?\s*(\d{1,3})\.(?:\s+(.*)|\s*)$")


def parse_numbered_entries(text: str, odd_only: bool = True) -> dict[int, str]:
    entries: dict[int, list[str]] = {}
    current: int | None = None
    for raw_line in normalize_text(text).splitlines():
        line = raw_line.strip()
        if not line:
            continue
        match = PROBLEM_START_RE.match(line)
        if match:
            number = int(match.group(1))
            if odd_only and number % 2 == 0:
                current = None
                continue
            current = number
            entries.setdefault(number, [])
            remainder = (match.group(2) or "").strip()
            if remainder:
                entries[number].append(remainder)
            continue
        if current is not None:
            entries[current].append(line)
    return {number: clean_entry(" ".join(lines)) for number, lines in entries.items()}


def clean_entry(text: str) -> str:
    text = re.sub(r"\s+", " ", text).strip()
    text = re.sub(r"\b(?:Problems|General Problems|CHAPTER \d+)\b", "", text).strip()
    return text


def chapter_answer_text(chapter_number: int, pdf_path: Path = SOURCE_PDF) -> str:
    chapters = {chapter.number: chapter for chapter in load_chapters(pdf_path)}
    chapter = chapters[chapter_number]
    with fitz.open(pdf_path) as doc:
        chunks = [doc[page - 1].get_text("text") for page in range(chapter.answer_start_page, chapter.answer_end_page + 1)]
    text = "\n".join(chunks)
    start = re.search(rf"Chapter\s+{chapter_number}\b", text)
    end = re.search(rf"Chapter\s+{chapter_number + 1}\b", text)
    if start:
        text = text[start.end() :]
    if end:
        end_index = end.start() - (start.end() if start else 0)
        text = text[:end_index]
    return normalize_text(text)


def write_chapter_answer_markdown(chapter: Chapter, overwrite: bool = False) -> None:
    answers_path = PROCESSED_ROOT / chapter.slug / "answers.md"
    if answers_path.exists() and not overwrite:
        return
    text = chapter_answer_text(chapter.number)
    ensure_parent(answers_path)
    answers_path.write_text(f"# Chapter {chapter.number} Answers\n\n{text.strip()}\n", encoding="utf-8")


def needs_review(question: str, answer: str) -> bool:
    combined = f"{question} {answer}".lower()
    figure_markers = ["fig.", "figure", "shown", "diagram", "graph", "table"]
    if any(marker in combined for marker in figure_markers):
        return True
    if len(answer.strip()) < 4:
        return True
    return False


def pair(overwrite: bool = False) -> None:
    chapters = load_chapters()
    total_pairs = 0
    for chapter in chapters:
        chapter_dir = PROCESSED_ROOT / chapter.slug
        problems_path = chapter_dir / "problems.md"
        general_path = chapter_dir / "general_problems.md"
        if not problems_path.exists() or not general_path.exists():
            raise RuntimeError(f"Missing processed problem markdown for chapter {chapter.number}. Run convert first.")

        write_chapter_answer_markdown(chapter, overwrite=overwrite)
        output_path = chapter_dir / "problem_answer_pairs.jsonl"
        if output_path.exists() and not overwrite:
            total_pairs += sum(1 for _ in output_path.open(encoding="utf-8"))
            continue

        problem_text = problems_path.read_text(encoding="utf-8", errors="replace")
        general_text = general_path.read_text(encoding="utf-8", errors="replace")
        questions = parse_numbered_entries(problem_text + "\n" + general_text, odd_only=True)
        answers = parse_numbered_entries(chapter_answer_text(chapter.number), odd_only=True)

        records: list[dict[str, object]] = []
        for number in sorted(set(questions) & set(answers)):
            question = questions[number]
            answer = answers[number]
            if not question or not answer:
                continue
            records.append(
                {
                    "source": BOOK_TITLE,
                    "chapter": chapter.number,
                    "chapter_title": chapter.title,
                    "problem_number": number,
                    "question": question,
                    "final_answer": answer,
                    "needs_review": needs_review(question, answer),
                }
            )

        ensure_parent(output_path)
        with output_path.open("w", encoding="utf-8") as handle:
            for record in records:
                handle.write(json.dumps(record, ensure_ascii=False) + "\n")
        total_pairs += len(records)
        print(f"Paired chapter {chapter.number}: {len(records)} problem-answer records")
    print(f"Paired {total_pairs} total problem-answer records into {PROCESSED_ROOT}")


def iter_pair_records() -> Iterable[tuple[Path, dict[str, object]]]:
    if not PROCESSED_ROOT.exists():
        return []
    records: list[tuple[Path, dict[str, object]]] = []
    for pairs_path in sorted(PROCESSED_ROOT.glob("ch*/problem_answer_pairs.jsonl")):
        for line in pairs_path.read_text(encoding="utf-8").splitlines():
            if line.strip():
                records.append((pairs_path, json.loads(line)))
    return records


def build_solution_prompt(record: dict[str, object]) -> str:
    return f"""Generate a source-constrained worked physics solution.

Use this exact output structure in Markdown:

---
source: {BOOK_TITLE}
chapter: {record["chapter"]}
problem_number: {record["problem_number"]}
answer_source: Answers to Odd-Numbered Problems
needs_review: <true or false>
---

# Problem {record["chapter"]}.{record["problem_number"]}

## Question
<copy the problem statement faithfully>

## Final answer from source
<copy the final answer faithfully>

## Worked solution
<derive a step-by-step solution that ends consistently with the source answer>

## Key concepts used
<bulleted concepts>

Rules:
- The source final answer is a hard constraint.
- Do not invent missing diagram details. If a diagram/table/figure is required, set needs_review: true and explain the limitation.
- If OCR appears incomplete or variables are missing, set needs_review: true.
- Keep units, signs, directions, and vector reasoning explicit.

Question:
{record["question"]}

Final answer from source:
{record["final_answer"]}

Initial needs_review flag from parser: {str(record["needs_review"]).lower()}
"""


def call_openai(api_key: str, model: str, prompt: str) -> str:
    client = make_openai_client(api_key)
    if hasattr(client, "responses"):
        response = client.responses.create(model=model, input=prompt, max_output_tokens=4000)
        output_text = getattr(response, "output_text", None)
        if output_text:
            return output_text
        chunks: list[str] = []
        for item in getattr(response, "output", []) or []:
            for content in getattr(item, "content", []) or []:
                text = getattr(content, "text", None)
                if text:
                    chunks.append(text)
        if chunks:
            return "\n".join(chunks)

    response = client.chat.completions.create(
        model=model,
        messages=[
            {"role": "system", "content": "You generate faithful worked physics solutions from source problem-answer pairs."},
            {"role": "user", "content": prompt},
        ],
    )
    return response.choices[0].message.content or ""


def transform(overwrite: bool = False) -> None:
    load_env()
    api_key, model = get_openai_settings()
    records = list(iter_pair_records())
    if not records:
        raise RuntimeError(f"No problem-answer pairs found under {PROCESSED_ROOT}. Run pair first.")

    transformed = 0
    skipped = 0
    for pairs_path, record in records:
        chapter_slug = pairs_path.parent.name
        chapter = int(record["chapter"])
        number = int(record["problem_number"])
        golden_path = GOLDEN_ROOT / chapter_slug / f"{chapter:02d}_{number:03d}.md"
        if golden_path.exists() and not overwrite:
            skipped += 1
            continue
        prompt = build_solution_prompt(record)
        markdown = call_openai(api_key, model, prompt).strip()
        ensure_parent(golden_path)
        golden_path.write_text(markdown + "\n", encoding="utf-8")
        transformed += 1
    print(f"Transformed {transformed} golden files into {GOLDEN_ROOT}; skipped {skipped} existing files.")


def validate(strict: bool = False) -> None:
    chapters = load_chapters()
    errors: list[str] = []
    total_pairs = 0
    needs_review_count = 0

    for chapter in chapters:
        raw_dir = RAW_ROOT / chapter.slug
        processed_dir = PROCESSED_ROOT / chapter.slug
        for filename in [f"ch{chapter.number:02d}.pdf", "problems.pdf", "general_problems.pdf", "answers.pdf"]:
            if not (raw_dir / filename).is_file():
                errors.append(f"Missing raw file: {raw_dir / filename}")
        for filename in ["problems.md", "general_problems.md", "answers.md", "problem_answer_pairs.jsonl"]:
            if not (processed_dir / filename).is_file():
                errors.append(f"Missing processed file: {processed_dir / filename}")

        pairs_path = processed_dir / "problem_answer_pairs.jsonl"
        if pairs_path.exists():
            for line_number, line in enumerate(pairs_path.read_text(encoding="utf-8").splitlines(), start=1):
                if not line.strip():
                    continue
                total_pairs += 1
                record = json.loads(line)
                for key in ["chapter", "problem_number", "question", "final_answer"]:
                    if not record.get(key):
                        errors.append(f"Missing {key} in {pairs_path}:{line_number}")
                if int(record["problem_number"]) % 2 == 0:
                    errors.append(f"Even problem number in {pairs_path}:{line_number}")
                if record.get("needs_review"):
                    needs_review_count += 1

        if strict:
            for pairs_path, record in iter_pair_records():
                if pairs_path.parent.name != chapter.slug:
                    continue
                golden_path = GOLDEN_ROOT / chapter.slug / f"{int(record['chapter']):02d}_{int(record['problem_number']):03d}.md"
                if not golden_path.is_file():
                    errors.append(f"Missing golden file: {golden_path}")
                    continue
                text = golden_path.read_text(encoding="utf-8", errors="replace")
                for heading in REQUIRED_GOLDEN_HEADINGS:
                    if heading not in text:
                        errors.append(f"Golden file missing {heading}: {golden_path}")

    if errors:
        for error in errors:
            print(f"ERROR: {error}", file=sys.stderr)
        raise SystemExit(1)
    mode = "strict raw/processed/golden" if strict else "raw/processed"
    print(f"Validated {mode} data for {len(chapters)} chapters and {total_pairs} pairs.")
    print(f"Pairs marked needs_review: {needs_review_count}")


def list_plan() -> None:
    for chapter in load_chapters():
        print(f"{chapter.number}: {chapter.slug} pages {chapter.toc_page}-{chapter.next_toc_page - 1}")
        print(f"  problems: {chapter.problems_page}-{chapter.general_problems_page - 1}")
        print(f"  general_problems: {chapter.general_problems_page}-{chapter.search_page - 1}")
        print(f"  answers: {chapter.answer_start_page}-{chapter.answer_end_page}")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("stage", choices=["list", "extract", "convert", "pair", "transform", "validate", "all"])
    parser.add_argument("--overwrite", action="store_true", help="Overwrite existing generated files.")
    parser.add_argument("--strict", action="store_true", help="For validate, require golden files.")
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    if args.stage == "list":
        list_plan()
    elif args.stage == "extract":
        extract()
    elif args.stage == "convert":
        convert(overwrite=args.overwrite)
    elif args.stage == "pair":
        pair(overwrite=args.overwrite)
    elif args.stage == "transform":
        transform(overwrite=args.overwrite)
    elif args.stage == "validate":
        validate(strict=args.strict)
    elif args.stage == "all":
        extract()
        convert(overwrite=args.overwrite)
        pair(overwrite=args.overwrite)
        transform(overwrite=args.overwrite)
        validate(strict=True)


if __name__ == "__main__":
    main()
