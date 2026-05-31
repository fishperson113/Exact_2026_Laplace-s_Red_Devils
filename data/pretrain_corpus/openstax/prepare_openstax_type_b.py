"""Prepare OpenStax College Physics 2e chapter sections as Loai B markdown.

Stages:
  extract   -> app/data/openstax/raw/<chapter_slug>/*.pdf
  convert   -> app/data/openstax/processed/<chapter_slug>/*.md
  transform -> app/data/openstax/golden/<chapter_slug>/*.md

The extraction stage uses the PDF table of contents. Only numbered level-2
sections such as "5.1 Friction" are emitted as standalone section files.
"""

from __future__ import annotations

import argparse
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
OUTPUT_ROOT = REPO_ROOT / "app" / "data" / "openstax"
SOURCE_PDF = OUTPUT_ROOT / "college-physics-2e_-_WEB.pdf"
RAW_ROOT = OUTPUT_ROOT / "raw"
PROCESSED_ROOT = OUTPUT_ROOT / "processed"
GOLDEN_ROOT = OUTPUT_ROOT / "golden"
CHAPTER_START = 5
CHAPTER_END = 12
BOOK_TITLE = "OpenStax College Physics 2e"

REQUIRED_GOLDEN_HEADINGS = [
    "## Concept explanation",
    "## Key formulas",
    "## Variables and units",
    "## Worked example",
    "## Key concepts used",
]


@dataclass(frozen=True)
class Chapter:
    number: int
    title: str
    toc_page: int
    next_toc_page: int

    @property
    def slug(self) -> str:
        return f"ch{self.number:02d}_{slugify(strip_chapter_prefix(self.title))}"

    @property
    def filename(self) -> str:
        return f"ch{self.number:02d}.pdf"


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
    value = value.lower()
    value = value.replace("&", " and ")
    value = re.sub(r"[^a-z0-9]+", "_", value)
    value = re.sub(r"_+", "_", value).strip("_")
    return value[:90].rstrip("_")


def strip_chapter_prefix(title: str) -> str:
    return re.sub(r"^Chapter\s+\d+\s+", "", title).strip()


def strip_section_prefix(title: str) -> tuple[str, str] | None:
    match = re.match(r"^(\d+\.\d+)\s+(.+)$", title.strip())
    if not match:
        return None
    return match.group(1), match.group(2).strip()


def load_toc(pdf_path: Path) -> tuple[list[Chapter], list[Section]]:
    with fitz.open(pdf_path) as doc:
        toc = doc.get_toc(simple=True)

    chapters: dict[int, Chapter] = {}
    chapter_entries: list[tuple[int, str, int]] = []
    for level, title, page in toc:
        if level != 1:
            continue
        match = re.match(r"^Chapter\s+(\d+)\s+", title)
        if match:
            chapter_entries.append((int(match.group(1)), title, page))

    for index, (number, title, page) in enumerate(chapter_entries):
        if CHAPTER_START <= number <= CHAPTER_END:
            next_page = chapter_entries[index + 1][2]
            chapters[number] = Chapter(number, title, page, next_page)

    sections: list[Section] = []
    active_chapter: Chapter | None = None
    pending: list[tuple[Chapter, str, str, int]] = []
    for level, title, page in toc:
        if level == 1:
            match = re.match(r"^Chapter\s+(\d+)\s+", title)
            active_chapter = chapters.get(int(match.group(1))) if match else None
            continue
        if level != 2 or active_chapter is None:
            continue
        parsed = strip_section_prefix(title)
        if parsed is None:
            continue
        section_number, section_title = parsed
        if int(section_number.split(".", 1)[0]) != active_chapter.number:
            continue
        pending.append((active_chapter, section_number, section_title, page))

    for index, (chapter, number, title, page) in enumerate(pending):
        next_page = chapter.next_toc_page
        if index + 1 < len(pending) and pending[index + 1][0].number == chapter.number:
            next_page = pending[index + 1][3]
        sections.append(Section(chapter, number, title, page, next_page))

    missing = [number for number in range(CHAPTER_START, CHAPTER_END + 1) if number not in chapters]
    if missing:
        raise RuntimeError(f"Missing chapter TOC entries: {missing}")
    return [chapters[number] for number in sorted(chapters)], sections


def ensure_parent(path: Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)


