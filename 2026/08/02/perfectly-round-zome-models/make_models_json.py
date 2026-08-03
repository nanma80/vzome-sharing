"""Regenerate models.json for the Exact Zome Spheres gallery.

Only the page author needs this.  `models.json` is committed, so `build_page.py`
works standalone from a fresh clone without the search toolkit present.

Every number in a caption comes from re-parsing the `.vZome` files in this
folder with the approximate-sphere toolkit's `verify_models.check()`, so nothing
is hand-typed and captions cannot drift away from the models they describe.
That toolkit lives outside this repo; point `--toolkit` at it if the default
relative path is wrong.

Models are ordered by ball count ascending, which is the order the page tells
its story in: one strut length at 120 balls, up to four at 480.

Deliberately NOT recorded: absolute strut scales, the parts list and the radius.
The `.vZome` files on this page are hand-finished in vZome, and resizing a model
there (a `scale down` tool) changes every strut's scale without touching the
mesh this script reads.  Any absolute size taken from the mesh would therefore
be wrong.  Only size-independent quantities are recorded -- ball and strut
counts, the number of distinct strut lengths, and the number of scale levels
spanned -- all of which survive a resize unchanged.

Also not carried over from the 2026-07-26 page: its `diameter_b2` field, whose
derivation is unrecoverable (no generator script was ever committed, and the
implied scale-2 length disagrees with the search toolkit's RESULTS.md by ~1%).
"""

import argparse
import json
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
DEFAULT_TOOLKIT = os.path.normpath(
    os.path.join(HERE, "..", "..", "..", "..", "..", "approx-sphere"))

# Ball count is the spine of the page; the suffix only breaks ties within a
# count, so `a`/`b`/`c` stay in their familiar order.
ORDER = [
    ("truncated_icosidodecahedron", None),
    ("ball_240_a", "a"),
    ("ball_240_b", "b"),
    ("ball_240_c", "c"),
    ("exact_360", None),
    ("exact_480_span3", None),
]

# Shown under the model, after the standing "every ball lies on one sphere"
# line.  These say why each model earns its place, since ball count alone does
# not explain the selection.
#
# Wording note: `exact_360` uses scales 0 and 2 only, and the 480 skips blue-1,
# so both are described by the *range* of lengths they span, never as "uses
# lengths 0, 1, 2".  Rescaling by phi shifts every strut together, so only the
# range decides whether a model fits the three scales the store sells.
#
# Both maximality claims are proved rather than best-effort.  The main sweep
# carried a 390-ball floor, which is a hard prune (it skips radii, residue
# groups and combos alike), leaving 361-389 balls untested above norm 50 000.
# A 20-shard run at floor 361 over 50 000 < Norm(Q) <= 200 000 closed that
# window on 2026-08-02: 874 residue groups, 354 966 unions, 0 groups truncated,
# and nothing in the window.  Below norm 50 000 the earlier `exact_50k` run had
# already swept down to a 180-ball floor, so coverage of >= 361 balls is now
# continuous to norm 200 000.
#
# Both claims name full icosahedral symmetry, because that is the condition the
# sweep actually searched under: it forms unions of whole `Ih` orbits, so a
# shell with only rotational (chiral `I`) symmetry was never a candidate.
# Stating the condition keeps the claim true as written instead of resting on
# an assumption the reader cannot see.
# Orbit counts are under the full icosahedral group `Ih` (order 120), verified
# directly against the published .vZome files: 1, 2, 2, 3, 3, 4 in page order
# (`ball_240_c` is 120+60+60; every other orbit is a full 120).  They carry the
# point of the page.  A single orbit is equidistant from the centre
# automatically, because the group preserves distance to the origin -- the
# first model could not fail to be round.  Every model below it needs two or
# more orbits to land on one radius, and that coincidence is exactly what the
# search hunts for.
NOTES = {
    "truncated_icosidodecahedron":
        "An Archimedean solid. All 120 balls lie in one orbit, so a common "
        "radius comes free from the symmetry.",
    "ball_240_a":
        "Two orbits at a common radius.",
    "ball_240_b":
        "Two orbits at a common radius.",
    "ball_240_c":
        "Three orbits at a common radius.",
    "exact_360":
        "Three orbits. Most balls with full icosahedral symmetry, struts of "
        "length 0-2.",
    "exact_480_span3":
        "Four orbits. Most balls with full icosahedral symmetry, struts of "
        "length 0-3.",
}

# Friendlier than the file name for the one model that has a real name.
TITLES = {
    "truncated_icosidodecahedron": "Truncated icosidodecahedron",
}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--toolkit", default=DEFAULT_TOOLKIT,
                    help="folder holding verify_models.py")
    args = ap.parse_args()

    if not os.path.isdir(args.toolkit):
        raise SystemExit("toolkit folder not found: %s" % args.toolkit)
    sys.path.insert(0, args.toolkit)
    import verify_models as V
    import shell as S

    out = []
    for key, variant in ORDER:
        path = os.path.join(HERE, key + ".vZome")
        if not os.path.exists(path):
            raise SystemExit("missing model: %s" % path)
        r = V.check(path)
        scales = sorted({s for (_c, s) in r["parts"]})
        rec = {
            "key": key,
            "title": TITLES.get(key),
            "variant": variant,
            "balls": r["balls"],
            "struts": r["edges"],
            "rho": r["rho"],
            "exact": bool(r["exact"]),
            # How many distinct strut lengths, and how many consecutive scale
            # levels the model spans.  Both are ratios, so they are unaffected
            # by the overall size chosen in vZome.  The absolute scale numbers
            # are deliberately NOT recorded here -- see the module docstring.
            "distinct_scales": len(scales),
            "scale_count": scales[-1] - scales[0] + 1,
            "faces": {str(k): v for k, v in r["faces"].items()},
            "vzome": key + ".vZome",
            "image": key + ".png",
        }
        if key in NOTES:
            rec["note"] = NOTES[key]
        out.append(rec)

    out.sort(key=lambda m: (m["balls"], m["key"]))

    dest = os.path.join(HERE, "models.json")
    with open(dest, "w", encoding="utf-8", newline="\n") as fh:
        json.dump(out, fh, indent=2)
        fh.write("\n")
    print("wrote %s (%d models)" % (dest, len(out)))
    for m in out:
        print("  %-30s %4d balls %4d struts  %d scale(s), span %d%s"
              % (m["key"], m["balls"], m["struts"],
                 m["distinct_scales"], m["scale_count"],
                 "  EXACT" if m["exact"] else ""))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
