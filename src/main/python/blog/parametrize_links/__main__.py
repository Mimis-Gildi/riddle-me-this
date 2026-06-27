"""Executable entry: python -m blog.parametrize_links <article.adoc>"""

import sys

from . import main

if __name__ == "__main__":
    main(sys.argv[1])
