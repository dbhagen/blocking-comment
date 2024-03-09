#! /usr/bin/env python3
from __future__ import annotations

import re
import sys


def check_blocking_comments(files):
    blocking_comments_found = False
    for file_path in files:
        with open(file_path) as file:
            print(f"Processing file: {file_path}")
            content = file.read()
            if (
                # Java, JavaScript, Python, HTML comments
                re.search(
                    r'^\s*(//|/\*|#|<!--).*?(blocking-comment|block-commit)',
                    content,
                    re.MULTILINE,
                )
                or
                re.search(
                    r'(\s+|^)(//|/\*|#|<!--).*?(blocking-comment|block-commit).*?(\s+|$)',  # noqa: E501
                    content,
                    re.MULTILINE,
                )  # Comment at the end of a line
            ):
                print(f"Blocking comment found in file: {file_path}")
                print('Content:')
                print(content)
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
