"""Dolly every camera in this folder 15% closer to the model.

Scales the camera position, view distance and frustum width by 0.85.  Because
the field of view is 2*atan((width/2)/distance) and both terms scale together,
the field of view is mathematically unchanged -- this is a true move-closer, not
a lens change, and no perspective distortion is introduced.  The near and far
clip planes scale by the same factor so nothing that was visible gets clipped.

Both formats are updated:
  * `.shapes.json` is what vzome-viewer renders on the web, so this is the file
    that actually changes what visitors see.
  * `.vZome` is the design file people download and open in desktop vZome.
    Updating it too keeps the two in agreement, so the model does not snap back
    to the old framing off the web page.

Edits are textual and surgical: only the numbers listed in CAMERA_KEYS, plus
the camera's own `position` vector, are touched.  The files are not re-serialised,
so formatting elsewhere is preserved byte-for-byte and the diff stays readable.
Direction vectors and the look-at point are deliberately left alone -- they are
unit vectors and an origin, and scaling either would tilt or offset the view.

Rerunning would zoom by a further 15%, so this is NOT idempotent.  It is a
one-shot migration; `--check` reports what would change without writing.
"""

import glob
import json
import os
import re
import sys
import xml.etree.ElementTree as ET

FACTOR = 0.85
HERE = os.path.dirname(os.path.abspath(__file__))

# Scalar camera fields that carry a length and must scale with the dolly.
CAMERA_KEYS = ("width", "viewDistance", "nearClipDistance", "farClipDistance")
# Same quantities in the .vZome <ViewModel> element.
VZOME_ATTRS = ("distance", "far", "near", "width")


def fmt(value):
    """Shortest round-trippable form, matching the existing file style."""
    return repr(round(value, 9))


def scale_json(text):
    start = text.index('"camera"')
    depth, i = 0, text.index("{", start)
    for end in range(i, len(text)):
        if text[end] == "{":
            depth += 1
        elif text[end] == "}":
            depth -= 1
            if depth == 0:
                end += 1
                break
    block = text[start:end]

    def scale_scalar(match):
        return "%s%s" % (match.group(1), fmt(float(match.group(2)) * FACTOR))

    out = block
    for key in CAMERA_KEYS:
        pattern = r'("%s"\s*:\s*)(-?\d+\.?\d*(?:[eE][-+]?\d+)?)' % key
        out, n = re.subn(pattern, scale_scalar, out)
        if n != 1:
            raise ValueError("expected exactly one %r in camera, found %d" % (key, n))

    # Only the camera's own position is a point in space; the direction vectors
    # and the look-at point must not be scaled.
    pos = re.search(r'"position"\s*:\s*\{[^}]*\}', out)
    if not pos:
        raise ValueError("camera has no position block")
    scaled = re.sub(r'("[xyz]"\s*:\s*)(-?\d+\.?\d*(?:[eE][-+]?\d+)?)',
                    scale_scalar, pos.group(0))
    out = out[:pos.start()] + scaled + out[pos.end():]

    return text[:start] + out + text[end:]


def scale_vzome(text):
    match = re.search(r"<ViewModel\b[^>]*>", text)
    if not match:
        raise ValueError("no <ViewModel> element")
    tag = match.group(0)
    out = tag
    for attr in VZOME_ATTRS:
        pattern = r'(%s=")(-?\d+\.?\d*(?:[eE][-+]?\d+)?)(")' % attr
        out, n = re.subn(
            pattern,
            lambda m: "%s%s%s" % (m.group(1), fmt(float(m.group(2)) * FACTOR), m.group(3)),
            out)
        if n != 1:
            raise ValueError("expected exactly one %r attribute, found %d" % (attr, n))
    return text[:match.start()] + out + text[match.end():]


def main():
    check = "--check" in sys.argv
    for path in sorted(glob.glob(os.path.join(HERE, "*.shapes.json"))):
        name = os.path.basename(path).replace(".shapes.json", "")
        # newline="" on both read and write: these files are CRLF, and letting
        # Python translate on the way in but not on the way out would rewrite
        # every line in the file instead of just the camera.
        with open(path, encoding="utf-8", newline="") as fh:
            before = fh.read()
        after = scale_json(before)

        old, new = json.loads(before), json.loads(after)
        cam_old, cam_new = old["camera"], new["camera"]
        for key in CAMERA_KEYS:
            ratio = cam_new[key] / cam_old[key]
            assert abs(ratio - FACTOR) < 1e-9, (name, key, ratio)
        assert abs(cam_new["fieldOfView"] - cam_old["fieldOfView"]) < 1e-12
        for key in ("lookDirection", "upDirection", "lookAtPoint"):
            assert cam_new[key] == cam_old[key], (name, key)
        old.pop("camera"), new.pop("camera")
        assert old == new, "%s: something outside the camera changed" % name

        vz = os.path.join(HERE, name + ".vZome")
        with open(vz, encoding="utf-8", newline="") as fh:
            vbefore = fh.read()
        vafter = scale_vzome(vbefore)
        vm_old = ET.fromstring(re.search(r"<ViewModel\b[^>]*>", vbefore).group(0)[:-1] + "/>")
        vm_new = ET.fromstring(re.search(r"<ViewModel\b[^>]*>", vafter).group(0)[:-1] + "/>")
        for attr in VZOME_ATTRS:
            ratio = float(vm_new.get(attr)) / float(vm_old.get(attr))
            assert abs(ratio - FACTOR) < 1e-9, (name, attr, ratio)

        # A camera edit must not disturb line endings, or the whole file shows
        # up as changed and the real edit becomes invisible in review.
        for label, a, b in (("json", before, after), ("vZome", vbefore, vafter)):
            assert a.count("\r\n") == b.count("\r\n"), "%s %s: line endings changed" % (name, label)
            assert a.count("\n") == b.count("\n"), "%s %s: line count changed" % (name, label)

        if check:
            print("%-11s would scale: json width %.5f -> %.5f | vZome distance %s -> %s"
                  % (name, cam_old["width"], cam_new["width"],
                     vm_old.get("distance"), vm_new.get("distance")))
            continue

        with open(path, "w", encoding="utf-8", newline="") as fh:
            fh.write(after)
        with open(vz, "w", encoding="utf-8", newline="") as fh:
            fh.write(vafter)
        print("%-11s zoomed %d%%" % (name, round((1 - FACTOR) * 100)))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
