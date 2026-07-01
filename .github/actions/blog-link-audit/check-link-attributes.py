#!/usr/bin/env python3
"""Blog link attribute checker — composite action entry point."""
import os
import sys


def main():
    print(f"Python: {sys.version}")
    print(f"Conda env: {os.environ.get('CONDA_DEFAULT_ENV', '(not set)')}")


if __name__ == "__main__":
    main()