"""Prepare Young & Freedman University Physics chapter 21-31 worked examples.

Stages:
  extract   -> app/data/university_of_physic/raw/<chapter_slug>/*.pdf
  convert   -> app/data/university_of_physic/processed/<chapter_slug>/*.md
  parse     -> app/data/university_of_physic/processed/<chapter_slug>/worked_examples.jsonl
  transform -> app/data/university_of_physic/golden/<chapter_slug>/*.md

Golden files are named from the worked-example number and detected subtitle:
  21_004_forces_between_three_point_charges.md
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
OUTPUT_ROOT = REPO_ROOT / "app" / "data" / "university_of_physic"
SOURCE_PDF = OUTPUT_ROOT / "Young-Freedman-University-Physics-13th-txtbk_compressed.pdf"
RAW_ROOT = OUTPUT_ROOT / "raw"
PROCESSED_ROOT = OUTPUT_ROOT / "processed"
GOLDEN_ROOT = OUTPUT_ROOT / "golden"
CHAPTER_START = 21
CHAPTER_END = 31
BOOK_TITLE = "Young and Freedman University Physics, 13th ed."

REQUIRED_GOLDEN_HEADINGS = [
    "## Problem",
    "## Setup",
    "## Solution",
    "## Evaluation",
    "## Key concepts used",
]


@dataclass(frozen=True)
class Chapter:
    number: int
    title: str
    toc_page: int
    next_toc_page: int
    summary_page: int

    @property
    def slug(self) -> str:
        return f"ch{self.number:02d}_{slugify(self.title)}"


@dataclass(frozen=True)
class Section:
    chapter: Chapter
    number: str
    title: str
    toc_page: int
    next_toc_page: int

    @property
    def slug(self) -> str:
        return f"{self.number.replace('.', '_')}_{slugify(self.title)}"

    @property
    def pdf_filename(self) -> str:
        return f"{self.slug}.pdf"

    @property
    def md_filename(self) -> str:
        return f"{self.slug}.md"


def slugify(value: str) -> str:
    value = value.lower().replace("&", " and ")
    value = re.sub(r"[^a-z0-9]+", "_", value)
    value = re.sub(r"_+", "_", value).strip("_")
    return value[:90].rstrip("_") or "worked_example"


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


def load_toc(pdf_path: Path = SOURCE_PDF) -> tuple[list[Chapter], list[Section]]:
    with fitz.open(pdf_path) as doc:
        toc = doc.get_toc(simple=True)

    chapter_entries: list[tuple[int, str, int]] = []
    for level, title, page in toc:
        match = re.match(r"^(\d+)\s+(.+)$", title.strip())
        if level == 2 and match:
            chapter_entries.append((int(match.group(1)), match.group(2).strip().title(), page))

    chapters: dict[int, Chapter] = {}
    for index, (number, title, page) in enumerate(chapter_entries):
        if not (CHAPTER_START <= number <= CHAPTER_END):
            continue
        next_page = chapter_entries[index + 1][2]
        summary_page = next_page - 1
        for level, item_title, item_page in toc:
            if level == 3 and page <= item_page < next_page and item_title.strip() == "Summary":
                summary_page = item_page
                break
        chapters[number] = Chapter(number, title, page, next_page, summary_page)

    sections: list[Section] = []
    pending: list[tuple[Chapter, str, str, int]] = []
    for level, title, page in toc:
        if level != 3:
            continue
        match = re.match(r"^(\d+\.\d+)\s+(.+)$", title.strip())
        if not match:
            continue
        chapter_number = int(match.group(1).split(".", 1)[0])
        chapter = chapters.get(chapter_number)
        if not chapter:
            continue
        if page >= chapter.summary_page:
            continue
        pending.append((chapter, match.group(1), match.group(2).strip(), page))

    for index, (chapter, number, title, page) in enumerate(pending):
        next_page = chapter.summary_page
        if index + 1 < len(pending) and pending[index + 1][0].number == chapter.number:
            next_page = pending[index + 1][3]
        sections.append(Section(chapter, number, title, page, next_page))

    missing = [number for number in range(CHAPTER_START, CHAPTER_END + 1) if number not in chapters]
    if missing:
        raise RuntimeError(f"Missing chapter TOC entries: {missing}")
    return [chapters[number] for number in sorted(chapters)], sections


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
    chapters, sections = load_toc()
    with fitz.open(SOURCE_PDF) as doc:
        for chapter in chapters:
            chapter_dir = RAW_ROOT / chapter.slug
            save_pdf_pages(doc, chapter.toc_page, chapter.next_toc_page - 1, chapter_dir / f"ch{chapter.number:02d}.pdf")
        for section in sections:
            section_dir = RAW_ROOT / section.chapter.slug
            save_pdf_pages(doc, section.toc_page, section.next_toc_page - 1, section_dir / section.pdf_filename)
    print(f"Extracted {len(chapters)} chapter PDFs and {len(sections)} section PDFs into {RAW_ROOT}")


def convert_one_pdf(pdf_path: Path, md_path: Path, api_key: str, model: str) -> None:
    from markitdown import MarkItDown

    client = make_openai_client(api_key)
    converter = MarkItDown(llm_client=client, llm_model=model)
    result = converter.convert(str(pdf_path))
    text = getattr(result, "text_content", None) or getattr(result, "markdown", None) or str(result)
    ensure_parent(md_path)
    md_path.write_text(text.rstrip() + "\n", encoding="utf-8")


def iter_raw_section_pdfs() -> Iterable[Path]:
    if not RAW_ROOT.exists():
        return []
    return sorted(path for path in RAW_ROOT.glob("ch*/*.pdf") if not re.fullmatch(r"ch\d+\.pdf", path.name))


def convert(overwrite: bool = False) -> None:
    load_env()
    api_key, model = get_openai_settings()
    pdfs = list(iter_raw_section_pdfs())
    if not pdfs:
        raise RuntimeError(f"No section PDFs found under {RAW_ROOT}. Run extract first.")
    converted = 0
    skipped = 0
    for pdf_path in pdfs:
        md_path = PROCESSED_ROOT / pdf_path.parent.name / f"{pdf_path.stem}.md"
        if md_path.exists() and not overwrite:
            skipped += 1
            continue
        convert_one_pdf(pdf_path, md_path, api_key, model)
        converted += 1
    print(f"Converted {converted} section PDFs into {PROCESSED_ROOT}; skipped {skipped} existing files.")


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
    return text.replace("\r\n", "\n")


def compact(text: str) -> str:
    return re.sub(r"\s+", " ", text).strip()


def subtitle_from_block(example_id: str, block: str) -> str:
    cleaned = normalize_text(block)
    head = cleaned[:1200]
    after = re.split(re.escape(example_id), head, maxsplit=1, flags=re.IGNORECASE)
    candidate_region = after[1] if len(after) > 1 else head
    before_solution = re.split(r"\bSOLUTION\b", candidate_region, maxsplit=1, flags=re.IGNORECASE)[0]
    lines = [compact(line) for line in before_solution.splitlines()]
    lines = [line for line in lines if line and not re.fullmatch(r"[\d\s|.#:;-]+", line)]

    bad_prefixes = (
        "identify",
        "set up",
        "execute",
        "evaluate",
        "solution",
        "figure",
        "chapter",
        "example",
    )
    for line in lines[:8]:
        stripped = re.sub(rf"^{re.escape(example_id)}[:.\s-]*", "", line, flags=re.IGNORECASE).strip()
        if not stripped or len(stripped) < 6 or len(stripped) > 90:
            continue
        if stripped.lower().startswith(bad_prefixes):
            continue
        if stripped.count(".") > 2:
            continue
        return stripped
    return "Worked Example"


def example_filename(example_number: str, subtitle: str) -> str:
    chapter, local = example_number.split(".", 1)
    return f"{int(chapter):02d}_{int(local):03d}_{slugify(subtitle)}.md"


def needs_review(block: str, subtitle: str) -> bool:
    lower = block.lower()
    if subtitle == "Worked Example":
        return True
    if any(marker in lower for marker in ["fig.", "figure", "shown", "diagram", "graph", "table"]):
        return True
    if any(marker in block for marker in ["cid:", "\ufffd"]):
        return True
    return False


EXAMPLE_RE = re.compile(r"\bExample\s+(\d{2})\.(\d{1,2})\b", flags=re.IGNORECASE)


def parse_examples_from_markdown(text: str, chapter_number: int, section_number: str, section_title: str) -> list[dict[str, object]]:
    text = normalize_text(text)
    matches = list(EXAMPLE_RE.finditer(text))
    actual_starts: list[re.Match[str]] = []
    seen_actual: set[str] = set()
    for match in matches:
        example_chapter = int(match.group(1))
        if example_chapter != chapter_number:
            continue
        example_number = f"{example_chapter}.{int(match.group(2))}"
        if example_number in seen_actual:
            continue
        nearby = text[match.start() : min(len(text), match.start() + 5000)]
        if not re.search(r"\bSOLUTION\b", nearby, flags=re.IGNORECASE):
            continue
        actual_starts.append(match)
        seen_actual.add(example_number)

    records: list[dict[str, object]] = []
    seen: set[str] = set()
    for index, match in enumerate(actual_starts):
        example_chapter = int(match.group(1))
        start = match.start()
        end = actual_starts[index + 1].start() if index + 1 < len(actual_starts) else len(text)
        block = text[start:end].strip()
        example_number = f"{example_chapter}.{int(match.group(2))}"
        if example_number in seen:
            continue
        seen.add(example_number)
        subtitle = subtitle_from_block(f"Example {example_number}", block)
        filename = example_filename(example_number, subtitle)
        records.append(
            {
                "source": BOOK_TITLE,
                "chapter": chapter_number,
                "section": section_number,
                "section_title": section_title,
                "example_number": example_number,
                "subtitle": subtitle,
                "filename": filename,
                "source_markdown": block,
                "needs_review": needs_review(block, subtitle),
            }
        )
    return records


def section_lookup() -> dict[str, Section]:
    _, sections = load_toc()
    return {section.slug: section for section in sections}


def section_source_text(section: Section) -> str:
    with fitz.open(SOURCE_PDF) as doc:
        chunks = [
            doc[page - 1].get_text("text")
            for page in range(section.toc_page, section.next_toc_page)
        ]
    return "\n".join(chunks)


def chapter_source_text(chapter: Chapter) -> str:
    with fitz.open(SOURCE_PDF) as doc:
        chunks = [
            doc[page - 1].get_text("text")
            for page in range(chapter.toc_page, chapter.summary_page)
        ]
    return "\n".join(chunks)


def section_for_example(chapter: Chapter, sections: list[Section], example_number: str) -> Section | None:
    label = rf"Example\s+{re.escape(example_number)}\b"
    with fitz.open(SOURCE_PDF) as doc:
        for page in range(chapter.toc_page, chapter.summary_page):
            text = doc[page - 1].get_text("text")
            match = re.search(label, text)
            if not match:
                continue
            nearby = text[match.start() :] + (doc[page].get_text("text") if page < doc.page_count else "")
            if not re.search(r"\bSOLUTION\b", nearby[:5000], flags=re.IGNORECASE):
                continue
            for section in sections:
                if section.chapter.number == chapter.number and section.toc_page <= page < section.next_toc_page:
                    return section
            return None
    return None


def parse(overwrite: bool = False) -> None:
    chapters, sections = load_toc()
    by_chapter: dict[str, list[dict[str, object]]] = {}
    processed_files = sorted(PROCESSED_ROOT.glob("ch*/*.md")) if PROCESSED_ROOT.exists() else []
    if not processed_files:
        raise RuntimeError(f"No processed markdown files found under {PROCESSED_ROOT}. Run convert first.")

    for chapter in chapters:
        text = chapter_source_text(chapter)
        records = parse_examples_from_markdown(text, chapter.number, f"{chapter.number}", chapter.title)
        if not records:
            continue
        for record in records:
            section = section_for_example(chapter, sections, str(record["example_number"]))
            if section:
                record["section"] = section.number
                record["section_title"] = section.title
        by_chapter.setdefault(chapter.slug, []).extend(records)

    total = 0
    for chapter_slug, records in sorted(by_chapter.items()):
        deduped: dict[str, dict[str, object]] = {}
        for record in records:
            deduped.setdefault(str(record["example_number"]), record)
        records = sorted(deduped.values(), key=lambda record: [int(part) for part in str(record["example_number"]).split(".")])
        out_path = PROCESSED_ROOT / chapter_slug / "worked_examples.jsonl"
        if out_path.exists() and not overwrite:
            total += sum(1 for line in out_path.read_text(encoding="utf-8").splitlines() if line.strip())
            continue
        ensure_parent(out_path)
        examples_dir = out_path.parent / "examples"
        examples_dir.mkdir(parents=True, exist_ok=True)
        with out_path.open("w", encoding="utf-8") as handle:
            for record in records:
                handle.write(json.dumps(record, ensure_ascii=False) + "\n")
                example_path = examples_dir / str(record["filename"])
                if overwrite or not example_path.exists():
                    example_path.write_text(str(record["source_markdown"]).rstrip() + "\n", encoding="utf-8")
        total += len(records)
        print(f"Parsed {chapter_slug}: {len(records)} worked examples")
    print(f"Parsed {total} worked examples into {PROCESSED_ROOT}")


def iter_example_records() -> Iterable[tuple[Path, dict[str, object]]]:
    records: list[tuple[Path, dict[str, object]]] = []
    if not PROCESSED_ROOT.exists():
        return records
    for path in sorted(PROCESSED_ROOT.glob("ch*/worked_examples.jsonl")):
        for line in path.read_text(encoding="utf-8").splitlines():
            if line.strip():
                records.append((path, json.loads(line)))
    return records


def build_transform_prompt(record: dict[str, object]) -> str:
    return f"""Clean this Young and Freedman worked example into standalone Markdown.

