#!/usr/bin/env python3
"""Build a single offline HTML document for the research guide.

The workflow turns this HTML into a PDF with WeasyPrint. The script itself only
assembles Markdown so it stays easy to run locally:

    python scripts/build_pdf.py

The result is written to ``build/how-to-research.html``.
"""

from __future__ import annotations

import html
import pathlib
import re
from dataclasses import dataclass, field
from typing import Optional

import markdown


ROOT = pathlib.Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
BUILD = ROOT / "build"
OUT_HTML = BUILD / "how-to-research.html"
OUT_PDF = BUILD / "how-to-research.pdf"

_CJK = re.compile(r"[\u3400-\u9fff\uf900-\ufaff]")
_H1 = re.compile(r"^#\s+(.+)$", re.MULTILINE)
_IMG = re.compile(
    r"!\[([^\]]*)\]\((?:\s*<([^>]+)>\s*|\s*([^)\s]+)\s*)"
    r"(?:\s+[\"'][^\"']*[\"'])?\)"
)

_MARKDOWN = markdown.Markdown(
    extensions=["tables", "fenced_code", "sane_lists", "attr_list"]
)

PDF_EXCLUDED_SUBDIR_CHAPTERS = {"04-本科论文写作"}


@dataclass
class Doc:
    path: pathlib.Path
    title: str


@dataclass
class Group:
    label: Optional[str]
    docs: list[Doc] = field(default_factory=list)


@dataclass
class Chapter:
    label: str
    groups: list[Group] = field(default_factory=list)


def prettify_title(raw: str) -> str:
    """Turn a file/dir name into a readable Chinese title."""
    title = raw.strip()
    if not title:
        return "未命名"

    match = re.match(r"^\d{1,3}\s*[-–—.]\s*(.*)$", title)
    if match:
        candidate = match.group(1).strip()
        cjk = _CJK.search(candidate)
        if cjk:
            start = cjk.start()
            while start > 0 and candidate[start - 1].isdigit():
                start -= 1
            candidate = candidate[start:].strip()
        if candidate:
            title = candidate

    return title


def first_heading(path: pathlib.Path) -> str:
    text = path.read_text(encoding="utf-8")
    match = _H1.search(text)
    if match:
        return prettify_title(match.group(1))
    return prettify_title(path.stem)


def rewrite_images(text: str, base_dir: pathlib.Path) -> str:
    """Resolve relative image paths to file:// URLs WeasyPrint can load."""

    def replace(match: re.Match[str]) -> str:
        target = match.group(2) or match.group(3)
        if not target:
            return match.group(0)
        if re.match(r"^(?:https?://|data:|file:|/)", target, re.IGNORECASE):
            return match.group(0)

        resolved = (base_dir / target).resolve()
        if resolved.exists():
            return f"![{match.group(1)}]({resolved.as_uri()})"
        return match.group(0)

    return _IMG.sub(replace, text)


def demote_headings(fragment: str, levels: int = 1) -> str:
    """Shift <hN> down one level so chapter titles stay on top."""
    if levels <= 0:
        return fragment

    def open_tag(match: re.Match[str]) -> str:
        new_level = min(int(match.group(1)) + levels, 6)
        return f"<h{new_level}{match.group(2)}"

    def close_tag(match: re.Match[str]) -> str:
        new_level = min(int(match.group(1)) + levels, 6)
        return f"</h{new_level}>"

    fragment = re.sub(r"<h([1-6])([ >])", open_tag, fragment)
    return re.sub(r"</h([1-6])>", close_tag, fragment)


def normalize_first_heading(text: str, pretty: str) -> str:
    """Replace a filename-like H1 with the cleaned title used in the TOC."""
    match = _H1.search(text)
    if not match:
        return text

    raw = match.group(1).strip()
    if not re.match(r"^\d{1,3}\s*[-–—.]", raw):
        return text

    return text[: match.start()] + f"# {pretty}" + text[match.end() :]


def convert_doc(doc: Doc) -> str:
    text = doc.path.read_text(encoding="utf-8")
    text = normalize_first_heading(text, doc.title)
    text = rewrite_images(text, doc.path.parent)
    body = _MARKDOWN.convert(text)
    body = demote_headings(body)
    return body


