"""Assemble a repository from templates/, turning each `dot-` prefix into a leading dot.

The templates keep their dotfiles as `dot-claude/`, `dot-gitignore` and so on, so that
the `.claude/` folder of an example project is never read as live configuration by a
session working in this repository. This script writes the real names into a target.

    python scripts/assemble_templates.py <target> [--force]

It refuses to overwrite an existing file unless --force is given. Run from the
repository root.
"""

from __future__ import annotations

import argparse
import shutil
import sys
from pathlib import Path

TEMPLATES = Path(__file__).resolve().parent.parent / "templates"
SKIP = {"README.md"}


def real(relative: Path) -> Path:
    return Path(*("." + part[4:] if part.startswith("dot-") else part for part in relative.parts))


def assemble(target: Path, force: bool = False) -> list[Path]:
    written = []
    for source in sorted(TEMPLATES.rglob("*")):
        if not source.is_file() or source.relative_to(TEMPLATES).as_posix() in SKIP:
            continue
        destination = target / real(source.relative_to(TEMPLATES))
        if destination.exists() and not force:
            raise FileExistsError(f"{destination} exists; pass --force to overwrite")
        destination.parent.mkdir(parents=True, exist_ok=True)
        shutil.copyfile(source, destination)
        written.append(destination.relative_to(target))
    return written


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    parser.add_argument("target")
    parser.add_argument("--force", action="store_true")
    args = parser.parse_args(argv)
    try:
        for path in assemble(Path(args.target), args.force):
            print(path.as_posix())
    except FileExistsError as error:
        print(error)
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
