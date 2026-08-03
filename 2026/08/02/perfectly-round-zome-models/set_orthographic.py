"""Make every viewer on this page open in orthographic projection.

The `View Settings` panel in vzome-viewer has a `Perspective` switch that is
bound to the camera state loaded from the model, not to a hard-coded default:

  * `worker/legacy/parser.js` builds the camera as `perspective: !orthographic`,
    reading the `parallel` attribute of the .vZome `<ViewModel>` element.
  * `viewer/ltcanvas.jsx` renders `<Show when={state.camera.perspective}>` with
    an orthographic camera as the fallback, so the flag picks the actual camera.
  * `viewer/settings.jsx` draws the switch as `checked={state.camera.perspective}`.

So flipping the flag in the files both renders the model orthographically and
leaves the switch unchecked when the panel is opened.  `exact_480_span3` was
already saved this way in desktop vZome and already behaves like this; this
script brings the other five into line.

Both formats are written, for the same reason the camera zoom writes both:
`.shapes.json` is what the web viewer renders, and `.vZome` is what people
download and open in desktop vZome.  The two must agree or the model changes
projection when it moves between them.

Orthographic projection is the honest choice for these models.  The claim the
page makes is that every ball sits at one distance from the centre, and under
perspective the balls nearer the camera are drawn larger, which is exactly the
cue a reader would otherwise read as unequal radii.  Removing the projection
removes that false signal.

Unlike zoom_cameras.py this is idempotent: it sets a flag rather than scaling a
value, so re-running is harmless.  `--check` reports without writing.
"""

import glob
import json
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))


def set_json(text):
    """Clear camera.perspective, leaving the rest of the file byte-identical."""
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

    out, n = re.subn(r'("perspective"\s*:\s*)(true|false)', r"\1false", block)
    if n != 1:
        raise ValueError("expected exactly one 'perspective' in camera, found %d" % n)
    return text[:start] + out + text[end:]


def set_vzome(text):
    """Set parallel="true" on <ViewModel>; the .vZome spells the flag inverted."""
    match = re.search(r"<ViewModel\b[^>]*>", text)
    if not match:
        raise ValueError("no <ViewModel> element")
    out, n = re.subn(r'(parallel=")(true|false)(")', r"\1true\3", match.group(0))
    if n != 1:
        raise ValueError("expected exactly one 'parallel' attribute, found %d" % n)
    return text[:match.start()] + out + text[match.end():]


def main():
    check = "--check" in sys.argv
    for path in sorted(glob.glob(os.path.join(HERE, "*.shapes.json"))):
        name = os.path.basename(path).replace(".shapes.json", "")

        # newline="" on both read and write: these files are CRLF, and letting
        # Python translate on the way in but not on the way out would rewrite
        # every line in the file instead of just the flag.
        with open(path, encoding="utf-8", newline="") as fh:
            before = fh.read()
        after = set_json(before)

        old, new = json.loads(before), json.loads(after)
        was = old["camera"]["perspective"]
        assert new["camera"]["perspective"] is False, name
        # Nothing but the one flag may move: the camera geometry set by
        # zoom_cameras.py has to survive this untouched.
        old["camera"].pop("perspective"), new["camera"].pop("perspective")
        assert old == new, "%s: something outside camera.perspective changed" % name

        vz = os.path.join(HERE, name + ".vZome")
        with open(vz, encoding="utf-8", newline="") as fh:
            vbefore = fh.read()
        vafter = set_vzome(vbefore)
        tag_old = re.search(r"<ViewModel\b[^>]*>", vbefore).group(0)
        tag_new = re.search(r"<ViewModel\b[^>]*>", vafter).group(0)
        for attr in ("distance", "far", "near", "width"):
            a = re.search(r'%s="([^"]*)"' % attr, tag_old).group(1)
            b = re.search(r'%s="([^"]*)"' % attr, tag_new).group(1)
            assert a == b, (name, attr, a, b)
        assert len(vbefore) - len(vafter) in (0, 1), name  # "false"->"true" only

        for label, a, b in (("json", before, after), ("vZome", vbefore, vafter)):
            assert a.count("\r\n") == b.count("\r\n"), "%s %s: line endings changed" % (name, label)
            assert a.count("\n") == b.count("\n"), "%s %s: line count changed" % (name, label)

        verb = "already orthographic" if was is False else ("would set" if check else "set")
        print("%-27s %s" % (name, verb))
        if check or was is False:
            continue

        with open(path, "w", encoding="utf-8", newline="") as fh:
            fh.write(after)
        with open(vz, "w", encoding="utf-8", newline="") as fh:
            fh.write(vafter)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
