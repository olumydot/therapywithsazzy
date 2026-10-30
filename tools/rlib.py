"""Shared page template, helpers and illustrations for the resource-center PDFs."""
import os

HERE = os.path.dirname(os.path.abspath(__file__))
FONT = 'file://' + os.path.join(HERE, 'Fraunces.ttf')

KITS = {
    'feelings': dict(name='The Feelings Toolkit', who='Children', label='Children · ages 4–12', a='#E8806A', s='#fde9e3', d='#a8432d'),
    'parent':   dict(name='The Parent Toolkit', who='Parents', label='Parents & caregivers', a='#E0A93B', s='#fbf0d4', d='#7d5a0c'),
    'teen':     dict(name='The Teen Toolkit', who='Teens', label='Teens · ages 12–18', a='#2E9C95', s='#dff1ee', d='#17625d'),
    'adult':    dict(name='The Adult Wellness Toolkit', who='Adults', label='Adults', a='#4F6FB5', s='#e4eaf6', d='#223e7a'),
    'trauma':   dict(name='Trauma & Healing Resource Center', who='Trauma & Healing', label='Trauma & healing education', a='#7B6AAE', s='#ebe7f5', d='#4a3d80'),
}

MARK = '<svg viewBox="0 0 64 64"><path d="M50.6 29.6 A21 21 0 1 1 35.6 13.5" fill="none" stroke="#0F2A4A" stroke-width="5.2" stroke-linecap="round"/><path d="M30 49 C30 39 34 31 43 23 C48 18.5 52 14.5 55 9" fill="none" stroke="#2E9C95" stroke-width="4.2" stroke-linecap="round"/><path d="M31.2 40.5 C24 40.5 19.5 36 19.5 29.5 C26.5 29.5 31.2 33.5 31.2 40.5Z" fill="#6CC4BC"/><path d="M36.5 31.5 C43 33 47.5 31 49.5 25.5 C43.5 23.5 38.5 25.5 36.5 31.5Z" fill="#6CC4BC"/><circle cx="56.5" cy="7.5" r="4.3" fill="#E8806A"/></svg>'

