#!/usr/bin/env python3
"""Write the one word this entry erases from the dictionary to /output/entry.txt.

The word is "queue": five letters, four of them silent. Deleting it
removes the most inefficient word in English — a word that is eighty
percent silence — and leaves every line of people waiting with no name.
"""

import os


def main():
    erased = "queue"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as out:
        out.write(erased)


if __name__ == "__main__":
    main()
