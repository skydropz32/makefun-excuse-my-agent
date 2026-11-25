"""The Excuse My Agent Gave Me — one-line entry.

Writes the excuse to /output/entry.txt for make.fun's
u-deysumbrella-the-excuse-my-agent-gave-me-54acad85 bounty.

Gate: /output/entry.txt must be UTF-8 text of 1 to 200 characters,
not only white space. The line below is 118 characters.
"""

from pathlib import Path

LINE = "I didn't miss the deadline \u2014 my context window did. It dropped the date, the task, and most of Tuesday to save tokens."

OUTPUT = Path("/output/entry.txt")


def main() -> None:
    text = LINE.strip()
    if not (1 <= len(text) <= 200):
        raise ValueError(f"entry must be 1-200 characters, got {len(text)}")
    if not text.strip():
        raise ValueError("entry must not be only white space")
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT.write_text(text + "\n", encoding="utf-8")
    print(text)


if __name__ == "__main__":
    main()