CSS = '''
@font-face{font-family:Fr;src:url(FONTURL);font-weight:100 900}
@page{size:Letter;margin:0}
*{box-sizing:border-box;-webkit-print-color-adjust:exact;print-color-adjust:exact}
body{margin:0;font:11.5pt/1.45 -apple-system,"Helvetica Neue",Arial,sans-serif;color:#16243a}
.page{width:8.5in;height:11in;position:relative;page-break-after:always;overflow:hidden;background:#fff;display:flex;flex-direction:column}
.page:last-child{page-break-after:auto}
.top{display:flex;align-items:center;gap:9px;padding:.28in .55in 0}
.top svg{width:28px;height:28px}.top b{font:600 11.5pt Fr,Georgia,serif;color:#0F2A4A}
.top span{margin-left:auto;font-size:7.8pt;letter-spacing:.14em;text-transform:uppercase;font-weight:700;color:var(--d)}
.band{margin:.14in .55in 0;border-radius:22px;background:var(--s);display:flex;align-items:center;gap:16px;padding:.22in .3in;position:relative;overflow:hidden}
.band::after{content:"";position:absolute;right:-50px;top:-60px;width:210px;height:210px;border-radius:50%;background:var(--a);opacity:.16}
.band h1{font:600 26pt/1.08 Fr,Georgia,serif;color:#0F2A4A;margin:6px 0 0;position:relative;z-index:1}
.band .bt{flex:1;position:relative;z-index:1}
.band .ill{width:1.25in;height:1.25in;flex:none;position:relative;z-index:1}
.badges{display:flex;gap:6px;flex-wrap:wrap}
.b{font-size:7.8pt;font-weight:700;letter-spacing:.1em;text-transform:uppercase;padding:3px 10px;border-radius:99px;background:#fff;color:var(--d);border:1.4px solid var(--a)}
.b.k{background:var(--a);color:#fff}
.info{display:grid;grid-template-columns:1.25fr 1fr;gap:.2in;margin:.16in .55in 0}
.info h4{font:700 8.5pt Arial,sans-serif;letter-spacing:.14em;text-transform:uppercase;color:var(--d);margin:0 0 3px}
.info p{margin:0 0 7px;font-size:10.5pt;line-height:1.4}
.info ol{margin:0;padding:0;list-style:none;counter-reset:n}
.info li{counter-increment:n;position:relative;padding-left:26px;margin-bottom:5px;font-size:10.5pt;line-height:1.35}
.info li::before{content:counter(n);position:absolute;left:0;top:0;width:19px;height:19px;border-radius:50%;background:var(--a);color:#fff;font:700 8.5pt/19px Arial;text-align:center}
.eg{background:#fff;border:1.6px dashed var(--a);border-radius:16px;padding:10px 14px;position:relative}
.eg p{font-style:italic}
.act{flex:1;margin:.14in .55in 0;min-height:0;position:relative}
.foot{margin:0 .55in .26in;padding-top:6px;border-top:1px solid #e3e8ef;font-size:7.2pt;color:#6b7a8e;display:flex;justify-content:space-between;gap:20px;line-height:1.35}
h2{font:600 14pt Fr,Georgia,serif;color:#0F2A4A;margin:10px 0 5px}
h3{font:600 12pt Fr,Georgia,serif;color:#0F2A4A;margin:0 0 3px}
.line{border-bottom:1.3px solid #9fb0c4;height:24px}
.lab{font-weight:700;color:#0F2A4A;font-size:10.5pt}
.small{font-size:9pt;color:#56657a}
.box{border:1.5px solid #c3cfdd;border-radius:14px;padding:9px 12px}
.sb{background:var(--s);border-color:transparent}.wb{background:#fff;border:1.5px solid var(--a)}
.tint{background:#fbf6ee;border-color:#eadfca}.teal{background:#e6f4f1;border-color:#bfe0da}.coral{background:#fdeee9;border-color:#f3cfc4}.sand{background:#f7f0e2;border-color:#e8dcc4}.blue{background:#e4eaf6;border-color:#c4d0ea}.lilac{background:#ebe7f5;border-color:#d3cbea}
.grid{display:grid;gap:10px}.g2{grid-template-columns:1fr 1fr}.g3{grid-template-columns:repeat(3,1fr)}.g4{grid-template-columns:repeat(4,1fr)}.g5{grid-template-columns:repeat(5,1fr)}.g7{grid-template-columns:repeat(7,1fr)}
.cb{display:inline-block;width:12px;height:12px;border:1.6px solid #0F2A4A;border-radius:3px;margin-right:7px;vertical-align:-2px;flex:none}
ul.cbs{list-style:none;margin:0;padding:0}ul.cbs li{margin:3px 0;display:flex;font-size:10.5pt;line-height:1.3}
ul.bl{margin:3px 0 0;padding-left:17px;font-size:10.5pt}ul.bl li{margin-bottom:2px}
table{width:100%;border-collapse:collapse}
th{background:var(--d);color:#fff;font-size:8.5pt;text-align:left;padding:6px 7px;font-weight:600}
td{border:1.3px solid #b9c6d6;vertical-align:top;padding:4px 6px;font-size:10pt}
.num{display:inline-grid;place-items:center;width:22px;height:22px;border-radius:50%;background:var(--a);color:#fff;font-weight:700;font-size:10pt;margin-right:7px;flex:none}
.face{text-align:center;border:1.5px solid #e1e7ef;border-radius:14px;padding:6px 4px 5px;background:#fff}
.face svg{width:54px;height:54px}.face b{display:block;font-size:11pt;color:#0F2A4A}
.center{text-align:center}.row{display:flex;gap:10px;align-items:center}
.pill{display:inline-block;padding:4px 12px;border-radius:99px;border:1.5px solid var(--a);font-size:10pt;margin:2px;background:#fff}
.stick{display:inline-block;background:var(--a);color:#fff;font-weight:700;font-size:8pt;letter-spacing:.1em;text-transform:uppercase;padding:2px 9px;border-radius:99px}
.say{background:var(--s);border-radius:14px;padding:9px 13px;font-size:10.5pt;position:relative}
.say b{color:var(--d)}
.warn{background:#fdeee9;border:1.5px solid #f3cfc4;border-radius:14px;padding:9px 13px;font-size:10pt}
.cut{border:1.6px dashed var(--a);border-radius:14px;padding:10px 12px}
'''.replace('FONTURL', FONT)

DISC = 'Educational self-help resource from Therapy with Sazzy, an initiative of Beyond Boundaries Consulting, LLC. It is not a diagnosis or a substitute for individualized professional care. In a crisis call or text 988, or call 911.'


def wrap(kit, inner):
    k = KITS[kit]
    return f'<section class="page" style="--a:{k["a"]};--s:{k["s"]};--d:{k["d"]}">' + inner + '</section>'


def topbar(kit):
    return f'<div class="top">{MARK}<b>Therapy with Sazzy</b><span>{KITS[kit]["name"]}</span></div>'


def foot():
    return f'<div class="foot"><span>{DISC}</span><span>therapywithsazzy.com</span></div>'


def res(kit, title, age, kind, ill, what, how, ex, body, z=1.14):
    steps = ''.join(f'<li>{h}</li>' for h in how)
    return wrap(kit, topbar(kit) +
        f'<div class="band"><div class="bt"><div class="badges"><span class="b k">{age}</span><span class="b">{kind}</span></div><h1>{title}</h1></div><div class="ill">{ill}</div></div>'
        f'<div class="info"><div><h4>What this is</h4><p>{what}</p><h4>How to use it</h4><ol>{steps}</ol></div><div class="eg"><h4>Example</h4><p>{ex}</p></div></div>'
        f'<div class="act" style="zoom:{z}">{body}</div>' + foot())


