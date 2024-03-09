#! /usr/bin/env python3
from __future__ import annotations

import pathlib

from setuptools import setup

here = pathlib.Path(__file__).parent.resolve()

# Get the long description from the README file
long_description = (here / 'README.md').read_text(encoding='utf-8')

setup(
    name='blocking-comment',
    version='1.0.4',
    description='Pre-commit hook to check for blocking comments before commit',
    author='Daniel Hagen',
    author_email='<5039466+dbhagen@users.noreply.github.com>',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/dbhagen/blocking-comment',
    python_requires='>=3.7, <4',
    entry_points={
        'console_scripts': [
            'blockingcomment=blockingcomment:main',
        ],
    },
    scripts=[
        'blockingcomment.py',
    ],
)
