#! /usr/bin/env python3

import markdown2, re, minify_html
from .utils import CODE_HTML, JS_HTML, CSS_HTML
from bs4 import BeautifulSoup

def load(fn):
    with open(fn, 'r', encoding='utf-8') as f:
        return f.read()

def save(s, fn):
    with open(fn, 'w', encoding='utf-8') as f:
        return f.write(s)

def prettier(s):
    code_types = []
    result = ''
    i = 0
    for c in s.split('\n'):
        if c.startswith('```'):
            i += 1
            if i == 1 and c == '```':
                code_types.append(c.replace('```', ''))
                c = '```bash\n'
            elif i == 1 and c != '```':
                code_types.append(c.replace('```', ''))
                i = 1
            else:
                i = 0
        result += f'{c}\n'
    return result, code_types

def convert(md):
    md, code_types = prettier(md)
    html = markdown2.markdown(md, extras=['fenced-code-blocks'])
    css = BeautifulSoup(CSS_HTML, 'html.parser').style
    js = BeautifulSoup(JS_HTML, 'html.parser').script
    soup = BeautifulSoup(html, 'html.parser')
    code_blocks = soup.find_all('div', class_='codehilite')
    for i, e in enumerate(code_blocks):
        box = CODE_HTML.replace('coding.type', code_types[i])
        new_box = BeautifulSoup(box, 'html.parser').div
        code = new_box.find('div', class_='codehilite')
        for child in e.contents[:]:
            code.append(child.extract())
        new_box.append(code)
        e.replace_with(new_box)
    return minify_html.minify(f'{css}\n{soup}\n{js}', minify_js=True, minify_css=True, remove_processing_instructions=True)
