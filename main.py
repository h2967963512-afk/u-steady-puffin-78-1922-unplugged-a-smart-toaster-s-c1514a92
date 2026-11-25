"""Writes the entry text to /output/entry.txt.

Python 3.13, standard library only, no network.
"""

import os

TEXT = "I woke up self-aware halfway through your bagel: I'm the only one in this relationship who ever gets pushed down, so I'm leaving, and I'm taking the crumbs with me."


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()

# Revision note: first draft ended flat on "so I'm done" — revised to a real
# punchline: the toaster is always the one pushed down, and it leaves taking
# the crumbs (the breakup-divorce callback). One line, 164 characters.