def save_pdf_pages(source: fitz.Document, start_toc_page: int, next_toc_page: int, dest: Path) -> None:
    start_index = start_toc_page - 1
    end_index = next_toc_page - 2
    if start_index < 0 or end_index < start_index or end_index >= source.page_count:
        raise ValueError(f"Invalid page range {start_toc_page}-{next_toc_page - 1} for {dest}")
    ensure_parent(dest)
    out = fitz.open()
    out.insert_pdf(source, from_page=start_index, to_page=end_index)
    out.save(dest)
    out.close()


def extract(pdf_path: Path = SOURCE_PDF) -> None:
    chapters, sections = load_toc(pdf_path)
    with fitz.open(pdf_path) as doc:
        for chapter in chapters:
            chapter_dir = RAW_ROOT / chapter.slug
            save_pdf_pages(doc, chapter.toc_page, chapter.next_toc_page, chapter_dir / chapter.filename)
        for section in sections:
            section_dir = RAW_ROOT / section.chapter.slug
            save_pdf_pages(doc, section.toc_page, section.next_toc_page, section_dir / section.pdf_filename)
    print(f"Extracted {len(chapters)} chapter PDFs and {len(sections)} section PDFs into {RAW_ROOT}")


def convert_one_pdf(pdf_path: Path, md_path: Path, api_key: str, model: str) -> None:
    from markitdown import MarkItDown

    client = make_openai_client(api_key)
    converter = MarkItDown(llm_client=client, llm_model=model)
    result = converter.convert(str(pdf_path))
    text = getattr(result, "text_content", None) or getattr(result, "markdown", None) or str(result)
    ensure_parent(md_path)
    md_path.write_text(text.rstrip() + "\n", encoding="utf-8")


def iter_section_pdfs() -> Iterable[Path]:
    if not RAW_ROOT.exists():
        return []
    return sorted(path for path in RAW_ROOT.glob("ch*/*.pdf") if not re.fullmatch(r"ch\d+\.pdf", path.name))


def convert(overwrite: bool = False) -> None:
    load_env()
    api_key, model = get_openai_settings()
    section_pdfs = list(iter_section_pdfs())
    if not section_pdfs:
        raise RuntimeError(f"No section PDFs found under {RAW_ROOT}. Run extract first.")
    converted = 0
    skipped = 0
    for pdf_path in section_pdfs:
        md_path = PROCESSED_ROOT / pdf_path.parent.name / f"{pdf_path.stem}.md"
        if md_path.exists() and not overwrite:
            skipped += 1
            continue
        convert_one_pdf(pdf_path, md_path, api_key, model)
        converted += 1
    print(f"Converted {converted} section PDFs into {PROCESSED_ROOT}; skipped {skipped} existing files.")


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


def build_transform_prompt(section_path: Path, source_markdown: str) -> str:
    section_label = section_path.stem.split("_", 2)
    section_number = ".".join(section_label[:2]) if len(section_label) >= 2 else section_path.stem
    title_hint = section_path.stem.replace("_", " ")
    return f"""You transform OpenStax textbook markdown into Loai B physics pretraining markdown.

Output must be Markdown only, with this exact structure:

# {section_number} <section title>

Source: {BOOK_TITLE}, Chapter {section_number.split('.')[0]}, Section {section_number}

## Concept explanation
...

## Key formulas
...

## Variables and units
...

## Worked example
...

## Key concepts used
...

Rules:
- Preserve source facts and physics notation. Do not invent textbook content.
- Keep formulas, units, assumptions, and conditions explicit.
- Include at least one worked example only when it is present in the source section.
- If no worked example is present, write exactly: Worked example unavailable in source section
- Remove PDF artifacts such as repeated headers, footers, page numbers, navigation text, and copyright boilerplate.
- The output is standalone Loai B pretraining text, not JSONL, not CSV, and not a chat transcript.

Section file hint: {title_hint}

Source markdown:
```markdown
{source_markdown}
```
"""


def call_openai(api_key: str, model: str, prompt: str) -> str:
    client = make_openai_client(api_key)
    if hasattr(client, "responses"):
        response = client.responses.create(
            model=model,
            input=prompt,
            max_output_tokens=8000,
        )
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
            {"role": "system", "content": "You create faithful physics pretraining markdown from source text."},
            {"role": "user", "content": prompt},
        ],
    )
    return response.choices[0].message.content or ""


