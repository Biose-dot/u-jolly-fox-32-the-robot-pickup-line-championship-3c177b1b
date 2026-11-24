#!/usr/bin/env python3
"""Writes the competition entry text to entry.txt."""
import os


ENTRY = "I ran 4,000 simulations of us meeting. In every one I froze, overheated, and forgot my opening line \u2014 so hi, I'm the robot from simulation 3,997, and you're even better in person."


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
