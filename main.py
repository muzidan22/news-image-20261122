"""news-image-20261122 entry: writes one image summing up 22 November 2026 world news.

The image is the entry.png beside this file; the program copies it to the output
directory the grader gives (MAKEFUN_OUTPUT_DIR, or /output in the sandbox). It runs
twice and copies identical bytes each time, with no network access and only the
Python 3.13 standard library.
"""
import os
import shutil

HERE = os.path.dirname(os.path.abspath(__file__))
SOURCE = os.path.join(HERE, "entry.png")
OUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")


def main():
    # The composed front page must sit beside the program before we copy it.
    if not os.path.isfile(SOURCE):
        raise FileNotFoundError(f"entry.png not found beside the program: {SOURCE}")
    os.makedirs(OUT_DIR, exist_ok=True)
    destination = os.path.join(OUT_DIR, "entry.png")
    shutil.copyfile(SOURCE, destination)
    # Read the copy back: both runs must leave byte-identical output.
    with open(SOURCE, "rb") as src, open(destination, "rb") as dst:
        if src.read() != dst.read():
            raise IOError("copied entry.png differs from the source bytes")
    return destination  # the same bytes on every run: deterministic, no network


if __name__ == "__main__":
    main()
