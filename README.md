# md2html

[![GitHub issues](https://img.shields.io/github/issues/anbuhckr/md2html)](https://github.com/anbuhckr/md2html/issues)
[![GitHub forks](https://img.shields.io/github/forks/anbuhckr/md2html)](https://github.com/anbuhckr/md2html/network)
[![GitHub stars](https://img.shields.io/github/stars/anbuhckr/md2html)](https://github.com/anbuhckr/md2html/stargazers)
[![GitHub license](https://img.shields.io/github/license/anbuhckr/md2html)](./LICENSE)
![PyPI - Python Version](https://img.shields.io/badge/python-3.6%20%7C%203.7%20%7C%203.8%20%7C%203.9-blue)

md2html is python library for converting markdown to html with nice code blocks.

## Table of Contents

* [Installation](#installation)
* [CLI](#cli)
* [Getting Started](#getting-started)
* [Ref](#ref)


## Installation

To install md2html, simply:

```bash
$ python3 -m pip install -U git+https://github.com/anbuhckr/md2html.git
```

or from source:

```bash
$ python3 setup.py install
```

## CLI

```bash
$ python3 -m md2html -f input.md -o output.html
```

## Getting Started

```python
#! /usr/bin/env python3

import md2html, requests

md = requests.get('https://raw.githubusercontent.com/anbuhckr/md2html/main/README.md').text
html = md2html.convert(md)
md2html.save(html, 'output.html')
print(html)
```

## Ref

* [python-markdown2](https://github.com/trentm/python-markdown2)
* [minify-html](https://github.com/wilsonzlin/minify-html)
