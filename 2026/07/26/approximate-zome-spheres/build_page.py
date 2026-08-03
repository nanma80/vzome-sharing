"""Generate index.md for the Approximate Zome Spheres gallery.

Run with no arguments from anywhere; paths are resolved relative to this file.

This folder follows the pattern set by
`2026/07/18/shanghai-2026-zometool-build-zh/`: a hand-curated page living in a
slug-named folder inside the dated tree, with its model assets copied in
alongside it.  Everything the page needs is local, so the viewers use plain
relative `src` attributes and nothing breaks if the timestamped share folders
this was assembled from are ever reorganised.

Every number in a caption comes from `models.json`, which was produced by
re-parsing these exact `.vZome` files with the approximate-sphere toolkit's
`verify_models.py`.  Nothing is hand-typed, so captions cannot drift away from
the models they describe.

Captions are deliberately two lines: what it is, and how round it is.
`models.json` still carries the parts list, diameter, radius and face counts,
so restoring any of them is a one-line change in `figure()` -- the data is kept
even though the page does not currently show it.

Each `<vzome-viewer>` wraps the `.png` as a poster.  The image renders
immediately and is replaced when the interactive model finishes loading, which
matters here: the two 960-ball models are ~520 KB of shape data each.

The Shanghai page puts its viewers inside a `<template>` that is cloned on
expand, so only one group loads at a time.  This page deliberately does not do
that yet -- with six models we want to measure the flat-page cost first.  If it
turns out to be too slow, port that pattern over.

Note: this repo's `replace-host-url` workflow rewrites `nanma80.github.io` to
`www.nan.ma` across every file on push.  Write any absolute URL in the
`www.nan.ma` form already so the committed text matches what is published.

Idempotent: rerunning with an unchanged models.json produces no diff.
"""

import json
import os

HERE = os.path.dirname(os.path.abspath(__file__))
MODELS_JSON = os.path.join(HERE, "models.json")
OUT_MD = os.path.join(HERE, "index.md")

FRONT_MATTER = """---
title: Approximate Zome Spheres
date: 2026-07-26
share-description: Hollow Zometool shells whose balls all lie on one sphere.
image: ball_960_a.png
layout: vzome
---"""

VZOME_SCRIPT = ("<script type='module' "
                "src='https://www.vzome.com/modules/vzome-viewer.js'></script>")

STYLE = """<style>
  .approx-model {
    box-sizing: border-box;
    border: 1px solid #ddd;
    border-radius: 0.5rem;
    background: #fff;
    margin: 2rem auto;
    max-width: min(100%, 72dvh);
    padding: 0.25rem;
    width: 100%;
  }
  .approx-model vzome-viewer {
    display: block;
    width: 100%;
    aspect-ratio: 1 / 1;
    height: auto;
  }
  .approx-model vzome-viewer img {
    width: 100%;
    height: auto;
  }
  .approx-model figcaption {
    color: #24292f;
    margin: 0.75rem 0 0.5rem;
    text-align: center;
  }
  .approx-model figcaption .model-title {
    display: block;
    font-weight: 600;
  }
  .approx-model figcaption .model-note {
    color: #57606a;
    display: block;
    margin-top: 0.2rem;
  }
</style>"""


def title_of(m):
    """`240 balls (variant a) 420 struts`."""
    variant = " (variant %s)" % m["variant"] if m["variant"] else ""
    return "%d balls%s %d struts" % (m["balls"], variant, m["struts"])


def is_exact(m):
    """True when every ball is the same distance from the centre.

    The hull code works in floats, so an exact sphere comes back as
    0.99999999999999978 rather than 1.0 -- comparing `rho == 1` silently
    misclassifies all three 240-ball models.  Round to 9 places first, the same
    tolerance `pareto.py` uses in the search toolkit.
    """
    return round(m["rho"], 9) >= 1.0


def note_of(m):
    """One short line about roundness, as a rounded percentage.

    vZome reports ratios this way, so the page matches it.  Unlike a bare
    ">" claim, a rounded "approximately" figure is honest in both directions,
    which matters for ball_360: its rho is 0.99959975, so "> 0.9996" would
    have been false by a hair while "~ 99.96%" is right.

    Guard: a shell that is very round but not perfect must not round up to a
    flat 100.00%, which would contradict the exact-sphere wording above.  Add
    decimals until the figure is distinguishable from 100.
    """
    if is_exact(m):
        return "Every ball lies on one sphere."
    for places in (2, 3, 4, 5, 6):
        pct = "%.*f" % (places, m["rho"] * 100)
        if float(pct) < 100.0:
            return "Ratios between radii &asymp; %s%%" % pct
    raise ValueError("rho indistinguishable from 1 but not exact: %r" % m["rho"])


def figure(m):
    title = title_of(m)
    return "\n".join([
        '<figure class="approx-model">',
        ' <vzome-viewer src="%s" progress="true" >' % m["vzome"],
        '  <img src="%s" alt="%s" >' % (m["image"], title),
        ' </vzome-viewer>',
        ' <figcaption>',
        '  <span class="model-title">%s</span>' % title,
        '  <span class="model-note">%s</span>' % note_of(m),
        ' </figcaption>',
        '</figure>',
    ])


def build(models):
    lines = [
        FRONT_MATTER,
        "",
        "Each model is a hollow Zometool shell: every ball sits on one thin spherical",
        "shell centred on the origin, and every edge of the convex hull is a **single**",
        "standard strut (RGBY, scales 0-3, no concatenation). Drag to rotate any model.",
        "",
        "The three 240-ball shells here are exactly round: their radii are equal in",
        "exact arithmetic, not merely to within a tolerance. More models like them are",
        "collected in [Perfectly Round Zome Models](../../../08/02/perfectly-round-zome-models/).",
        "",
        VZOME_SCRIPT,
        "",
        STYLE,
        "",
    ]
    for m in models:
        lines.append(figure(m))
        lines.append("")
    return "\n".join(lines).rstrip() + "\n"


def main():
    with open(MODELS_JSON, encoding="utf-8") as fh:
        models = json.load(fh)

    missing = [f for m in models for f in (m["vzome"], m["image"])
               if not os.path.exists(os.path.join(HERE, f))]
    if missing:
        raise SystemExit("assets referenced but not present: %s" % ", ".join(missing))

    text = build(models)
    old = None
    if os.path.exists(OUT_MD):
        with open(OUT_MD, encoding="utf-8") as fh:
            old = fh.read()
    if old == text:
        print("index.md already up to date (%d models)" % len(models))
        return 0
    with open(OUT_MD, "w", encoding="utf-8", newline="\n") as fh:
        fh.write(text)
    print("wrote %s (%d models)" % (OUT_MD, len(models)))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
