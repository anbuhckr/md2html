#! /usr/bin/env python3

COPY_HTML = '''
<svg xmlns="http://www.w3.org/2000/svg" width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
    <path d="M9 5h-2a2 2 0 0 0 -2 2v12a2 2 0 0 0 2 2h10a2 2 0 0 0 2 -2v-12a2 2 0 0 0 -2 -2h-2"></path><path d="M9 3m0 2a2 2 0 0 1 2 -2h2a2 2 0 0 1 2 2v0a2 2 0 0 1 -2 2h-2a2 2 0 0 1 -2 -2z"></path>
</svg>
Copy code
'''

CHECK_HTML = '''
<svg xmlns="http://www.w3.org/2000/svg" width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
    <path d="M5 12l5 5l10 -10"></path>
</svg>
Copied!
'''

CODE_HTML = f'''
<div class="codehilite-box">
    <div class="h">
        <span>coding.type</span>
        <div class="hp">
            <span data-state="closed">
                <button class="bt" onclick="codeBoxClicked(this)">
                    {COPY_HTML}
                </button>
            </span>
        </div>
        <div class="codehilite"></div>
    </div>
</div>
'''

JS_HTML = f'''
<script>
    async function codeBoxClicked(e) {{
        await navigator.clipboard.writeText(e.parentNode.parentNode.parentNode.parentNode.querySelector('.codehilite').querySelector('pre').textContent)
        e.innerHTML = `{CHECK_HTML}`
        await new Promise(r => setTimeout(r, 3000))
        e.innerHTML = `{COPY_HTML}`
    }}
</script>
'''

