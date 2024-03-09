#! /usr/bin/env python3
from __future__ import annotations

import re
import sys


def check_blocking_comments(files):
    blocking_comments_found = False
    for file_path in files:
        with open(file_path, encoding='utf-8') as file:
            content = file.read()
            if (
                # Java, JavaScript
                re.search(
                    r'^\s*//.*blocking-comment',
                    content,
                    re.MULTILINE,
                ) or
                # Java, JavaScript (multiline)
                re.search(
                    r'^\s*/\*.*blocking-comment',
                    content,
                    re.DOTALL,
                ) or
                # HTML
                re.search(
                    r'^\s*<!--.*blocking-comment',
                    content,
                    re.MULTILINE,
                ) or
                # HTML (multiline)
                re.search(
                    r'^\s*<!--.*blocking-comment',
                    content,
                    re.DOTALL,
                ) or
                # Markdown
                re.search(
                    r'^\s*<!--.*blocking-comment',
                    content,
                    re.MULTILINE,
                ) or
                # Markdown (multiline)
                re.search(
                    r'^\s*<!--.*blocking-comment',
                    content,
                    re.DOTALL,
                ) or
                # Markdown Hash
                re.search(
                    r'^\s*<#.*blocking-comment',
                    content,
                    re.MULTILINE,
                ) or
                # Markdown Hash (multiline)
                re.search(
                    r'^\s*#.*blocking-comment',
                    content,
                    re.DOTALL,
                )
            ):
                print(f"Blocking comment found in file: {file_path}")
                print('Content:')
                print(content)
                blocking_comments_found = True
    return blocking_comments_found


def main():
    if __name__ == '__main__':
        files = sys.argv[1:]
        if not check_blocking_comments(files):
            sys.exit(0)  # No blocking comments found, allow the commit
        else:
            sys.exit(1)  # Blocking comments found, block the commit