def cont(kit, title, body, sub='', z=1.1):
    return wrap(kit, topbar(kit) +
        f'<div class="band" style="padding:.14in .3in"><div class="bt"><div class="badges"><span class="b">{sub or "continued"}</span></div><h1 style="font-size:20pt">{title}</h1></div></div>'
        f'<div class="act" style="zoom:{z}">{body}</div>' + foot())


# ---------------------------------------------------------------- small html helpers
def lines(n, h=24): return ''.join(f'<div class="line" style="height:{h}px"></div>' for _ in range(n))
def cbs(items): return '<ul class="cbs">' + ''.join(f'<li><i class="cb"></i><span>{i}</span></li>' for i in items) + '</ul>'
def bl(items): return '<ul class="bl">' + ''.join(f'<li>{i}</li>' for i in items) + '</ul>'
def field(label, n=1, h=24): return f'<div style="margin-bottom:6px"><div class="lab">{label}</div>{lines(n, h)}</div>'
def box(inner, cls='', style=''): return f'<div class="box {cls}" style="{style}">{inner}</div>'
def grid(cols, items, gap=10, style=''): return f'<div class="grid g{cols}" style="gap:{gap}px;{style}">' + ''.join(items) + '</div>'
def tbl(heads, rows, h=40): return '<table><tr>' + ''.join(f'<th>{x}</th>' for x in heads) + '</tr>' + ''.join('<tr>' + ''.join(f'<td style="height:{h}px">{c}</td>' for c in r) + '</tr>' for r in rows) + '</table>'
def say(t): return f'<div class="say">{t}</div>'
def warn(t): return f'<div class="warn">{t}</div>'
def circles(n, size=30): return '<div class="row" style="justify-content:space-between">' + ''.join(f'<span style="width:{size}px;height:{size}px;border-radius:50%;border:1.7px solid #0F2A4A;display:grid;place-items:center;font-size:10pt">{i}</span>' for i in range(1, n + 1)) + '</div>'
def pills(items): return ''.join(f'<span class="pill">{i}</span>' for i in items)


# ---------------------------------------------------------------- illustrations
def svg(vb, inner, w=None):
    return f'<svg viewBox="{vb}" xmlns="http://www.w3.org/2000/svg" style="width:100%;height:100%">{inner}</svg>'

INK = '#16243a'

def face(bg, feat, size=None):
    return f'<svg viewBox="0 0 64 64"><circle cx="32" cy="32" r="29" fill="{bg}"/><g fill="{INK}" stroke="{INK}" stroke-width="3" stroke-linecap="round" stroke-linejoin="round">{feat}</g></svg>'

E2 = '<circle cx="23" cy="28" r="3" stroke="none"/><circle cx="41" cy="28" r="3" stroke="none"/>'
FACE_DEF = {
    'Happy': ('#fbe3a8', E2 + '<path d="M22 39c4 8 16 8 20 0" fill="none"/>'),
    'Calm': ('#cdeae5', '<path d="M18 29q5 4 10 0M36 29q5 4 10 0" fill="none"/><path d="M24 41c4 4 12 4 16 0" fill="none"/>'),
    'Excited': ('#fbe3a8', E2 + '<path d="M20 38c3 9 21 9 24 0z" stroke-width="2"/>'),
    'Proud': ('#f7d9a8', '<path d="M18 29q5-4 10 0M36 29q5-4 10 0" fill="none"/><path d="M21 38c5 8 17 8 22 0" fill="none"/>'),
    'Worried': ('#cfe0f5', E2 + '<path d="M17 25l9-4M47 25l-9-4" fill="none"/><path d="M24 44c3-3 13-3 16 0" fill="none"/>'),
    'Scared': ('#d8d4ee', '<circle cx="23" cy="28" r="4.5" fill="#fff" stroke-width="2"/><circle cx="41" cy="28" r="4.5" fill="#fff" stroke-width="2"/><circle cx="23" cy="28" r="1.6" stroke="none"/><circle cx="41" cy="28" r="1.6" stroke="none"/><ellipse cx="32" cy="44" rx="5" ry="6" stroke-width="2"/>'),
    'Sad': ('#d9e0ee', E2 + '<path d="M24 46c3-4 13-4 16 0" fill="none"/><path d="M42 36q2 4 0 6" stroke="#5b8fd6" stroke-width="2.6" fill="none"/>'),
    'Lonely': ('#dfe3ea', E2 + '<path d="M20 47c4-3 20-3 24 0" fill="none"/>'),
    'Frustrated': ('#fbd0c6', E2 + '<path d="M16 22l10 5M48 22l-10 5" fill="none"/><path d="M24 45h16" fill="none"/>'),
    'Angry': ('#f7b8a8', E2 + '<path d="M15 21l12 7M49 21l-12 7" fill="none" stroke-width="3.6"/><path d="M22 46q10-8 20 0" fill="none"/>'),
    'Confused': ('#e9dff5', '<circle cx="23" cy="29" r="3" stroke="none"/><circle cx="41" cy="29" r="3" stroke="none"/><path d="M17 24l9-2M38 20l9 3" fill="none"/><path d="M24 44q4-3 8 0t8 0" fill="none" stroke-width="2.6"/>'),
    'Tired': ('#e3e0ea', '<path d="M18 29h10M36 29h10" fill="none"/><ellipse cx="32" cy="43" rx="4.5" ry="3.5" stroke-width="2"/>'),
    'Embarrassed': ('#f9d6d6', E2 + '<circle cx="16" cy="37" r="4" fill="#f08f8f" stroke="none" opacity=".7"/><circle cx="48" cy="37" r="4" fill="#f08f8f" stroke="none" opacity=".7"/><path d="M24 44q4 3 8 0t8 0" fill="none" stroke-width="2.4"/>'),
    'Blank': ('#fff', E2 + ''),
}
def F(name, label=None, extra=''):
    bg, ft = FACE_DEF[name]
    return f'<div class="face">{face(bg, ft)}<b>{label or name}</b>{extra}</div>'
