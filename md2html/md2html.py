#! /usr/bin/env python3

import markdown2, re, minify_html
from .utils import CODE_HTML, JS_HTML, CSS_HTML
from bs4 import BeautifulSoup

def detect_code_language(text):
    patterns = {
        'python': [
            re.compile(r'\bdef\b'),
            re.compile(r'\bimport\b'),
            re.compile(r'\bprint\b'),
            re.compile(r'\bself\b'),
            re.compile(r'\bclass\s+\w+\s*\(?\w*\)?\s*:\s*\n'),
        ],
        'javascript': [
            re.compile(r'\bfunction\b'),
            re.compile(r'\bvar\b|\bconst\b|\blet\b'),
            re.compile(r'\bconsole\.log\b'),
            re.compile(r'\bclass\s+\w+\s*{'),
        ],
        'c++': [
            re.compile(r'\b#include\b'),
            re.compile(r'\bstd::\b'),
            re.compile(r'\bint main\b'),
            re.compile(r'\bcout\b'),
            re.compile(r'\bclass\s+\w+\s*{'),
        ],
        'php': [
            re.compile(r'<\?php'),
            re.compile(r'\becho\b'),
            re.compile(r'\$[a-zA-Z_]\w*'),
        ],
        'ruby': [
            re.compile(r'\bdef\b'),
            re.compile(r'\bend\b'),
            re.compile(r'\bclass\s+\w+'),
            re.compile(r'\bmodule\b'),
            re.compile(r'\bputs\b'),
        ],
        'java': [
            re.compile(r'\bpublic\b'),
            re.compile(r'\bstatic\b'),
            re.compile(r'\bvoid\b'),
            re.compile(r'\bclass\s+\w+\s*{'),
            re.compile(r'\bSystem\.out\.println\b'),
        ],
        'c#': [
            re.compile(r'\busing\b'),
            re.compile(r'\bnamespace\b'),
            re.compile(r'\bclass\s+\w+\s*{'),
            re.compile(r'\bpublic\b'),
            re.compile(r'\bstatic\b'),
        ],
        'typescript': [
            re.compile(r'\bfunction\b'),
            re.compile(r'\bconst\b|\blet\b|\bvar\b'),
            re.compile(r'\bconsole\.log\b'),
            re.compile(r'\bclass\s+\w+\s*{'),
            re.compile(r'\binterface\b'),
            re.compile(r'\btype\b'),
        ],
    }
    match_counts = {language: sum(bool(pattern.search(text)) for pattern in pattern_list) for language, pattern_list in patterns.items()}
    detected_language = max(match_counts, key=match_counts.get)
    if match_counts[detected_language] == 0:
        return 'bash'
    return detected_language

def load(fn):
    with open(fn, 'r', encoding='utf-8') as f:
        return f.read()

def save(s, fn):
    with open(fn, 'w', encoding='utf-8') as f:
        return f.write(s)

def prettier(s):
    result = ''
    code_block = ''
    code_types = []
    record = False
    for c in s.split('\n'):
        if record:
            code_block += f'{c}\n'
            if c.startswith('```'):
                record = False
                ct = re.findall(r'^```(.*?)\n', code_block)
                if not ct or not ct[0]:
                    ct = [detect_code_language(code_block)]
                    code_block = re.sub(r'^```\n', f'```{ct[0]}\n', code_block)
                result += code_block
                if ct[0] == 'bash':
                    code_types.append('')
                else:
                    code_types.append(ct[0])
                code_block = ''
            continue
        if c.startswith('```'):
            record = True
            code_block += f'{c}\n'
            continue
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
