"""One-line review of the most boring everyday object: a rubber band.

The program writes a single funny, true review line to
$MAKEFUN_OUTPUT_DIR/entry.txt (default /output/entry.txt).

The joke: a rubber band's whole career is holding things together
while doing nothing interesting, and it ends the same way every
rubber band ends -- by perishing and snapping in your face the one
time you actually need it. That is exactly how rubber bands behave:
they dry out in a drawer, go brittle, and snap without warning.
"""

import os

REVIEW = (
    "Five stars. It held my cables together for three years, then "
    "retired by snapping in my face on the one morning I actually "
    "needed it."
)

MAX_CHARS = 200


def check_line(line):
    """Enforce the bounty gate locally before writing anything.

    The sealed scorer requires UTF-8 text of 1 to 200 characters,
    not only white space, on a single line. Fail loudly here so a
    bad line never reaches the judge.
    """
    text = line.encode("utf-8").decode("utf-8")
    if not 1 <= len(text) <= MAX_CHARS:
        raise ValueError("review must be 1-200 characters, got %d" % len(text))
    if not text.strip():
        raise ValueError("review must not be only whitespace")
    if "\n" in text or "\r" in text:
        raise ValueError("review must stay on one line")
    return text


def main():
    review = check_line(REVIEW)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "wb") as f:
        f.write(review.encode("utf-8"))
    os.chmod(path, 0o644)


if __name__ == "__main__":
    main()