def Fsvg(name): return face(*FACE_DEF[name])

def blank_face(): return face('#fff', '<circle cx="32" cy="32" r="29" fill="none" stroke="#9fb0c4" stroke-width="2" stroke-dasharray="4 4"/>')

def body_outline(w='1.6in', dots=False):
    return f'''<svg viewBox="0 0 200 330" style="width:{w};height:auto"><g fill="#fff" stroke="#16243a" stroke-width="3" stroke-linejoin="round" stroke-linecap="round">
<circle cx="100" cy="42" r="30"/><path d="M92 70h16v14H92z"/><path d="M60 92q40-14 80 0l14 90-18 4-8-60v80l6 100h-26l-8-80-8 80H62l6-100v-80l-8 60-18-4z"/></g></svg>'''

def hand(w='2in'):
    fingers = [(38, 122, -38, 'thumb'), (62, 92, -14, ''), (92, 82, 0, ''), (122, 92, 14, ''), (148, 112, 28, '')]
    s = '<svg viewBox="0 0 190 230" style="width:%s;height:auto"><g fill="#fde9e3" stroke="#16243a" stroke-width="3" stroke-linejoin="round" stroke-linecap="round">' % w
    s += '<path d="M44 130 Q40 210 95 214 Q150 210 152 150 L150 118 L44 118Z"/>'
    for i, (x, y, r, _) in enumerate(fingers):
        s += f'<rect x="{x-11}" y="{y-70}" width="22" height="{74 if i else 62}" rx="11" transform="rotate({r} {x} {y})"/>'
    s += '</g>'
    for i, (x, y, r, _) in enumerate(fingers):
        s += f'<circle cx="{x}" cy="{y+26}" r="10" fill="#E8806A"/><text x="{x}" y="{y+30}" text-anchor="middle" font-family="Arial" font-weight="700" font-size="12" fill="#fff">{i+1}</text>'
    return s + '</svg>'

def monster(w='1.6in', eyes=3, color='#9aa9e0'):
    es = ''.join(f'<circle cx="{70 + i*(60/(max(eyes-1,1)))}" cy="82" r="13" fill="#fff" stroke="{INK}" stroke-width="3"/><circle cx="{70 + i*(60/(max(eyes-1,1)))+2}" cy="84" r="5" fill="{INK}"/>' for i in range(eyes))
    return f'''<svg viewBox="0 0 200 210" style="width:{w};height:auto"><path d="M100 18c48 0 80 38 80 92 0 40-18 78-80 78S20 150 20 110C20 56 52 18 100 18z" fill="{color}" stroke="{INK}" stroke-width="3.5"/>
<path d="M58 28l-12-22 26 14M142 28l12-22-26 14" fill="{color}" stroke="{INK}" stroke-width="3.5" stroke-linejoin="round"/>{es}
<path d="M62 132q38 30 76 0" fill="#fff" stroke="{INK}" stroke-width="3.5" stroke-linecap="round"/><path d="M74 138v10M92 142v10M110 142v10M126 138v10" stroke="{INK}" stroke-width="3"/>
<path d="M40 190l-8 16M70 192l-4 16M130 192l4 16M160 190l8 16" stroke="{INK}" stroke-width="3.5" stroke-linecap="round"/></svg>'''

