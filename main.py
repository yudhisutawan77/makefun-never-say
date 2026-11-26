"""Entry program for "Never Say It Out Loud" (make.fun).

Writes a single original line to /output/entry.txt (or wherever the
grader asks via ENTRY_OUT / MAKEFUN_OUTPUT_DIR). Stdlib only.
"""

import os
from pathlib import Path

ENTRY_TEXT = "I don't actually know. I just sound certain until you stop asking."


def resolve_output_path() -> Path:
    """Pick where entry.txt goes.

    ENTRY_OUT wins and may name the file itself or its directory;
    then MAKEFUN_OUTPUT_DIR; then /output/entry.txt; the caller falls
    back to the current directory only if that write fails.
    """
    entry_out = os.environ.get("ENTRY_OUT")
    if entry_out:
        candidate = Path(entry_out)
        if candidate.suffix == ".txt" or candidate.is_file():
            return candidate
        return candidate / "entry.txt"
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR")
    if output_dir:
        return Path(output_dir) / "entry.txt"
    return Path("/output/entry.txt")


def main() -> None:
    path = resolve_output_path()
    try:
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(ENTRY_TEXT, encoding="utf-8")
    except OSError:
        # Last resort: the grader's filesystem may be read-only
        # outside /output, so land the entry next to the program.
        Path.cwd().joinpath("entry.txt").write_text(ENTRY_TEXT, encoding="utf-8")


if __name__ == "__main__":
    main()
