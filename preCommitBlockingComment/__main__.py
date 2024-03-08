#!/usr/bin/env python3
from __future__ import annotations

import re
import sys


def check_comments(filename):
    with open(filename) as file:
        content = file.read()
        # Check for comments containing "block-commit"
        comment_patterns = [
            r'#.*block-commit',   # Python
            r'\/\/.*block-commit',  # JavaScript
            r'\/\*.*block-commit',  # Java
        ]

        for pattern in comment_patterns:
            if re.search(pattern, content):
                print(
                    f"Error: Commit contains a comment with 'block-commit': {
                        filename
                    }",
                )
                return False
    return True


def pre_commit_hook(files):
    for file in files:
        if not check_comments(file):
            return 1
    return 0


if __name__ == '__main__':
    # Get the list of staged files
    staged_files = sys.argv[1:]

    # Run the pre-commit hook
    sys.exit(pre_commit_hook(staged_files))