def collect_chapters() -> list[Chapter]:
    chapters: list[Chapter] = []
    chapter_dirs = sorted(
        (p for p in DOCS.iterdir() if p.is_dir() and not p.name.startswith(".")),
        key=lambda p: p.name,
    )

    for chapter_dir in chapter_dirs:
        number = chapter_dir.name.split("-", 1)[0]
        chapter = Chapter(label=f"{number} · {prettify_title(chapter_dir.name)}")

        top_level_docs = sorted(
            (p for p in chapter_dir.iterdir() if p.is_file() and p.suffix == ".md"),
            key=lambda p: (0 if p.stem == "README" else 1, p.name),
        )
        if top_level_docs:
            chapter.groups.append(
                Group(label=None, docs=[Doc(p, first_heading(p)) for p in top_level_docs])
            )

        subdirs = sorted(
            (
                p
                for p in chapter_dir.iterdir()
                if p.is_dir() and not p.name.startswith(".") and any(p.glob("**/*.md"))
            ),
            key=lambda p: p.name,
        )
        if chapter_dir.name in PDF_EXCLUDED_SUBDIR_CHAPTERS:
            subdirs = []
        for subdir in subdirs:
            docs = sorted(
                subdir.rglob("*.md"),
                key=lambda p: (
                    0 if p.stem == "README" else 1,
                    p.relative_to(subdir).as_posix(),
                ),
            )
            if docs:
                chapter.groups.append(
                    Group(
                        label=prettify_title(subdir.name),
                        docs=[Doc(p, first_heading(p)) for p in docs],
                    )
                )

        chapters.append(chapter)

    return chapters


CSS = """
@page {
  size: A4;
  margin: 20mm 17mm 22mm 17mm;
  @bottom-center {
    content: counter(page);
    font-family: "Noto Sans CJK SC", sans-serif;
    font-size: 9pt;
    color: #6e7781;
  }
  @top-center {
    content: "科研入门指南";
    font-family: "Noto Sans CJK SC", sans-serif;
    font-size: 8pt;
    color: #9ca3af;
  }
}

@page :first {
  margin: 0;
  @bottom-center { content: none; }
  @top-center { content: none; }
}

html {
  font-family: "Noto Sans CJK SC", "Noto Sans SC", "Noto Color Emoji", sans-serif;
}

body {
  font-family: "Noto Sans CJK SC", "Noto Sans SC", "Noto Color Emoji", sans-serif;
  font-size: 10.5pt;
  line-height: 1.75;
  color: #1f2328;
}

h1, h2, h3, h4, h5, h6 {
  font-family: "Noto Serif CJK SC", "Noto Sans CJK SC", sans-serif;
  color: #111418;
  line-height: 1.35;
}

h1 { font-size: 20pt; margin: 0 0 10pt; }
h2 { font-size: 15pt; margin: 16pt 0 8pt; }
h3 { font-size: 12.5pt; margin: 14pt 0 6pt; }
h4 { font-size: 11pt; margin: 10pt 0 4pt; }

h1 { bookmark-level: 1; bookmark-label: content(); }
h2 { bookmark-level: 2; bookmark-label: content(); }
h3 { bookmark-level: 3; bookmark-label: content(); }
h4 { bookmark-level: 4; bookmark-label: content(); }

p { margin: 6pt 0; }
a { color: #0969da; text-decoration: none; }
img { max-width: 100%; height: auto; }

ul, ol { margin: 6pt 0; padding-left: 1.6em; }
li { margin: 2pt 0; }

blockquote {
  margin: 8pt 0;
  padding: 4pt 10pt;
  border-left: 3pt solid #d0d7de;
  background: #f6f8fa;
  color: #57606a;
}

code {
  font-family: "DejaVu Sans Mono", "Noto Sans Mono CJK SC", monospace;
  font-size: 9pt;
  background: #f6f8fa;
  padding: 0 3pt;
  border-radius: 2pt;
}

pre {
  background: #f6f8fa;
  border: 1px solid #eaeef2;
  border-radius: 4pt;
  padding: 8pt 10pt;
  overflow-wrap: break-word;
  white-space: pre-wrap;
}

pre code { background: none; padding: 0; }

table {
  width: 100%;
  border-collapse: collapse;
  font-size: 9pt;
  margin: 8pt 0;
}

th, td {
  border: 1px solid #d0d7de;
  padding: 5pt 7pt;
  text-align: left;
  vertical-align: top;
}

th { background: #f6f8fa; font-weight: 600; }

hr { border: none; border-top: 1px solid #d0d7de; margin: 12pt 0; }

.cover {
  break-after: page;
  text-align: center;
  padding-top: 62mm;
}

.cover h1 {
  font-size: 34pt;
  margin: 0 0 14pt;
  bookmark-level: none;
}

.cover .subtitle {
  font-size: 14pt;
  color: #57606a;
  margin: 0 0 26pt;
}

.cover .meta {
  font-size: 10pt;
  color: #9ca3af;
}

nav.toc h2 { font-size: 20pt; bookmark-level: none; }

nav.toc ul { list-style: none; padding-left: 0; }
nav.toc li { margin: 2pt 0; }

nav.toc a {
  display: block;
  color: inherit;
  text-decoration: none;
}

nav.toc a::after {
  content: target-counter(attr(href), page);
  float: right;
  color: #6e7781;
  font-size: 9pt;
  font-weight: normal;
}

nav.toc .toc-chapter > a {
  font-weight: 700;
  font-size: 12pt;
  margin-top: 8pt;
}

nav.toc .toc-children { padding-left: 1.4em; }

nav.toc .toc-group {
  margin-top: 8pt;
  color: #57606a;
  font-weight: 600;
  font-size: 10pt;
}

nav.toc .toc-doc { padding-left: 1.3em; }

.chapter { break-before: page; }

.chapter-title { break-after: avoid; }

.doc { break-before: page; }

.chapter-title + .doc { break-before: auto; }
"""


