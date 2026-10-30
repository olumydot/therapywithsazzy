"""Builds the resource-center PDFs, thumbnails and catalog.
Run from the repo root:  python3 tools/make_resources.py [kit ...]
Needs Google Chrome and PyMuPDF. Output: resources/<slug>.pdf, resources/complete-<kit>.pdf,
resources/thumbs/<slug>.jpg and tools/catalog.json (read by the site builder).
"""
import os, sys, json, subprocess, tempfile, importlib
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import pymupdf
from rlib import CSS, KITS

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
OUT = os.path.join(ROOT, 'resources')
THUMBS = os.path.join(OUT, 'thumbs')
CHROME = '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome'
MODULES = {'feelings': 'kids', 'parent': 'parents', 'teen': 'teens', 'adult': 'adults', 'trauma': 'trauma'}


def render(html, pdf):
    with tempfile.NamedTemporaryFile('w', suffix='.html', delete=False) as t:
        t.write(f'<!doctype html><meta charset="utf-8"><style>{CSS}</style><body>{html}{FIT}</body>')
        p = t.name
    subprocess.run([CHROME, '--headless=new', '--disable-gpu', '--no-pdf-header-footer', f'--print-to-pdf={pdf}', 'file://' + p], capture_output=True)
    os.unlink(p)


FIT = '<script>document.querySelectorAll(".page .act").forEach(function(a){var z=1.32;a.style.zoom=z;while(a.scrollHeight>a.clientHeight+3&&z>0.8){z-=0.02;a.style.zoom=z}})</script>'
CHECK = '<script>var o=[];document.querySelectorAll(".page").forEach(function(p,i){var a=p.querySelector(".act");if(a.scrollHeight>a.clientHeight+3)o.push(i)});document.body.insertAdjacentHTML("beforeend","<pre id=rep>OVF:"+o.join(",")+":END</pre>")</script>'


def overflow(html):
    with tempfile.NamedTemporaryFile('w', suffix='.html', delete=False) as t:
        t.write(f'<!doctype html><meta charset="utf-8"><style>{CSS}</style><body>{html}{FIT}{CHECK}</body>')
        p = t.name
    out = subprocess.run([CHROME, '--headless=new', '--disable-gpu', '--virtual-time-budget=3000', '--dump-dom', 'file://' + p], capture_output=True, text=True).stdout
    os.unlink(p)
    seg = out.split('OVF:')[-1].split(':END')[0]
    return [int(x) for x in seg.split(',') if x.strip()]


def main(only):
    os.makedirs(THUMBS, exist_ok=True)
    cat_path = os.path.join(ROOT, 'tools', 'catalog.json')
    catalog = json.load(open(cat_path)) if os.path.exists(cat_path) else {}
    for kit, modname in MODULES.items():
        if only and kit not in only:
            continue
        try:
            mod = importlib.import_module(modname)
        except ModuleNotFoundError:
            continue
        res = mod.RES
        flat = [r['slug'] for r in res for _ in range(r['pages'])]
        bad = overflow(''.join(r['html'] for r in res))
        if bad:
            print('  OVERFLOW on:', ', '.join(sorted(set(flat[i] for i in bad))))
        tmp = os.path.join(tempfile.gettempdir(), f'{kit}-all.pdf')
        render(''.join(r['html'] for r in res), tmp)
        src = pymupdf.open(tmp)
        total = sum(r['pages'] for r in res)
        assert len(src) == total, f'{kit}: expected {total} pages, got {len(src)} (a page overflowed?)'
        i = 0
        entries = []
        for r in res:
            d = pymupdf.open()
            d.insert_pdf(src, from_page=i, to_page=i + r['pages'] - 1)
            d.save(os.path.join(OUT, r['slug'] + '.pdf'), deflate=True)
            pix = src[i].get_pixmap(matrix=pymupdf.Matrix(0.5, 0.5), alpha=False)
            pix.save(os.path.join(THUMBS, r['slug'] + '.jpg'), jpg_quality=80)
            entries.append({k: r[k] for k in ('slug', 'title', 'aud', 'age', 'kind', 'topics', 'teaches', 'start', 'pages', 'group')})
            i += r['pages']
        src.save(os.path.join(OUT, f'complete-{kit}.pdf'), deflate=True)
        catalog[kit] = dict(entries=entries, pages=total, name=KITS[kit]['name'])
        print(kit, len(res), 'resources,', total, 'pages')
    json.dump(catalog, open(cat_path, 'w'), indent=1)


if __name__ == '__main__':
    main(set(sys.argv[1:]))
