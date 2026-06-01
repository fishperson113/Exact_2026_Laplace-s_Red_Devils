"""Summarize and optionally delete Markdown files matching a regex.

Default target:
    data/pretrain_corpus/**/*.md

Example dry run:
    python scripts/remove_markdown_by_regex.py

Actually delete files after reviewing the summary:
    python scripts/remove_markdown_by_regex.py --delete --yes
"""

from __future__ import annotations

import argparse
import re
from collections import defaultdict
from dataclasses import dataclass
from pathlib import Path


DEFAULT_ROOT = Path("data/pretrain_corpus")
DEFAULT_PATTERN = r"Figure \d+"


@dataclass(frozen=True)
class MatchRecord:
    path: Path
    corpus: str
    chapter: str


@dataclass
class Impact:
    total: int = 0
    matched: int = 0


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description=(
            "Find Markdown files under a corpus root whose contents match a "
            "regex, summarize the impact, and optionally delete them."
        )
    )
    parser.add_argument(
        "--root",
        type=Path,
        default=DEFAULT_ROOT,
        help=f"Corpus root to scan. Default: {DEFAULT_ROOT}",
    )
    parser.add_argument(
        "--pattern",
        default=DEFAULT_PATTERN,
        help=f"Regex pattern to search for. Default: {DEFAULT_PATTERN!r}",
    )
    parser.add_argument(
        "--ignore-case",
        action="store_true",
        help="Search case-insensitively.",
    )
    parser.add_argument(
        "--delete",
        action="store_true",
        help="Delete matching Markdown files after printing the impact summary.",
    )
    parser.add_argument(
        "--yes",
        action="store_true",
        help="Required with --delete to confirm deletion.",
    )
    parser.add_argument(
        "--hide-files",
        action="store_true",
        help="Do not print the per-file match list.",
    )
    return parser.parse_args()


def classify_markdown_file(path: Path, root: Path) -> tuple[str, str]:
    """Return (corpus, chapter) for paths under data/pretrain_corpus.

    Expected layout is:
        <root>/<corpus>/<split>/<chapter>/<file>.md

    Files outside that shape are still included with a stable fallback group.
    """
    relative_parts = path.relative_to(root).parts
    corpus = relative_parts[0] if len(relative_parts) >= 2 else "(root)"
    chapter = relative_parts[2] if len(relative_parts) >= 4 else "(no chapter)"
    return corpus, chapter


def iter_markdown_files(root: Path) -> list[Path]:
    return sorted(path for path in root.rglob("*.md") if path.is_file())


def find_matches(
    markdown_files: list[Path],
    root: Path,
    pattern: re.Pattern[str],
) -> tuple[list[MatchRecord], dict[str, Impact], dict[tuple[str, str], Impact]]:
    corpus_impact: dict[str, Impact] = defaultdict(Impact)
    chapter_impact: dict[tuple[str, str], Impact] = defaultdict(Impact)
    matches: list[MatchRecord] = []

    for path in markdown_files:
        corpus, chapter = classify_markdown_file(path, root)
        corpus_impact[corpus].total += 1
        chapter_impact[(corpus, chapter)].total += 1

        text = path.read_text(encoding="utf-8", errors="replace")
        if pattern.search(text):
            corpus_impact[corpus].matched += 1
            chapter_impact[(corpus, chapter)].matched += 1
            matches.append(MatchRecord(path=path, corpus=corpus, chapter=chapter))

    return matches, corpus_impact, chapter_impact


def percent(matched: int, total: int) -> str:
    if total == 0:
        return "0.0%"
    return f"{matched / total * 100:.1f}%"


def print_table(headers: tuple[str, ...], rows: list[tuple[object, ...]]) -> None:
    widths = [
        max(len(str(value)) for value in (header, *(row[index] for row in rows)))
        for index, header in enumerate(headers)
    ]
    header_line = "  ".join(
        str(header).ljust(widths[index]) for index, header in enumerate(headers)
    )
    separator = "  ".join("-" * width for width in widths)
    print(header_line)
    print(separator)
    for row in rows:
        print(
            "  ".join(
                str(value).ljust(widths[index]) for index, value in enumerate(row)
            )
        )


def print_summary(
    root: Path,
    pattern: str,
    matches: list[MatchRecord],
    corpus_impact: dict[str, Impact],
    chapter_impact: dict[tuple[str, str], Impact],
    hide_files: bool,
) -> None:
    print(f"Root: {root}")
    print(f"Pattern: {pattern}")
    print(f"Matching Markdown files: {len(matches)}")
    print()

    print("Impact by corpus")
    corpus_rows = [
        (corpus, impact.matched, impact.total, percent(impact.matched, impact.total))
        for corpus, impact in sorted(corpus_impact.items())
    ]
    print_table(("corpus", "matched", "total_md", "impact"), corpus_rows)
    print()

    print("Impact by chapter")
    chapter_rows = [
        (
            corpus,
            chapter,
            impact.matched,
            impact.total,
            percent(impact.matched, impact.total),
        )
        for (corpus, chapter), impact in sorted(chapter_impact.items())
        if impact.matched
    ]
    if chapter_rows:
        print_table(("corpus", "chapter", "matched", "total_md", "impact"), chapter_rows)
    else:
        print("No chapter-level matches.")
    print()

    if not hide_files:
        print("Matched files")
        if matches:
            for match in matches:
                print(match.path)
        else:
            print("No files matched.")
        print()


def delete_matches(matches: list[MatchRecord]) -> None:
    for match in matches:
        match.path.unlink()
    print(f"Deleted {len(matches)} Markdown files.")


def main() -> int:
    args = parse_args()
    root = args.root.resolve()
    if not root.exists():
        raise SystemExit(f"Root does not exist: {root}")
    if not root.is_dir():
        raise SystemExit(f"Root is not a directory: {root}")

    flags = re.MULTILINE
    if args.ignore_case:
        flags |= re.IGNORECASE
    pattern = re.compile(args.pattern, flags)

    markdown_files = iter_markdown_files(root)
    matches, corpus_impact, chapter_impact = find_matches(markdown_files, root, pattern)

    print_summary(
        root=root,
        pattern=args.pattern,
        matches=matches,
        corpus_impact=corpus_impact,
        chapter_impact=chapter_impact,
        hide_files=args.hide_files,
    )

    if args.delete:
        if not args.yes:
            raise SystemExit("Refusing to delete without --yes.")
        delete_matches(matches)
    else:
        print("Dry run only. Re-run with --delete --yes to remove matched files.")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())