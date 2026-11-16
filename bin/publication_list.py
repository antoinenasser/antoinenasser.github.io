#!/usr/bin/env python3
"""Build a plain PDF list of publications and talks from the site's .bib files.

Run before `jekyll build` (the deploy workflow and bin/serve do it). Output:
assets/pdf/Antoine_Nasser_publications.pdf, linked from the Publications and Talks pages.
Needs `pip install pybtex typst`.
"""

import datetime
import re
from pathlib import Path

import typst
from pybtex.database import parse_string

ROOT = Path(__file__).resolve().parent.parent
OUTPUT = ROOT / "assets/pdf/Antoine_Nasser_publications.pdf"
NAME = "Antoine Nasser"
WEBSITE = "https://antoinenasser.github.io"
MONTHS = {m: i for i, m in enumerate(["jan", "feb", "mar", "apr", "may", "jun", "jul", "aug", "sep", "oct", "nov", "dec"], 1)}


def read_bib(path):
    text = path.read_text(encoding="utf-8")
    text = re.sub(r"\A---\s*\n.*?---\s*\n", "", text, flags=re.S)  # Jekyll front matter
    return parse_string(text, "bibtex").entries.values()


def plain(text):
    return re.sub(r"[{}]", "", text).replace("\\&", "&").strip()


def initials(given):
    # "Antoine-Alexis" -> "A.-A.", "Julia L." -> "J. L."
    return " ".join("-".join(part[0] + "." for part in word.split("-") if part) for word in given.split())


def authors(entry):
    names = []
    for person in entry.persons.get("author", []):
        last = plain(" ".join(person.prelast_names + person.last_names))
        given = plain(" ".join(person.first_names + person.middle_names))
        names.append(f"{last}, {initials(given)}" if given else last)
    if len(names) == 1:
        return names[0]
    return ", ".join(names[:-1]) + ", & " + names[-1]


def link(entry):
    f = entry.fields
    if "doi" in f:
        return "https://doi.org/" + f["doi"]
    if "arxiv" in f:
        return "https://arxiv.org/abs/" + f["arxiv"]
    if "hal" in f:
        host = "theses.hal.science" if f["hal"].startswith("tel-") else "hal.science"
        return f"https://{host}/{f['hal']}"
    if f.get("slides", "").startswith("http"):
        return f["slides"]
    return f.get("url", "")


def venue(entry):
    f = entry.fields
    if entry.type == "phdthesis":
        return f"[PhD thesis, {plain(f.get('school', ''))}]."
    if entry.type == "inproceedings":
        parts = [plain(f.get("booktitle", "")), plain(f.get("location", ""))]
        return ", ".join(p for p in parts if p) + "."
    text = plain(f.get("journal", ""))
    if "volume" in f:
        text += f", {f['volume']}"
        if "number" in f:
            text += f"({f['number']})"
    if "pages" in f:
        text += ", " + f["pages"].replace("--", "–")
    return text + "."


def reference(entry):
    f = entry.fields
    title = plain(f["title"]).rstrip(".")
    if entry.type == "unpublished":
        return f"{authors(entry)} (in preparation). {title}."
    text = f"{authors(entry)} ({f.get('year', 'n.d.')}). {title}. {venue(entry)}"
    tag = plain(f.get("tag", ""))
    return f"{text} {tag}." if tag else text


def is_peer_reviewed(entry):
    return entry.type == "article" and "tag" not in entry.fields and "preprint" not in entry.fields.get("journal", "").lower()


def sort_key(entry):
    f = entry.fields
    return (int(f.get("year", 0)), MONTHS.get(f.get("month", "").lower()[:3], 0))


def typst_string(text):
    return '"' + text.replace("\\", "\\\\").replace('"', '\\"') + '"'


def section(title, entries):
    if not entries:
        return ""
    items = []
    for entry in sorted(entries, key=sort_key, reverse=True):
        url = link(entry)
        item = f"#{typst_string(reference(entry))}"
        if url:
            item += f" #box(link({typst_string(url)}))"  # a box keeps the URL on one line
        items.append(f"  [{item}],")
    return f"= {title}\n#enum(numbering: \"1.\", spacing: 1em,\n" + "\n".join(items) + "\n)\n"


def main():
    papers = list(read_bib(ROOT / "_bibliography/papers.bib"))
    talks = list(read_bib(ROOT / "_bibliography/talks.bib"))
    today = datetime.date.today().strftime("%-d %B %Y")
    source = f"""#set document(title: "{NAME}: publications and talks", author: "{NAME}")
#set page(paper: "a4", margin: (x: 2.2cm, y: 2cm), numbering: "1")
#set text(size: 10.5pt, ligatures: false, hyphenate: false, lang: "en")
#set par(justify: false)
#show heading: set block(above: 1.6em, below: 1em)
#show link: set text(fill: rgb("#1d4f91"))
#text(size: 17pt, weight: "bold")[{NAME}]

Publications and talks, updated {today}. #link("{WEBSITE}")

{section("Peer-reviewed articles", [e for e in papers if is_peer_reviewed(e)])}
{section("Submitted articles and preprints", [e for e in papers if e.type == "article" and not is_peer_reviewed(e)])}
{section("In preparation", [e for e in papers if e.type == "unpublished"])}
{section("PhD thesis", [e for e in papers if e.type == "phdthesis"])}
{section("Invited talks and seminars", [e for e in talks if e.fields.get("tag", "").startswith("Invited")])}
{section("Contributed presentations", [e for e in talks if not e.fields.get("tag", "").startswith("Invited")])}
"""
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT.write_bytes(typst.compile(source.encode("utf-8")))
    print(f"Wrote {OUTPUT.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
