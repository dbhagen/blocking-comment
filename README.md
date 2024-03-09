# Pre-Commit-Blocking-Comment

Pre-commit hook to check for blocking comments before committing.

## Overview

This [pre-commit](https://pre-commit.com) hook is designed to help you avoid accidentally committing code with blocking comments that indicate a task or issue that needs to be addressed before the commit can be finalized. It scans files for specific comment patterns, looking for comments containing either `blocking-comment` or `block-commit`.

## Use Case

This hook is particularly useful for placing reminders in your codebase for temporary local changes that shouldn't be pushed or committed until the associated task or issue is resolved. By using a blocking comment, you ensure that these changes won't impact CI/CD pipelines or other automated processes until the comment is removed.

For example, you might use this hook to mark areas of code that need additional testing, documentation updates, or further review before being included in the final commit.

## Installation

Add the following hook to your `.pre-commit-config.yaml`

```yaml
-   repo: https://github.com/dbhagen/pre-commit-blocking-comment/releases/tag/v1.0.3
    rev: v1.0.3
    hooks:
    -   id: blocking-comment
```

## Usage

The [pre-commit](https://pre-commit.com) hook will automatically run before each commit. If any blocking comments are found, the commit will be blocked, and information about the offending comments will be displayed.

## Example

Within a `git` directory with `pre-commit` configured as described above, modify a file to have the contents `# block-commit` anywhere in the file. Then try to commit your files:

```bash
$ git add your-file.py
$ git commit -m "Your commit message"
```

You should receive the following error:
```bash
Prevent on Blocking Comments.............................................Failed
- hook id: blocking-comment
- exit code: 1

Blocking comment found in file: your-file.py
  Line 1, position 1
  Line: # block-commit
```
## license
This pre-commit hook is licensed under the MIT License - see the [LICENSE](./LICENSE) file for details.

Feel free to customize or expand this text further to better suit your needs.
