#! /usr/bin/env python3
from __future__ import annotations

import re
import sys


def check_blocking_comments(files):
    blocking_comments_found = False
    for file_path in files:
        with open(file_path) as file:
            lines = file.readlines()
            for line_num, line in enumerate(lines, start=1):
                matches = re.finditer(
                    r'(//|/\*|#|<!--).*?(blocking-comment|block-commit)', line,
                )
                for match in matches:
                    print(f"Blocking comment found in file: {file_path}")
                    print(f"  Line {line_num}, position {match.start()}")
                    print(f"  Line: {line.strip()}")
                    blocking_comments_found = True
    return blocking_comments_found


def main():
    files = sys.argv[1:]
    if not check_blocking_comments(files):
        sys.exit(0)  # No blocking comments found, allow the commit
    else:
        sys.exit(1)  # Blocking comments found, block the commit


if __name__ == '__main__':
    main()
