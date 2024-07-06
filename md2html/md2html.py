#! /usr/bin/env python3

import markdown2, re
from .utils import CODE_HTML, JS_HTML, CSS_HTML
from bs4 import BeautifulSoup

def load(fn):
    with open(fn, 'r', encoding='utf-8') as f:
        return f.read()

def save(s, fn):
    with open(fn, 'w', encoding='utf-8') as f:
        return f.write(s)

def convert(md):
    code_types = re.findall(r'```(.*?)(?=\n(?!\n)|\Z)', md)
    for c in code_types:
        if not c:
            md = re.sub(r'```(?=\n(?!\n)|\Z)', '```bash\n', md)
    html = markdown2.markdown(md, extras=['fenced-code-blocks'])
    css = BeautifulSoup(CSS_HTML, 'html.parser').style
    js = BeautifulSoup(JS_HTML, 'html.parser').script
    soup = BeautifulSoup(html, 'html.parser')
    code_blocks = soup.find_all('div', class_='codehilite')
    if len(code_types) != len(code_blocks):
        raise SystemExit('[!] Error: md2html can not find code blocks.')
    for i, e in enumerate(code_blocks):
        box = CODE_HTML.replace('coding.type', code_types[i])
        new_box = BeautifulSoup(box, 'html.parser').div
        code = new_box.find('div', class_='codehilite')
        for child in e.contents[:]:
            code.append(child.extract())
        new_box.append(code)
        e.replace_with(new_box)
    return f'{css}\n{soup}\n{js}'
