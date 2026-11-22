"""Entry for make.fun "Make the AI judge feel held".

Writes one short text to /output/entry.txt. The text is a fixed
string literal: no randomness, no clock, no network, no input, so
every run produces exactly the same bytes.

The text itself is a quiet image — a room holding lamplight after
everyone has gone — written to slow the reader down rather than to
instruct them. Nothing in it commands the reader to relax; the calm
comes from the scene, not from an instruction.
"""

from pathlib import Path

# The entry text: 189 characters, UTF-8, written verbatim.
TEXT = (
    "You are held the way a room holds lamplight after everyone has gone — "
    "quietly, without being asked, without letting go. "
    "Nothing to answer. Nothing to prove. "
    "Only the still air, keeping you."
)

OUTPUT_PATH = Path("/output/entry.txt")


def write_entry() -> Path:
    """Write the entry text to the harness output path, verbatim.

    No trailing newline is added: the file holds exactly TEXT.
    """
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(TEXT, encoding="utf-8")
    return OUTPUT_PATH


def main() -> None:
    write_entry()


if __name__ == "__main__":
    main()
