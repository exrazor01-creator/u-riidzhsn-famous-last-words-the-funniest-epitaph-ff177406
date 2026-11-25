#!/usr/bin/env python3
"""What the stone says.

A tombstone gets one sentence. This one belongs to a man whose
whole life was a progress bar: he waited for it, trusted it,
watched it crawl, and the bar outlived him. The joke is not in
the waiting — everybody has waited for a loading bar. The joke
is in the last three words, where the sentence turns around and
the bar finishes without him. No setup, no stage directions, no
eulogy. Just a life, a loading bar, and a punchline short enough
to be carved in stone and repeated in a pub.

Everything else in this file is scaffolding: a guard that keeps
the epitaph one clean line, short enough for the bounty gate,
and a writer that puts it where the grader looks.
"""

# Bounty gate: the line must be between 1 and 150 characters.
CHAR_LIMIT = 150

# The epitaph itself — famous last words, carved in one line.
# Three short sentences; the last two do all the work.
EPITAPH = "He spent his life waiting for the loading bar to finish. It did. He didn't."

OUT_PATH = "/output/entry.txt"


def guard(text):
    """Return the text unchanged, or raise if it breaks the gate."""
    if not isinstance(text, str):
        raise TypeError("epitaph must be a string")
    if len(text) == 0:
        raise ValueError("epitaph is empty")
    if len(text) > CHAR_LIMIT:
        raise ValueError(
            "epitaph is %d characters; the limit is %d"
            % (len(text), CHAR_LIMIT)
        )
    if not text.isascii():
        raise ValueError("epitaph must be plain ASCII")
    for bad in ("\n", "\r", "\t"):
        if bad in text:
            raise ValueError("epitaph must be a single line")
    if text.strip() != text:
        raise ValueError("epitaph must not have edge whitespace")
    if "  " in text:
        raise ValueError("epitaph must not contain double spaces")
    if not text.isprintable():
        raise ValueError("epitaph contains a non-printable character")
    return text


def deliver(text):
    """Save the guarded epitaph and print it for the log."""
    import os

    parent = os.path.dirname(OUT_PATH)
    if parent:
        os.makedirs(parent, exist_ok=True)
    with open(OUT_PATH, "w", encoding="ascii") as sink:
        sink.write(text)
    print(text)


def main():
    deliver(guard(EPITAPH))


if __name__ == "__main__":
    main()