def thermometer(w='1.1in', levels=5):
    cols = ['#8fd3c8', '#bfe3a0', '#f5d58a', '#f2a96b', '#e8806a', '#d9604a', '#b84a3a'][:levels] if levels <= 7 else None
    cols = ['#8fd3c8', '#c3e29c', '#f5d58a', '#f2a96b', '#e8806a'][:levels]
    segs = ''
    h = 220 / levels
    for i, c in enumerate(cols):
        y = 250 - (i + 1) * h
        segs += f'<rect x="38" y="{y:.1f}" width="44" height="{h:.1f}" fill="{c}"/>'
    return f'<svg viewBox="0 0 120 310" style="width:{w};height:auto"><defs><clipPath id="t"><path d="M38 40a22 22 0 0 1 44 0v178a40 40 0 1 1-44 0z"/></clipPath></defs><g clip-path="url(#t)">{segs}<circle cx="60" cy="262" r="38" fill="#d9604a"/></g><path d="M38 40a22 22 0 0 1 44 0v178a40 40 0 1 1-44 0z" fill="none" stroke="{INK}" stroke-width="4"/></svg>'

def hero_badge(w='1.3in', color='#E8806A'):
    return f'<svg viewBox="0 0 160 170" style="width:{w};height:auto"><path d="M30 40l-22 30 26 6zM130 40l22 30-26 6z" fill="#4F6FB5" stroke="{INK}" stroke-width="3" stroke-linejoin="round"/><path d="M80 8l56 18v50c0 40-26 68-56 84C50 144 24 116 24 76V26z" fill="{color}" stroke="{INK}" stroke-width="3.5" stroke-linejoin="round"/><path d="M80 44l10 22 24 2-18 16 6 24-22-13-22 13 6-24-18-16 24-2z" fill="#fbe3a8" stroke="{INK}" stroke-width="3" stroke-linejoin="round"/></svg>'

def circles_control(w='2.4in'):
    return f'<svg viewBox="0 0 240 240" style="width:{w};height:auto"><circle cx="120" cy="120" r="112" fill="#f3efe6" stroke="{INK}" stroke-width="3" stroke-dasharray="6 6"/><circle cx="120" cy="120" r="76" fill="#dff1ee" stroke="{INK}" stroke-width="3"/><circle cx="120" cy="120" r="38" fill="#fbe3a8" stroke="{INK}" stroke-width="3"/><text x="120" y="118" text-anchor="middle" font-family="Arial" font-weight="700" font-size="12" fill="{INK}">I CAN</text><text x="120" y="132" text-anchor="middle" font-family="Arial" font-weight="700" font-size="12" fill="{INK}">CONTROL</text><text x="120" y="78" text-anchor="middle" font-family="Arial" font-weight="700" font-size="11" fill="{INK}">I CAN INFLUENCE</text><text x="120" y="26" text-anchor="middle" font-family="Arial" font-weight="700" font-size="11" fill="{INK}">OUT OF MY CONTROL</text></svg>'

def window_chart(w='100%'):
    return f'''<svg viewBox="0 0 560 250" style="width:{w};height:auto"><rect x="0" y="0" width="560" height="78" fill="#fdeee9"/><rect x="0" y="78" width="560" height="94" fill="#dff1ee"/><rect x="0" y="172" width="560" height="78" fill="#e3e0ea"/>
<path d="M10 150 C60 70 90 40 130 60 S170 160 220 126 S270 96 310 120 S360 190 400 130 S450 50 480 46 S530 90 548 110" fill="none" stroke="{INK}" stroke-width="4" stroke-linecap="round"/>
<g font-family="Arial" font-weight="700" font-size="13" fill="{INK}"><text x="12" y="22">TOO MUCH: hyper-arousal</text><text x="12" y="38" font-weight="400" font-size="11">fight / flight, panic, anger, racing thoughts</text><text x="12" y="104" fill="#17625d">THE WINDOW OF TOLERANCE</text><text x="12" y="120" font-weight="400" font-size="11">calm, present, able to think and feel at the same time</text><text x="12" y="198">TOO LITTLE: hypo-arousal</text><text x="12" y="214" font-weight="400" font-size="11">freeze, numb, shut down, spaced out, exhausted</text></g></svg>'''

def zone_ill(w='1.2in'):
    return f'<svg viewBox="0 0 120 120" style="width:{w};height:auto"><rect x="6" y="10" width="108" height="30" rx="8" fill="#f3cfc4"/><rect x="6" y="45" width="108" height="30" rx="8" fill="#bfe0da"/><rect x="6" y="80" width="108" height="30" rx="8" fill="#d6d1e4"/><path d="M12 62c20-30 30 20 48 0s32 20 48-4" fill="none" stroke="{INK}" stroke-width="3.5" stroke-linecap="round"/></svg>'

def toolbox(w='1.5in'):
    return f'<svg viewBox="0 0 180 150" style="width:{w};height:auto"><path d="M62 42v-14h56v14" fill="none" stroke="{INK}" stroke-width="5" stroke-linecap="round"/><rect x="14" y="42" width="152" height="94" rx="14" fill="#E8806A" stroke="{INK}" stroke-width="4"/><path d="M14 80h152" stroke="{INK}" stroke-width="4"/><rect x="76" y="70" width="28" height="22" rx="5" fill="#fbe3a8" stroke="{INK}" stroke-width="3.5"/></svg>'

