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
.codehilite-box{border-radius:.375rem!important;background:#0d0d0d!important}
.codehilite-box .h{font-size:.75rem!important;line-height:1rem!important;color:#cdcdcd!important;background:#2f2f2f!important;border-top-left-radius:.375rem!important;border-top-right-radius:.375rem!important;padding-bottom:.5rem!important;padding-top:.5rem!important;padding-left:1rem!important;padding-right:1rem!important;justify-content:space-between!important;align-items:center!important;display:flex!important;position:relative!important}
.codehilite-box .h .hp{align-items:center!important;display:flex!important}
.codehilite-box .h .hp .bt{align-items:center!important;display:flex!important;gap:.25rem!important;cursor:pointer!important;background:#fff0!important;appearance:button!important;-webkit-appearance:button!important;background-image:none!important;text-transform:none!important;font-feature-settings:inherit!important;color:inherit!important;font-family:inherit!important;font-size:100%!important;font-variation-settings:inherit!important;font-weight:inherit!important;letter-spacing:inherit!important;line-height:inherit!important;margin:0!important;padding:0!important;border:0 solid #e3e3e3!important;box-sizing:border-box!important}
.codehilite-box .codehilite .hll{background-color:#f1fa8c!important}
.codehilite-box .codehilite{background:#0d0d0d!important;color:#f8f8f2!important;padding:1rem!important}
.codehilite-box .codehilite pre{background:transparent!important}
.codehilite-box .codehilite .c{color:#6272a4!important}
.codehilite-box .codehilite .err{color:#f8f8f2!important}
.codehilite-box .codehilite .g{color:#f8f8f2!important}
.codehilite-box .codehilite .k{color:#ff79c6!important}
.codehilite-box .codehilite .l{color:#f8f8f2!important}
.codehilite-box .codehilite .n{color:#f8f8f2!important}
.codehilite-box .codehilite .o{color:#ff79c6!important}
.codehilite-box .codehilite .x{color:#f8f8f2!important}
.codehilite-box .codehilite .p{color:#f8f8f2!important}
.codehilite-box .codehilite .ch{color:#6272a4!important}
.codehilite-box .codehilite .cm{color:#6272a4!important}
.codehilite-box .codehilite .cp{color:#ff79c6!important}
.codehilite-box .codehilite .cpf{color:#6272a4!important}
.codehilite-box .codehilite .c1{color:#6272a4!important}
.codehilite-box .codehilite .cs{color:#6272a4!important}
.codehilite-box .codehilite .gd{color:#8b080b!important}
.codehilite-box .codehilite .ge{color:#f8f8f2!important;text-decoration:underline!important}
.codehilite-box .codehilite .gr{color:#f8f8f2!important}
.codehilite-box .codehilite .gh{color:#f8f8f2!important;font-weight:700!important}
.codehilite-box .codehilite .gi{color:#f8f8f2!important;font-weight:700!important}
.codehilite-box .codehilite .go{color:#44475a!important}
.codehilite-box .codehilite .gp{color:#f8f8f2!important}
.codehilite-box .codehilite .gs{color:#f8f8f2!important}
.codehilite-box .codehilite .gu{color:#f8f8f2!important;font-weight:700!important}
.codehilite-box .codehilite .gt{color:#f8f8f2!important}
.codehilite-box .codehilite .kc{color:#ff79c6!important}
.codehilite-box .codehilite .kd{color:#8be9fd!important;font-style:italic!important}
.codehilite-box .codehilite .kn{color:#ff79c6!important}
.codehilite-box .codehilite .kp{color:#ff79c6!important}
.codehilite-box .codehilite .kr{color:#ff79c6!important}
.codehilite-box .codehilite .kt{color:#8be9fd!important}
.codehilite-box .codehilite .ld{color:#f8f8f2!important}
.codehilite-box .codehilite .m{color:#bd93f9!important}
.codehilite-box .codehilite .s{color:#f1fa8c!important}
.codehilite-box .codehilite .na{color:#50fa7b!important}
.codehilite-box .codehilite .nb{color:#8be9fd!important;font-style:italic!important}
.codehilite-box .codehilite .nc{color:#50fa7b!important}
.codehilite-box .codehilite .no{color:#f8f8f2!important}
.codehilite-box .codehilite .nd{color:#f8f8f2!important}
.codehilite-box .codehilite .ni{color:#f8f8f2!important}
.codehilite-box .codehilite .ne{color:#f8f8f2!important}
.codehilite-box .codehilite .nf{color:#50fa7b!important}
.codehilite-box .codehilite .nl{color:#8be9fd!important;font-style:italic!important}
.codehilite-box .codehilite .nn{color:#f8f8f2!important}
.codehilite-box .codehilite .nx{color:#f8f8f2!important}
.codehilite-box .codehilite .py{color:#f8f8f2!important}
.codehilite-box .codehilite .nt{color:#ff79c6!important}
.codehilite-box .codehilite .nv{color:#8be9fd!important;font-style:italic!important}
.codehilite-box .codehilite .ow{color:#ff79c6!important}
.codehilite-box .codehilite .w{color:#f8f8f2!important}
.codehilite-box .codehilite .mb{color:#bd93f9!important}
.codehilite-box .codehilite .mf{color:#bd93f9!important}
.codehilite-box .codehilite .mh{color:#bd93f9!important}
.codehilite-box .codehilite .mi{color:#bd93f9!important}
.codehilite-box .codehilite .mo{color:#bd93f9!important}
.codehilite-box .codehilite .sa{color:#f1fa8c!important}
.codehilite-box .codehilite .sb{color:#f1fa8c!important}
.codehilite-box .codehilite .sc{color:#f1fa8c!important}
.codehilite-box .codehilite .dl{color:#f1fa8c!important}
.codehilite-box .codehilite .sd{color:#f1fa8c!important}
.codehilite-box .codehilite .s2{color:#f1fa8c!important}
.codehilite-box .codehilite .se{color:#f1fa8c!important}
.codehilite-box .codehilite .sh{color:#f1fa8c!important}
.codehilite-box .codehilite .si{color:#f1fa8c!important}
.codehilite-box .codehilite .sx{color:#f1fa8c!important}
.codehilite-box .codehilite .sr{color:#f1fa8c!important}
.codehilite-box .codehilite .s1{color:#f1fa8c!important}
.codehilite-box .codehilite .ss{color:#f1fa8c!important}
.codehilite-box .codehilite .bp{color:#f8f8f2!important;font-style:italic!important}
.codehilite-box .codehilite .fm{color:#50fa7b!important}
.codehilite-box .codehilite .vc{color:#8be9fd!important;font-style:italic!important}
.codehilite-box .codehilite .vg{color:#8be9fd!important;font-style:italic!important}
.codehilite-box .codehilite .vi{color:#8be9fd!important;font-style:italic!important}
.codehilite-box .codehilite .vm{color:#8be9fd!important;font-style:italic!important}
.codehilite-box .codehilite .il{color:#bd93f9!important}
</style>
'''
