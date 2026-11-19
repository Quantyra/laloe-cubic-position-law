"""Build manuscript.pdf from manuscript.md with Pandoc 3.9 and Typst 0.15.2."""

from pathlib import Path
from tempfile import TemporaryDirectory

import pypandoc
import typst


def main():
    root = Path(__file__).resolve().parent
    with TemporaryDirectory() as scratch:
        typeset = Path(scratch) / "manuscript.typ"
        pypandoc.convert_file(str(root / "manuscript.md"), "typst",
                              format="markdown", extra_args=["--standalone"],
                              outputfile=str(typeset))
        pdf = typst.compile(str(typeset), timestamp=1794960000)
    (root / "manuscript.pdf").write_bytes(pdf)


if __name__ == "__main__":
    main()
