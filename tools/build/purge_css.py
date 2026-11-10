"""Build a lean stylesheet for a set of pages from the site's full stylesheet.

The writing pages use only a fraction of assets/site.css (which also styles the home page, case studies, the Lab,
pricing and contact). This keeps every rule whose selectors can match something on the given pages, plus
everything that has no selectors to test (@font-face, @keyframes, @view-transition, :root tokens), and writes
the result minified. Classes added by JavaScript are found by scanning assets/site.js for quoted words.

Usage (from writing.py): purge(pages=[...html paths...], out="assets/writing.css")
"""
import os
import re

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))


def _used(pages, scripts=()):
    classes, ids, tags = set(), set(), set()
    for f in pages:
        h = open(f).read()
        for m in re.findall(r'\sclass="([^"]*)"', h):
            classes.update(m.split())
        ids.update(re.findall(r'\sid="([^"]+)"', h))
        tags.update(t.lower() for t in re.findall(r"<([a-zA-Z][a-zA-Z0-9-]*)", h))
    js = open(os.path.join(ROOT, "assets", "site.js")).read()
    words = set(re.findall(r"""["']([a-zA-Z][\w-]*)["']""", js))
    for f in scripts:  # page scripts that build markup from strings: keep every word that could be a class
        words |= set(re.findall(r"[a-zA-Z][\w-]*", open(os.path.join(ROOT, f)).read()))
    classes |= words
    ids |= words
    return classes, ids, tags


def _split(css):
    """Split a block of CSS into top-level items: (prelude, body) for blocks, or (statement, None)."""
    items, i, n = [], 0, len(css)
    while i < n:
        j = i
        depth = 0
        while j < n:
            c = css[j]
            if c == "{":
                break
            if c == ";" and depth == 0:
                break
            j += 1
        if j >= n:
            break
        if css[j] == ";":
            items.append((css[i:j + 1].strip(), None))
            i = j + 1
            continue
        prelude = css[i:j].strip()
        depth, k = 1, j + 1
        while k < n and depth:
            if css[k] == "{":
                depth += 1
            elif css[k] == "}":
                depth -= 1
            k += 1
        items.append((prelude, css[j + 1:k - 1]))
        i = k
    return items


_PSEUDO_FN = re.compile(r":(?:not|is|where|has)\(([^()]*(?:\([^()]*\)[^()]*)*)\)")


def _matches(selector, classes, ids, tags):
    sel = _PSEUDO_FN.sub(lambda m: "" if m.group(0).startswith(":not") else " " + m.group(1), selector)
    sel = re.sub(r"::?[\w-]+(\([^)]*\))?", "", sel)       # other pseudo-classes and pseudo-elements
    sel = re.sub(r"\[[^\]]*\]", "", sel)                   # attribute selectors: always allowed
    for c in re.findall(r"\.(-?[_a-zA-Z][\w-]*)", sel):
        if c not in classes:
            return False
    for i in re.findall(r"#(-?[_a-zA-Z][\w-]*)", sel):
        if i not in ids:
            return False
    for t in re.findall(r"(?:^|[\s>+~(,])([a-z][a-z0-9-]*)", sel):
        if t not in tags and t not in ("html", "body"):
            return False
    return True


def _keep(css, used):
    out = []
    for prelude, body in _split(css):
        if body is None:
            if not prelude.startswith("@import"):
                out.append(prelude)
            continue
        if prelude.startswith("@media") or prelude.startswith("@supports") or prelude.startswith("@layer"):
            inner = _keep(body, used)
            if inner:
                out.append(f"{prelude}{{{inner}}}")
        elif prelude.startswith("@"):
            out.append(f"{prelude}{{{body}}}")             # @font-face, @keyframes, @view-transition…
        else:
            sels = [s.strip() for s in prelude.split(",")]
            kept = [s for s in sels if _matches(s, *used)]
            if kept:
                out.append(f"{','.join(kept)}{{{body}}}")
    return "".join(out)


def _minify(css):
    css = re.sub(r"/\*.*?\*/", "", css, flags=re.S)
    css = re.sub(r"\s+", " ", css)
    css = re.sub(r"\s*([{};,>])\s*", r"\1", css)
    css = css.replace(";}", "}")
    return css.strip() + "\n"


def purge(pages, out, js=()):
    full = open(os.path.join(ROOT, "assets", "site.css")).read()
    full = re.sub(r"/\*.*?\*/", "", full, flags=re.S)
    lean = _minify(_keep(full, _used(pages, js)))
    with open(os.path.join(ROOT, out), "w") as f:
        f.write(lean)
    return len(full), len(lean)
