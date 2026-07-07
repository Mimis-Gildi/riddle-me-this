"""Executable entry: python -m blog.parametrize_links [--csv [DIR]]"""

import sys
from pathlib import Path

from . import main, SITE_ROOT

if __name__ == "__main__":
    args = sys.argv[1:]
    csv_dir = None
    if "--csv" in args:
        idx = args.index("--csv")
        csv_dir = Path(args[idx + 1]) if idx + 1 < len(args) else SITE_ROOT.parent / "reports"
    sys.exit(main(csv_dir=csv_dir))