CSS_HTML = '''
<style>
.codehilite-box{border-radius:.375rem;background:#0d0d0d}
.codehilite-box .h{font-size:.75rem;line-height:1rem;color:#cdcdcd;background:#2f2f2f;border-top-left-radius:.375rem;border-top-right-radius:.375rem;padding-bottom:.5rem;padding-top:.5rem;padding-left:1rem;padding-right:1rem;justify-content:space-between;align-items:center;display:flex;position:relative}
.codehilite-box .h .hp{align-items:center;display:flex}
.codehilite-box .h .hp .bt{align-items:center;display:flex;gap:.25rem;cursor:pointer;background:#fff0;appearance:button;-webkit-appearance:button;background-image:none;text-transform:none;font-feature-settings:inherit;color:inherit;font-family:inherit;font-size:100%;font-variation-settings:inherit;font-weight:inherit;letter-spacing:inherit;line-height:inherit;margin:0;padding:0;border:0 solid #e3e3e3;box-sizing:border-box}
.codehilite-box .codehilite .hll{background-color:#f1fa8c}
.codehilite-box .codehilite{background:#0d0d0d;color:#f8f8f2;padding:1rem}
.codehilite-box .codehilite .c{color:#6272a4}
.codehilite-box .codehilite .err{color:#f8f8f2}
.codehilite-box .codehilite .g{color:#f8f8f2}
.codehilite-box .codehilite .k{color:#ff79c6}
.codehilite-box .codehilite .l{color:#f8f8f2}
.codehilite-box .codehilite .n{color:#f8f8f2}
.codehilite-box .codehilite .o{color:#ff79c6}
.codehilite-box .codehilite .x{color:#f8f8f2}
.codehilite-box .codehilite .p{color:#f8f8f2}
.codehilite-box .codehilite .ch{color:#6272a4}
.codehilite-box .codehilite .cm{color:#6272a4}
.codehilite-box .codehilite .cp{color:#ff79c6}
.codehilite-box .codehilite .cpf{color:#6272a4}
.codehilite-box .codehilite .c1{color:#6272a4}
.codehilite-box .codehilite .cs{color:#6272a4}
.codehilite-box .codehilite .gd{color:#8b080b}
.codehilite-box .codehilite .ge{color:#f8f8f2;text-decoration:underline}
.codehilite-box .codehilite .gr{color:#f8f8f2}
.codehilite-box .codehilite .gh{color:#f8f8f2;font-weight:700}
.codehilite-box .codehilite .gi{color:#f8f8f2;font-weight:700}
.codehilite-box .codehilite .go{color:#44475a}
.codehilite-box .codehilite .gp{color:#f8f8f2}
.codehilite-box .codehilite .gs{color:#f8f8f2}
.codehilite-box .codehilite .gu{color:#f8f8f2;font-weight:700}
.codehilite-box .codehilite .gt{color:#f8f8f2}
.codehilite-box .codehilite .kc{color:#ff79c6}
.codehilite-box .codehilite .kd{color:#8be9fd;font-style:italic}
.codehilite-box .codehilite .kn{color:#ff79c6}
.codehilite-box .codehilite .kp{color:#ff79c6}
.codehilite-box .codehilite .kr{color:#ff79c6}
.codehilite-box .codehilite .kt{color:#8be9fd}
.codehilite-box .codehilite .ld{color:#f8f8f2}
.codehilite-box .codehilite .m{color:#bd93f9}
.codehilite-box .codehilite .s{color:#f1fa8c}
.codehilite-box .codehilite .na{color:#50fa7b}
.codehilite-box .codehilite .nb{color:#8be9fd;font-style:italic}
.codehilite-box .codehilite .nc{color:#50fa7b}
.codehilite-box .codehilite .no{color:#f8f8f2}
.codehilite-box .codehilite .nd{color:#f8f8f2}
.codehilite-box .codehilite .ni{color:#f8f8f2}
.codehilite-box .codehilite .ne{color:#f8f8f2}
.codehilite-box .codehilite .nf{color:#50fa7b}
.codehilite-box .codehilite .nl{color:#8be9fd;font-style:italic}
.codehilite-box .codehilite .nn{color:#f8f8f2}
.codehilite-box .codehilite .nx{color:#f8f8f2}
.codehilite-box .codehilite .py{color:#f8f8f2}
.codehilite-box .codehilite .nt{color:#ff79c6}
.codehilite-box .codehilite .nv{color:#8be9fd;font-style:italic}
.codehilite-box .codehilite .ow{color:#ff79c6}
.codehilite-box .codehilite .w{color:#f8f8f2}
.codehilite-box .codehilite .mb{color:#bd93f9}
.codehilite-box .codehilite .mf{color:#bd93f9}
.codehilite-box .codehilite .mh{color:#bd93f9}
.codehilite-box .codehilite .mi{color:#bd93f9}
.codehilite-box .codehilite .mo{color:#bd93f9}
.codehilite-box .codehilite .sa{color:#f1fa8c}
.codehilite-box .codehilite .sb{color:#f1fa8c}
.codehilite-box .codehilite .sc{color:#f1fa8c}
.codehilite-box .codehilite .dl{color:#f1fa8c}
.codehilite-box .codehilite .sd{color:#f1fa8c}
.codehilite-box .codehilite .s2{color:#f1fa8c}
.codehilite-box .codehilite .se{color:#f1fa8c}
.codehilite-box .codehilite .sh{color:#f1fa8c}
.codehilite-box .codehilite .si{color:#f1fa8c}
.codehilite-box .codehilite .sx{color:#f1fa8c}
.codehilite-box .codehilite .sr{color:#f1fa8c}
.codehilite-box .codehilite .s1{color:#f1fa8c}
.codehilite-box .codehilite .ss{color:#f1fa8c}
.codehilite-box .codehilite .bp{color:#f8f8f2;font-style:italic}
.codehilite-box .codehilite .fm{color:#50fa7b}
.codehilite-box .codehilite .vc{color:#8be9fd;font-style:italic}
.codehilite-box .codehilite .vg{color:#8be9fd;font-style:italic}
.codehilite-box .codehilite .vi{color:#8be9fd;font-style:italic}
.codehilite-box .codehilite .vm{color:#8be9fd;font-style:italic}
.codehilite-box .codehilite .il{color:#bd93f9}
</style>
'''