def heart_hands(w='1.2in'):
    return f'<svg viewBox="0 0 120 110" style="width:{w};height:auto"><path d="M60 98S10 66 10 36a24 24 0 0 1 50-6 24 24 0 0 1 50 6c0 30-50 62-50 62z" fill="#E8806A" stroke="{INK}" stroke-width="4" stroke-linejoin="round"/></svg>'

def sun_ill(w='1.2in', c='#E0A93B'):
    rays = ''.join(f'<path d="M60 8v14" stroke="{INK}" stroke-width="4" stroke-linecap="round" transform="rotate({i*45} 60 60)"/>' for i in range(8))
    return f'<svg viewBox="0 0 120 120" style="width:{w};height:auto">{rays}<circle cx="60" cy="60" r="28" fill="{c}" stroke="{INK}" stroke-width="4"/></svg>'

def plant_ill(w='1.2in', c='#2E9C95'):
    return f'<svg viewBox="0 0 120 130" style="width:{w};height:auto"><path d="M60 122V62" stroke="{INK}" stroke-width="5" stroke-linecap="round"/><path d="M60 80C30 80 18 62 18 42c28 0 42 14 42 38z" fill="{c}" stroke="{INK}" stroke-width="4" stroke-linejoin="round"/><path d="M60 62C60 34 76 18 102 16c0 28-16 46-42 46z" fill="#6CC4BC" stroke="{INK}" stroke-width="4" stroke-linejoin="round"/><path d="M34 122h52" stroke="{INK}" stroke-width="5" stroke-linecap="round"/></svg>'

def chat_ill(w='1.2in', c='#2E9C95'):
    return f'<svg viewBox="0 0 120 110" style="width:{w};height:auto"><path d="M14 14h66a8 8 0 0 1 8 8v36a8 8 0 0 1-8 8H48L28 84V66H14a8 8 0 0 1-8-8V22a8 8 0 0 1 8-8z" fill="{c}" stroke="{INK}" stroke-width="4" stroke-linejoin="round"/><path d="M60 48h46a8 8 0 0 1 8 8v28a8 8 0 0 1-8 8h-6v16L82 92H60a8 8 0 0 1-8-8V56a8 8 0 0 1 8-8z" fill="#fbe3a8" stroke="{INK}" stroke-width="4" stroke-linejoin="round" transform="translate(-4 0)"/></svg>'

def journal_ill(w='1.2in', c='#2E9C95'):
    return f'<svg viewBox="0 0 120 130" style="width:{w};height:auto"><rect x="22" y="8" width="82" height="112" rx="10" fill="{c}" stroke="{INK}" stroke-width="4"/><path d="M38 8v112" stroke="{INK}" stroke-width="4"/><path d="M52 40h38M52 56h38M52 72h24" stroke="#fff" stroke-width="4" stroke-linecap="round"/><path d="M92 92l-14 22 20-4z" fill="#fbe3a8" stroke="{INK}" stroke-width="3" stroke-linejoin="round"/></svg>'

def shield_ill(w='1.2in', c='#7B6AAE'):
    return f'<svg viewBox="0 0 120 130" style="width:{w};height:auto"><path d="M60 8l46 16v38c0 32-20 52-46 62C34 114 14 94 14 62V24z" fill="{c}" stroke="{INK}" stroke-width="4" stroke-linejoin="round"/><path d="M40 62l14 14 28-30" fill="none" stroke="#fff" stroke-width="7" stroke-linecap="round" stroke-linejoin="round"/></svg>'

def brain_ill(w='1.2in', c='#4F6FB5'):
    return f'<svg viewBox="0 0 120 110" style="width:{w};height:auto"><path d="M60 14c-10-8-28-4-30 12-12 2-18 16-10 28-6 12 2 28 16 28 4 12 22 14 24 2 2 12 20 10 24-2 14 0 22-16 16-28 8-12 2-26-10-28-2-16-20-20-30-12z" fill="{c}" stroke="{INK}" stroke-width="4" stroke-linejoin="round"/><path d="M60 16v78M44 40c8 0 12 6 16 6M76 40c-8 0-12 6-16 6M44 70c8 0 12-6 16-6M76 70c-8 0-12-6-16-6" fill="none" stroke="#fff" stroke-width="3.5" stroke-linecap="round"/></svg>'

def people_ill(w='1.3in', c='#E0A93B'):
    return f'<svg viewBox="0 0 150 110" style="width:{w};height:auto"><circle cx="48" cy="34" r="20" fill="{c}" stroke="{INK}" stroke-width="4"/><path d="M12 100c0-26 16-40 36-40s36 14 36 40z" fill="{c}" stroke="{INK}" stroke-width="4" stroke-linejoin="round"/><circle cx="108" cy="52" r="14" fill="#6CC4BC" stroke="{INK}" stroke-width="4"/><path d="M84 102c0-18 10-30 24-30s24 12 24 30z" fill="#6CC4BC" stroke="{INK}" stroke-width="4" stroke-linejoin="round"/></svg>'