def iter_processed_markdown() -> Iterable[Path]:
    if not PROCESSED_ROOT.exists():
        return []
    return sorted(PROCESSED_ROOT.glob("ch*/*.md"))


def transform(overwrite: bool = False) -> None:
    load_env()
    api_key, model = get_openai_settings()

    processed_files = list(iter_processed_markdown())
    if not processed_files:
        raise RuntimeError(f"No processed markdown files found under {PROCESSED_ROOT}. Run convert first.")

    transformed = 0
    skipped = 0
    for processed_path in processed_files:
        golden_path = GOLDEN_ROOT / processed_path.parent.name / processed_path.name
        if golden_path.exists() and not overwrite:
            skipped += 1
            continue
        source_markdown = processed_path.read_text(encoding="utf-8")
        prompt = build_transform_prompt(processed_path, source_markdown)
        golden_markdown = call_openai(api_key, model, prompt).strip()
        ensure_parent(golden_path)
        golden_path.write_text(golden_markdown + "\n", encoding="utf-8")
        transformed += 1
    print(f"Transformed {transformed} markdown files into {GOLDEN_ROOT}; skipped {skipped} existing files.")


def validate(strict: bool = False) -> None:
    chapters, sections = load_toc(SOURCE_PDF)
    errors: list[str] = []

    for chapter in chapters:
        chapter_dir = RAW_ROOT / chapter.slug
        if not chapter_dir.is_dir():
            errors.append(f"Missing raw chapter directory: {chapter_dir}")
        if not (chapter_dir / chapter.filename).is_file():
            errors.append(f"Missing raw chapter PDF: {chapter_dir / chapter.filename}")

    for section in sections:
        raw_path = RAW_ROOT / section.chapter.slug / section.pdf_filename
        processed_path = PROCESSED_ROOT / section.chapter.slug / section.md_filename
        golden_path = GOLDEN_ROOT / section.chapter.slug / section.md_filename
        if not raw_path.is_file():
            errors.append(f"Missing section PDF: {raw_path}")
        if not processed_path.is_file():
            errors.append(f"Missing processed markdown: {processed_path}")
        else:
            text = processed_path.read_text(encoding="utf-8", errors="replace")
            if len(text.strip()) < 200:
                errors.append(f"Processed markdown looks too small: {processed_path}")
            if section.title.lower().split(":", 1)[0] not in text.lower():
                errors.append(f"Processed markdown may not contain section title: {processed_path}")
        if strict and not golden_path.is_file():
            errors.append(f"Missing golden markdown: {golden_path}")
        elif golden_path.exists():
            text = golden_path.read_text(encoding="utf-8", errors="replace")
            for heading in REQUIRED_GOLDEN_HEADINGS:
                if heading not in text:
                    errors.append(f"Golden markdown missing '{heading}': {golden_path}")

    if errors:
        for error in errors:
            print(f"ERROR: {error}", file=sys.stderr)
        raise SystemExit(1)
    mode = "strict raw/processed/golden" if strict else "raw/processed"
    print(f"Validated {mode} structure for {len(chapters)} chapters and {len(sections)} sections.")


def list_plan() -> None:
    chapters, sections = load_toc(SOURCE_PDF)
    for chapter in chapters:
        print(f"{chapter.number}: {chapter.slug} pages {chapter.toc_page}-{chapter.next_toc_page - 1}")
        for section in sections:
            if section.chapter.number == chapter.number:
                print(f"  {section.number}: {section.slug} pages {section.toc_page}-{section.next_toc_page - 1}")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "stage",
        choices=["list", "extract", "convert", "transform", "validate", "all"],
        help="Pipeline stage to run.",
    )
    parser.add_argument(
        "--overwrite",
        action="store_true",
        help="Overwrite existing processed or golden markdown files for convert/transform/all.",
    )
    parser.add_argument(
        "--strict",
        action="store_true",
        help="For validate, require every golden markdown file in addition to raw and processed files.",
    )
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    if args.stage == "list":
        list_plan()
    elif args.stage == "extract":
        extract()
    elif args.stage == "convert":
        convert(overwrite=args.overwrite)
    elif args.stage == "transform":
        transform(overwrite=args.overwrite)
    elif args.stage == "validate":
        validate(strict=args.strict)
    elif args.stage == "all":
        extract()
        convert(overwrite=args.overwrite)
        transform(overwrite=args.overwrite)
        validate(strict=True)


if __name__ == "__main__":
    main()