Use this exact structure:

---
source: {BOOK_TITLE}
chapter: {record["chapter"]}
section: {record["section"]}
example_number: {record["example_number"]}
subtitle: {record["subtitle"]}
needs_review: <true or false>
---

# Example {record["example_number"]}: {record["subtitle"]}

## Problem
...

## Setup
...

## Solution
...

## Evaluation
...

## Key concepts used
...

Rules:
- Preserve the textbook's worked-solution logic and terminology.
- Keep IDENTIFY and SET UP content under Setup, EXECUTE content under Solution, and EVALUATE content under Evaluation when present.
- Do not invent missing values, figures, or diagram details.
- Keep units, signs, vector directions, and formulas explicit.
- If OCR drops essential symbols or figure details are needed, set needs_review: true.
- Output Markdown only.

Source markdown:
```markdown
{record["source_markdown"]}
```
"""


def call_openai(api_key: str, model: str, prompt: str) -> str:
    client = make_openai_client(api_key)
    if hasattr(client, "responses"):
        response = client.responses.create(model=model, input=prompt, max_output_tokens=5000)
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
            {"role": "system", "content": "You clean worked physics examples into source-faithful Markdown."},
            {"role": "user", "content": prompt},
        ],
    )
    return response.choices[0].message.content or ""


def transform(overwrite: bool = False) -> None:
    load_env()
    api_key, model = get_openai_settings()
    records = list(iter_example_records())
    if not records:
        raise RuntimeError(f"No worked example records found under {PROCESSED_ROOT}. Run parse first.")
    transformed = 0
    skipped = 0
    for jsonl_path, record in records:
        golden_path = GOLDEN_ROOT / jsonl_path.parent.name / str(record["filename"])
        if golden_path.exists() and not overwrite:
            skipped += 1
            continue
        markdown = call_openai(api_key, model, build_transform_prompt(record)).strip()
        ensure_parent(golden_path)
        golden_path.write_text(markdown + "\n", encoding="utf-8")
        transformed += 1
    print(f"Transformed {transformed} golden examples into {GOLDEN_ROOT}; skipped {skipped} existing files.")


def validate(strict: bool = False) -> None:
    chapters, sections = load_toc()
    errors: list[str] = []
    total_records = 0
    review_count = 0

    for chapter in chapters:
        raw_dir = RAW_ROOT / chapter.slug
        processed_dir = PROCESSED_ROOT / chapter.slug
        if not (raw_dir / f"ch{chapter.number:02d}.pdf").is_file():
            errors.append(f"Missing raw chapter PDF: {raw_dir / f'ch{chapter.number:02d}.pdf'}")
        if not (processed_dir / "worked_examples.jsonl").is_file():
            errors.append(f"Missing worked_examples.jsonl: {processed_dir / 'worked_examples.jsonl'}")

    for section in sections:
        raw_path = RAW_ROOT / section.chapter.slug / section.pdf_filename
        processed_path = PROCESSED_ROOT / section.chapter.slug / section.md_filename
        if not raw_path.is_file():
            errors.append(f"Missing raw section PDF: {raw_path}")
        if not processed_path.is_file():
            errors.append(f"Missing processed section markdown: {processed_path}")

    seen: set[str] = set()
    for jsonl_path, record in iter_example_records():
        total_records += 1
        key = str(record.get("example_number"))
        if key in seen:
            errors.append(f"Duplicate example number: {key}")
        seen.add(key)
        for field in ["chapter", "section", "example_number", "subtitle", "filename", "source_markdown"]:
            if not record.get(field):
                errors.append(f"Missing {field} in {jsonl_path}")
        filename = str(record.get("filename", ""))
        if not re.match(r"^\d{2}_\d{3}_[a-z0-9_]+\.md$", filename):
            errors.append(f"Bad filename convention in {jsonl_path}: {filename}")
        if record.get("needs_review"):
            review_count += 1
        if strict:
            golden_path = GOLDEN_ROOT / jsonl_path.parent.name / filename
            if not golden_path.is_file():
                errors.append(f"Missing golden example: {golden_path}")
            else:
                text = golden_path.read_text(encoding="utf-8", errors="replace")
                for heading in REQUIRED_GOLDEN_HEADINGS:
                    if heading not in text:
                        errors.append(f"Golden file missing {heading}: {golden_path}")

    if errors:
        for error in errors:
            print(f"ERROR: {error}", file=sys.stderr)
        raise SystemExit(1)
    mode = "strict raw/processed/golden" if strict else "raw/processed"
    print(f"Validated {mode} data for {len(chapters)} chapters, {len(sections)} sections, and {total_records} examples.")
    print(f"Examples marked needs_review: {review_count}")


def list_plan() -> None:
    chapters, sections = load_toc()
    for chapter in chapters:
        print(f"{chapter.number}: {chapter.slug} pages {chapter.toc_page}-{chapter.next_toc_page - 1}; summary {chapter.summary_page}")
        for section in sections:
            if section.chapter.number == chapter.number:
                print(f"  {section.number}: {section.slug} pages {section.toc_page}-{section.next_toc_page - 1}")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("stage", choices=["list", "extract", "convert", "parse", "transform", "validate", "all"])
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
    elif args.stage == "parse":
        parse(overwrite=args.overwrite)
    elif args.stage == "transform":
        transform(overwrite=args.overwrite)
    elif args.stage == "validate":
        validate(strict=args.strict)
    elif args.stage == "all":
        extract()
        convert(overwrite=args.overwrite)
        parse(overwrite=args.overwrite)
        transform(overwrite=args.overwrite)
        validate(strict=True)


if __name__ == "__main__":
    main()
