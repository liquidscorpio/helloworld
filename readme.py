#!/usr/bin/env python

import os

skiplist = [
    'README.md',
    'readme.py'
]

rename_map = {
    'erlaang': 'erlang',
}

def proper_name(name):
    v = rename_map.get(name)
    return v if v else name

readme = ''
for path in sorted(os.listdir('.'), key=lambda x: x.lower()):
    if os.path.isfile(path) and path not in skiplist:
        with open(path, 'r') as curfile:
            code = curfile.read()
            lang = proper_name(os.path.splitext(path)[0])
            readme += "{0}\n-----\n```{1}\n{2}```\n\n".format(lang.title(), lang, code)

with open('README.md', 'w') as outfile:
    outfile.write("""
This repository contains code that outputs "Hello World" to stdout
in various programming languages.
"Hello World" programs are typically the first code most new comers
use to interface with a programming language. Per
[this Stackoverflow answer](https://stackoverflow.com/a/12785204)
such programs were first used by Brian Kernighan and Martin Richards
at Bell Labs during 1970s and tradition has since been honored by
many new programming language books, tutorials and courses.\n\n
""")
    outfile.write(readme)

