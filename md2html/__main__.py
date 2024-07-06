#! /usr/bin/env python3

import md2html
from argparse import ArgumentParser

parser = ArgumentParser()
parser.add_argument('-f', help='input markdown file path',default='input.md', type=str)
parser.add_argument('-o', help='output html file path', default='output.html', type=str)
args = parser.parse_args()

if __name__ == '__main__':
    md = md2html.load(args.f)
    html = md2html.convert(md)
    md2html.save(html, args.o)