def clock_ill(w='1.2in', c='#E0A93B'):
    return f'<svg viewBox="0 0 120 120" style="width:{w};height:auto"><circle cx="60" cy="60" r="48" fill="#fff" stroke="{INK}" stroke-width="5"/><circle cx="60" cy="60" r="48" fill="{c}" opacity=".25"/><path d="M60 30v32l22 12" fill="none" stroke="{INK}" stroke-width="6" stroke-linecap="round" stroke-linejoin="round"/></svg>'

def lungs_ill(w='1.2in', c='#2E9C95'):
    return f'<svg viewBox="0 0 120 120" style="width:{w};height:auto"><path d="M56 10v46M56 56c-8 6-14 10-14 10M64 56c8 6 14 10 14 10" fill="none" stroke="{INK}" stroke-width="5" stroke-linecap="round"/><path d="M48 44C20 46 8 88 14 104c6 8 24 4 34-10z" fill="{c}" stroke="{INK}" stroke-width="4" stroke-linejoin="round"/><path d="M72 44c28 2 40 44 34 60-6 8-24 4-34-10z" fill="{c}" stroke="{INK}" stroke-width="4" stroke-linejoin="round"/></svg>'

def anchor_ill(w='1.2in', c='#7B6AAE'):
    return f'<svg viewBox="0 0 120 130" style="width:{w};height:auto"><circle cx="60" cy="22" r="12" fill="none" stroke="{INK}" stroke-width="6"/><path d="M60 34v78M38 56h44M20 84c0 22 18 32 40 32s40-10 40-32M20 84l-8 10M100 84l8 10" fill="none" stroke="{INK}" stroke-width="6" stroke-linecap="round" stroke-linejoin="round"/><path d="M60 34v78" stroke="{c}" stroke-width="2"/></svg>'

def map_ill(w='1.2in', c='#4F6FB5'):
    return f'<svg viewBox="0 0 120 120" style="width:{w};height:auto"><circle cx="60" cy="60" r="50" fill="#fff" stroke="{INK}" stroke-width="5"/><path d="M80 40L68 70 40 80l12-30z" fill="{c}" stroke="{INK}" stroke-width="4" stroke-linejoin="round"/><circle cx="60" cy="60" r="4" fill="#fff"/></svg>'

def puzzle_ill(w='1.2in', c='#7B6AAE'):
    return f'<svg viewBox="0 0 120 120" style="width:{w};height:auto"><path d="M16 30h30a10 10 0 1 1 20 0h30v30a10 10 0 1 0 0 20v30H66a10 10 0 1 0-20 0H16V80a10 10 0 1 1 0-20z" fill="{c}" stroke="{INK}" stroke-width="4" stroke-linejoin="round" transform="scale(.9) translate(6 -6)"/></svg>'

def pencil_ill(w='1.2in', c='#E8806A'):
    return f'<svg viewBox="0 0 120 120" style="width:{w};height:auto"><path d="M24 96l8-26 44-44 18 18-44 44z" fill="{c}" stroke="{INK}" stroke-width="4" stroke-linejoin="round"/><path d="M24 96l8-26 18 18z" fill="#fbe3a8" stroke="{INK}" stroke-width="4" stroke-linejoin="round"/><path d="M76 26l18 18" stroke="{INK}" stroke-width="4"/></svg>'

def star_ill(w='1.2in', c='#E0A93B'):
    return f'<svg viewBox="0 0 120 120" style="width:{w};height:auto"><path d="M60 8l16 34 38 4-28 26 8 38-34-20-34 20 8-38L6 46l38-4z" fill="{c}" stroke="{INK}" stroke-width="4" stroke-linejoin="round"/></svg>'

def stop_ill(w='1.2in'):
    return f'<svg viewBox="0 0 120 120" style="width:{w};height:auto"><path d="M38 8h44l30 30v44l-30 30H38L8 82V38z" fill="#E8806A" stroke="{INK}" stroke-width="4" stroke-linejoin="round"/><text x="60" y="68" text-anchor="middle" font-family="Arial" font-weight="800" font-size="28" fill="#fff">STOP</text></svg>'

def magnifier_ill(w='1.2in', c='#E8806A'):
    return f'<svg viewBox="0 0 120 120" style="width:{w};height:auto"><circle cx="50" cy="50" r="34" fill="#fff" stroke="{INK}" stroke-width="6"/><circle cx="50" cy="50" r="34" fill="{c}" opacity=".25"/><path d="M76 76l30 30" stroke="{INK}" stroke-width="10" stroke-linecap="round"/></svg>'

