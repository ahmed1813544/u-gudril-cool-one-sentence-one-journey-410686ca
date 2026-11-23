"""One Sentence, One Journey.

Writes a single complete story about a journey, told in exactly one
sentence, to $MAKEFUN_OUTPUT_DIR/entry.txt (default /output/entry.txt).

Deterministic: the same sentence is written on every run, with no
network, no randomness, no file reads and no third-party imports.

The output file holds the sentence followed by a single trailing
newline, and nothing else: no title, no second sentence, no
explanation.
"""

import os

SENTENCE = (
    "Mara set out before dawn with a kettle of cold coffee and her "
    "grandfather's brass compass, crossed three borders on a bus that "
    "smelled of diesel and oranges, and when the road finally ended at "
    "the sea, she buried the compass in the sand and walked home by the "
    "stars instead."
)


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as fh:
        fh.write(SENTENCE + "\n")


if __name__ == "__main__":
    main()