def build_html(chapters: list[Chapter]) -> str:
    toc_parts: list[str] = ['<nav class="toc"><h2>目录</h2><ul class="toc-root">']
    body_parts: list[str] = []
    doc_index = 0

    for chapter_index, chapter in enumerate(chapters, start=1):
        chapter_id = f"chapter-{chapter_index}"
        toc_parts.append(
            f'<li class="toc-chapter"><a href="#{chapter_id}">'
            f"{html.escape(chapter.label)}</a><ul class=\"toc-children\">"
        )
        body_parts.append(
            f'<section class="chapter" id="{chapter_id}">'
            f'<h1 class="chapter-title">{html.escape(chapter.label)}</h1>'
        )

        for group in chapter.groups:
            if group.label:
                toc_parts.append(
                    f'<li class="toc-group">{html.escape(group.label)}</li>'
                )

            for doc in group.docs:
                doc_index += 1
                doc_id = f"doc-{doc_index}"
                toc_parts.append(
                    f'<li class="toc-doc"><a href="#{doc_id}">'
                    f"{html.escape(doc.title)}</a></li>"
                )
                body_parts.append(
                    f'<section class="doc" id="{doc_id}">{convert_doc(doc)}</section>'
                )

        toc_parts.append("</ul></li>")
        body_parts.append("</section>")

    toc_parts.append("</ul></nav>")

    return (
        "<!doctype html>\n"
        '<html lang="zh-CN">\n'
        "<head>\n"
        '<meta charset="utf-8">\n'
        '<meta name="viewport" content="width=device-width, initial-scale=1">\n'
        "<title>科研入门指南 · 离线版</title>\n"
        f"<style>{CSS}</style>\n"
        "</head>\n"
        "<body>\n"
        '<section class="cover">'
        "<h1>🔬 科研入门指南</h1>"
        '<p class="subtitle">从 0 开始，掌握做科研、写论文的基本流程</p>'
        '<p class="meta">离线 PDF 版 · 由 GitHub Actions 自动生成</p>'
        "</section>\n"
        + "\n".join(toc_parts)
        + "\n"
        + "\n".join(body_parts)
        + "\n</body>\n</html>\n"
    )


def main() -> None:
    BUILD.mkdir(parents=True, exist_ok=True)
    chapters = collect_chapters()
    doc_count = sum(len(group.docs) for chapter in chapters for group in chapter.groups)

    OUT_HTML.write_text(build_html(chapters), encoding="utf-8")

    print(f"Built {OUT_HTML}")
    print(f"  chapters: {len(chapters)}")
    print(f"  documents: {doc_count}")
    print(f"Next: weasyprint {OUT_HTML} {OUT_PDF}")


if __name__ == "__main__":
    main()
