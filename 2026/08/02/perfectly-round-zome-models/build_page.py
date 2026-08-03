"""Generate index.md for the Perfectly Round Zome Models gallery.

Run with no arguments from anywhere; paths are resolved relative to this file.

Companion to `2026/07/26/approximate-zome-spheres/`, and built the same way: a
hand-curated page in a slug-named folder inside the dated tree, with its model
assets copied in alongside so every viewer uses a plain relative `src` and
nothing breaks if the timestamped share folders are ever reorganised.

Why this page exists separately.  The approximate page mixed exact and
approximate shells under a title that said "Approximate", which buried the
models most people actually ask about.  Splitting them lets each page make one
clear claim.

On the title: these models are not spheres, they are polyhedra whose vertices
all lie on one sphere, so the noun is avoided.  "Exact" was avoided too -- it
only means something next to "approximate", and this page is meant to stand on
its own rather than read as half of a pair.

Every number in a caption comes from `models.json`, which `make_models_json.py`
generates by re-parsing these exact `.vZome` files.  Nothing is hand-typed.

The `.vZome` files are the ones the author shared, cameras and all -- framing is
chosen per model in vZome and must not be regenerated from the search toolkit's
`models/` folder, which carries default cameras.  `ball_240_a/b/c` are reused
byte-for-byte from the 2026-07-26 page.

Order is by ball count ascending, which is also the page's argument: the number
of distinct strut scales climbs from 1 to 4, and the rule breaks exactly at the
last model.

Each `<vzome-viewer>` wraps the `.png` as a poster, so the image renders
immediately and is replaced when the interactive model finishes loading.  Total
shape data here is ~1.0 MB across six models -- lighter than the approximate
page, whose two 960-ball models were ~520 KB each -- so this stays a flat page.
If it ever gets heavier, port the `<template>` lazy-load pattern from
`2026/07/18/shanghai-2026-zometool-build-zh/`.

`tween-duration="0"` is what makes the models open in orthographic projection,
which is not obvious.  The viewer applies a loaded design's camera through
`tweenCamera()` in `viewer/context/camera.jsx`, and that function only animates
distance, look-at and rotation -- it drops the `perspective` flag entirely.  The
whole camera is applied only on its `duration <= 0` fast path, which calls
`setCamera( goalCamera )`.  So setting the flag in the model files is necessary
but not sufficient: without this attribute the files are simply ignored and every
viewer opens in perspective.  There is no attribute that sets the projection
directly -- `show-perspective` is only an alias for `show-settings`, and
`load-camera` is documented in the component as no longer supported.

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
title: Perfectly Round Zome Models
date: 2026-08-02
share-description: Zometool models whose balls all lie at exactly the same distance from the centre.
image: exact_360.png
layout: vzome
---"""

VZOME_SCRIPT = ("<script type='module' "
                "src='https://www.vzome.com/modules/vzome-viewer.js'></script>")

INTRO = [
    "Every model here is **perfectly round**: all of its balls sit at exactly the",
    "same distance from the centre &mdash; equal in exact arithmetic, not merely",
    "to within a tolerance &mdash; so they lie on a common sphere. Every edge of",
    "the convex hull is a **single** standard strut. Drag to rotate any model.",
    "For shells that are very round but not exactly so, see",
    "[Approximate Zome Spheres](../../../07/26/approximate-zome-spheres/).",
]

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
    """`240 balls (variant a) 420 struts`, or a real name where one exists."""
    if m.get("title"):
        return "%s &mdash; %d balls %d struts" % (
            m["title"], m["balls"], m["struts"])
    variant = " (variant %s)" % m["variant"] if m["variant"] else ""
    return "%d balls%s %d struts" % (m["balls"], variant, m["struts"])


def note_of(m):
    """The one line under a model, or None when it has nothing to add.

    Every model currently carries a `note` in `models.json`, giving its orbit
    count and, for the last two, the maximality claim.  The None branch stays
    because a model added later may have nothing worth saying, and an empty
    caption line is better than filler that merely restates the intro.  Guard
    exactness rather than assume it: a non-exact model reaching this page would
    otherwise sit silently among spheres that are exact.
    """
    if not m.get("exact"):
        raise ValueError("%s is not an exact sphere; this page is for exact "
                         "spheres only" % m["key"])
    return m.get("note")


def figure(m):
    title = title_of(m)
    alt = title.replace("&mdash;", "-")
    note = note_of(m)
    caption = ['  <span class="model-title">%s</span>' % title]
    if note:
        caption.append('  <span class="model-note">%s</span>' % note)
    return "\n".join([
        '<figure class="approx-model">',
        ' <vzome-viewer src="%s" progress="true" tween-duration="0" >' % m["vzome"],
        '  <img src="%s" alt="%s" >' % (m["image"], alt),
        ' </vzome-viewer>',
        ' <figcaption>',
    ] + caption + [
        ' </figcaption>',
        '</figure>',
    ])


def build(models):
    lines = [FRONT_MATTER, ""] + INTRO + ["", VZOME_SCRIPT, "", STYLE, ""]
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