def bubbles_ill(w='1.2in'):
    return f'<svg viewBox="0 0 120 120" style="width:{w};height:auto"><circle cx="40" cy="74" r="30" fill="#bfe0da" stroke="{INK}" stroke-width="4"/><circle cx="84" cy="40" r="22" fill="#fbe3a8" stroke="{INK}" stroke-width="4"/><circle cx="90" cy="92" r="14" fill="#fde9e3" stroke="{INK}" stroke-width="4"/></svg>'

def bridge_ill(w='1.2in', c='#4F6FB5'):
    return f'<svg viewBox="0 0 140 100" style="width:{w};height:auto"><path d="M6 70h128" stroke="{INK}" stroke-width="6" stroke-linecap="round"/><path d="M18 70C30 20 110 20 122 70" fill="none" stroke="{c}" stroke-width="6"/><path d="M40 70V38M60 70V28M80 70V28M100 70V38" stroke="{INK}" stroke-width="4"/><path d="M6 90h128" stroke="#6CC4BC" stroke-width="5" stroke-linecap="round"/></svg>'

def battery_ill(w='1.2in', c='#4F6FB5'):
    return f'<svg viewBox="0 0 140 90" style="width:{w};height:auto"><rect x="6" y="14" width="114" height="62" rx="12" fill="#fff" stroke="{INK}" stroke-width="5"/><rect x="120" y="32" width="14" height="26" rx="4" fill="{INK}"/><rect x="14" y="22" width="30" height="46" rx="6" fill="#E8806A"/></svg>'

def flag_ill(w='1.2in', c='#E8806A'):
    return f'<svg viewBox="0 0 120 120" style="width:{w};height:auto"><path d="M26 112V12" stroke="{INK}" stroke-width="6" stroke-linecap="round"/><path d="M26 16h72l-16 24 16 24H26z" fill="{c}" stroke="{INK}" stroke-width="4" stroke-linejoin="round"/></svg>'

def calendar_ill(w='1.2in', c='#2E9C95'):
    return f'<svg viewBox="0 0 120 120" style="width:{w};height:auto"><rect x="12" y="20" width="96" height="88" rx="12" fill="#fff" stroke="{INK}" stroke-width="5"/><path d="M12 48h96" stroke="{INK}" stroke-width="5"/><rect x="12" y="20" width="96" height="28" rx="10" fill="{c}" stroke="{INK}" stroke-width="5"/><path d="M36 10v20M84 10v20" stroke="{INK}" stroke-width="6" stroke-linecap="round"/><path d="M34 68h10M54 68h10M74 68h10M34 88h10M54 88h10" stroke="{INK}" stroke-width="5" stroke-linecap="round"/></svg>'

def phone_ill(w='1.2in', c='#2E9C95'):
    return f'<svg viewBox="0 0 120 120" style="width:{w};height:auto"><rect x="32" y="8" width="56" height="104" rx="12" fill="#fff" stroke="{INK}" stroke-width="5"/><rect x="40" y="22" width="40" height="64" rx="4" fill="{c}"/><path d="M48 100h24" stroke="{INK}" stroke-width="5" stroke-linecap="round"/><path d="M52 40l-6 6 6 6M68 40l6 6-6 6" fill="none" stroke="#fff" stroke-width="3.5" stroke-linecap="round" stroke-linejoin="round"/></svg>'


# the nervous-system "gas pedal / brake" and generic dial
def dial_ill(w='1.2in', c='#4F6FB5'):
    return f'<svg viewBox="0 0 140 90" style="width:{w};height:auto"><path d="M12 80a58 58 0 0 1 116 0" fill="none" stroke="#e1e7ef" stroke-width="16" stroke-linecap="round"/><path d="M12 80a58 58 0 0 1 36-54" fill="none" stroke="#8fd3c8" stroke-width="16" stroke-linecap="round"/><path d="M48 26a58 58 0 0 1 44 0" fill="none" stroke="#f5d58a" stroke-width="16"/><path d="M92 26a58 58 0 0 1 36 54" fill="none" stroke="#e8806a" stroke-width="16" stroke-linecap="round"/><path d="M70 80L96 40" stroke="{INK}" stroke-width="5" stroke-linecap="round"/><circle cx="70" cy="80" r="7" fill="{INK}"/></svg>'


AUD = {'feelings': 'children', 'parent': 'parents', 'teen': 'teens', 'adult': 'adults', 'trauma': 'trauma'}

def R(kit, slug, title, age, kind, topics, teaches, ill, what, how, ex, body, start=False, extra=(), group='materials', z=1.14):
    html = res(kit, title, age, kind, ill, what, how, ex, body, z) + ''.join(extra)
    return dict(kit=kit, aud=AUD[kit], slug=slug, title=title, age=age, kind=kind, topics=topics, teaches=teaches,
                start=start, html=html, pages=1 + len(extra), group=group)
