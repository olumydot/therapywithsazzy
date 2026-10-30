"""Builds resources.html and toolkits/*.html from tools/catalog.json.
Run after tools/make_resources.py:  python3 tools/build_resources_site.py
Re-uses the header/footer already in index.html so the shell stays in sync.
"""
import os, re, json, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from rlib import KITS

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
DOMAIN = 'https://therapywithsazzy.com'
cat = json.load(open(os.path.join(ROOT, 'tools', 'catalog.json')))
home = open(os.path.join(ROOT, 'index.html')).read()

HEAD0 = home[:home.index('</head>') + 7]
HEADER = home[home.index('<header class="site-header">'):home.index('<main id="main">') + len('<main id="main">')]
FOOTER = home[home.index('</main>'):]
HEADER = HEADER.replace('<a href="/resources.html">', '<a href="/resources.html" aria-current="page">')

ARROW = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M5 12h14M13 6l6 6-6 6"/></svg>'
DL = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M12 4v11M7 11l5 5 5-5M5 20h14"/></svg>'
INFO = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><circle cx="12" cy="12" r="9"/><path d="M12 11v5M12 8v.01"/></svg>'

TK = {
    'feelings': dict(page='children', who='Children', title='The Feelings Toolkit', short='Help children recognize, identify, communicate, and manage their emotions.',
                     purpose='Help children recognize, identify, communicate, and manage their emotions. Colorful, visual, and easy to understand, with many pages that children ages 4–12 can use on their own or with a grown-up.',
                     qs=('feelings-toolkit.pdf', 'Quick-Start Pack', 'The 4-page set: feelings chart, thermometer, calm-down cards, and overwhelmed worksheet.'),
                     groups=[('materials', 'The core resources', 'Ten tools that teach children to name feelings, notice their bodies, calm down, and ask for help.'), ('activities', 'Interactive activities', 'Hands-on pages for drawing, designing, matching, and practicing.')],
                     note=''),
    'parent': dict(page='parents', who='Parents', title='The Parent Toolkit', short='Practical strategies to support your child\'s emotional, behavioral, and developmental needs.',
                   purpose='Equip parents and caregivers with practical strategies to support their children\'s emotional, behavioral, and developmental needs. Built for what to do in the moment, not only why a behavior happens.',
                   qs=('parent-toolkit.pdf', 'Quick-Start Pack', 'The 4-page set: visual routine, trigger log, reinforcement planner, and boundaries guide.'),
                   groups=[('materials', 'The core resources', 'Twelve guides and trackers for understanding behavior, setting boundaries, and responding with confidence.'), ('guides', 'Practical parent guides', 'One-page, script-ready responses for the moments that feel hardest.')],
                   note=''),
    'teen': dict(page='teens', who='Teens', title='The Teen Toolkit', short='Tools for identity, friendships, anxiety, self-esteem, and the pressures of adolescence.',
                 purpose='Give teenagers tools to navigate identity, friendships, anxiety, relationships, self-esteem, emotional regulation, and the pressures of adolescence. Modern, mature, and written in real language.',
                 qs=('teen-toolkit.pdf', 'Quick-Start Pack', 'The 4-page set: stress check-in, overthinking worksheet, coping-skills menu, and strengths journal.'),
                 groups=[('materials', 'The core resources', 'Twelve journals, worksheets, and guides for the things teens actually deal with.'), ('activities', 'Reflection activities', 'Short, honest exercises to try on your own.')],
                 note='Good to know: <b>Five Things I Like About Myself</b> is inside the Self-Esteem Journal, <b>What Does a Healthy Friendship Look Like?</b> is inside Healthy vs. Unhealthy Friendships, and the <b>Personal Boundaries Checklist</b> is inside Setting Boundaries.'),
    'adult': dict(page='adults', who='Adults', title='The Adult Wellness Toolkit', short='Practical guidance for stress, boundaries, relationships, self-awareness, and growth.',
                  purpose='Support adults with emotional wellness, stress management, self-awareness, boundaries, relationships, and personal growth, with practical, reflective tools rather than a clinical textbook.',
                  qs=('adult-wellness-toolkit.pdf', 'Quick-Start Pack', 'The 4-page set: personal coping plan, values and boundaries, mindfulness reset, and reflection journal.'),
                  groups=[('materials', 'The core resources', 'Twelve workbooks, check-ins, and guides for everyday emotional wellness.'), ('topics', 'Additional educational topics', 'Short explainers on the nervous system, boundaries, communication, and relationship dynamics.')],
                  note='Fight, flight, freeze, and fawn; attachment patterns; and trauma responses are explained in the <a href="/toolkits/trauma-healing.html">Trauma &amp; Healing Resource Center</a>.'),
    'trauma': dict(page='trauma-healing', who='Trauma & Healing', title='Trauma & Healing Resource Center', short='Learn about trauma, understand your responses, and build safety, grounding, and recovery skills.',
                   purpose='Learn about trauma and understand your emotional responses. Gentle, plain-language education with grounding skills, safety planning, and recovery tools.',
                   qs=None,
                   groups=[('materials', 'The twelve resources', 'Educational guides and worksheets, written to be gentle and go at your pace.')],
                   note=''),
}

for k, t in TK.items():
    ents = cat[k]['entries']
    t['entries'] = ents
    t['n'] = len(ents)
    t['pages'] = cat[k]['pages']

TOTAL = sum(t['n'] for t in TK.values())
COLOR = {k: (KITS[k]['a'], KITS[k]['s'], KITS[k]['d']) for k in KITS}


def head(title, desc, path):
    h = HEAD0
    url = f'{DOMAIN}{path}'
    h = re.sub(r'<title>.*?</title>', f'<title>{title}</title>', h, flags=re.S)
    h = re.sub(r'(<meta name="description" content=")[^"]*', r'\g<1>' + desc.replace('\\', ''), h)
    h = re.sub(r'(<link rel="canonical" href=")[^"]*', r'\g<1>' + url, h)
    h = re.sub(r'(<meta property="og:title" content=")[^"]*', r'\g<1>' + title, h)
    h = re.sub(r'(<meta property="og:description" content=")[^"]*', r'\g<1>' + desc, h)
    h = re.sub(r'(<meta property="og:url" content=")[^"]*', r'\g<1>' + url, h)
    h = re.sub(r'<script type="application/ld\+json">.*?</script>', '', h, flags=re.S)
    return h + '\n<body>\n<a class="skip" href="#main">Skip to content</a>\n'


def cta(h, p):
    return f'<section class="cta"><div class="wrap"><div class="cta-card reveal"><div><h2>{h}</h2><p>{p}</p></div><div class="cta-row"><a class="btn btn-coral" href="/get-started.html">Send an inquiry {ARROW}</a></div></div></div></section>\n'


def card(e, kit):
    a, s, d = COLOR[kit]
    star = '<span class="star">★ Start here</span>' if e['start'] else ''
    pg = f' · {e["pages"]} pages' if e['pages'] > 1 else ''
    return (f'<article class="rc-card reveal" style="--a:{a};--s:{s}"><a class="rc-thumb" href="/resources/{e["slug"]}.pdf" target="_blank" rel="noopener" aria-label="Preview {e["title"]}">{star}'
            f'<img loading="lazy" src="/resources/thumbs/{e["slug"]}.jpg" alt="Preview of {e["title"]}"></a>'
            f'<div class="rc-body"><div class="rc-tags"><span>{e["kind"]}</span><span>{e["age"]}{pg}</span></div><h3>{e["title"]}</h3><p>{e["teaches"]}</p>'
            f'<div class="rc-actions"><a class="btn btn-primary" href="/resources/{e["slug"]}.pdf" download>{DL} Download</a><a class="btn btn-ghost" href="/resources/{e["slug"]}.pdf" target="_blank" rel="noopener">Preview</a></div></div></article>')


def thumbs(kit, slugs, cls):
    return ''.join(f'<img src="/resources/thumbs/{s}.jpg" alt="" loading="lazy">' for s in slugs)


FAN = {'feelings': ['where-do-i-feel-it', 'my-feelings-chart', 'my-calm-down-menu'], 'parent': ['behavior-abc-tracker', 'managing-emotional-outbursts', 'positive-reinforcement-planner'],
       'teen': ['my-identity-and-values', 'anxiety-management-guide', 'overthinking-worksheet'], 'adult': ['personal-coping-plan', 'stress-management-workbook', 'burnout-prevention-guide'],
       'trauma': ['the-window-of-tolerance', 'grounding-techniques-for-emotional-distress', 'fight-flight-freeze-and-fawn']}


def nav(current):
    items = ''.join(f'<a href="/toolkits/{t["page"]}.html" {"aria-current=\"page\"" if k == current else ""} style="--c:{COLOR[k][0]}"><i></i>{t["who"]}</a>' for k, t in TK.items())
    return f'<div class="tk-nav"><a href="/resources.html" style="--c:#0F2A4A"><i></i>Resource center</a>{items}</div>'


# =================================================================== toolkit pages
def toolkit_page(k):
    t = TK[k]
    a, s, d = COLOR[k]
    path = f'/toolkits/{t["page"]}.html'
    h = head(f'{t["title"]} | Free Printable Resources | Therapy with Sazzy', f'{t["short"]} Free downloadable PDFs from Therapy with Sazzy.', path) + HEADER.replace('href="/', 'href="/')
    qs = ''
    dl = f'<a class="btn btn-primary" href="/resources/complete-{k}.pdf" download>{DL} Download the complete toolkit</a>'
    h += f'''
<section class="page-hero tk-hero" style="--c:{s};--a:{a};--s:{s};--d:{d}"><div class="wrap">
  <div>
    <div class="crumbs"><a href="/">Home</a> / <a href="/resources.html">Resources</a> / {t["who"]}</div>
    <span class="eyebrow">{t["who"]} · {t["n"]} resources</span>
    <h1>{t["title"]}</h1>
    <p class="lead">{t["purpose"]}</p>
    <div class="cta-row">{dl}<a class="btn btn-ghost" href="#resources">Browse the resources</a></div>
  </div>
  <div class="fan reveal">{thumbs(k, FAN[k], 'fan')}</div>
</div></section>
<section class="section" style="padding-top:10px;padding-bottom:30px"><div class="wrap">
  <div class="dl-strip">
    <div class="dl-card reveal" style="--a:{a}"><img src="/resources/thumbs/{FAN[k][0]}.jpg" alt=""><div><h3>Complete toolkit</h3><p>All {t["n"]} resources in one printable PDF ({t["pages"]} pages).</p><a class="btn btn-primary btn-sm" href="/resources/complete-{k}.pdf" download>{DL} Download PDF</a></div></div>'''
    if t['qs']:
        f, nm, desc = t['qs']
        h += f'''
    <div class="dl-card reveal" style="--a:{a};--d:.08s"><img src="/resources/thumbs/qs-{k}.jpg" alt="First page of the {nm}"><div><h3>{nm}</h3><p>{desc}</p><a class="btn btn-ghost btn-sm" href="/resources/{f}" download>{DL} Download PDF</a></div></div>'''
    else:
        h += f'''
    <div class="dl-card reveal" style="--a:{a};--d:.08s"><div>{INFO}</div><div><h3>Go at your own pace</h3><p>Trauma education and self-help materials are not a substitute for individualized trauma-informed care. Skip anything that feels like too much.</p><a class="btn btn-ghost btn-sm" href="/get-started.html">Talk with Sazzy</a></div></div>'''
    h += '\n  </div>\n</div></section>\n<section class="section" id="resources" style="padding-top:20px"><div class="wrap">'
    for gk, gt, gd in t['groups']:
        es = [e for e in t['entries'] if e['group'] == gk]
        if not es:
            continue
        cols = ' three' if len(es) <= 6 else ''
        h += f'<div class="group-head reveal"><div><span class="eyebrow">{gk.replace("materials", "Materials").replace("activities", "Activities").replace("guides", "Guides").replace("topics", "Topics")}</span><h2>{gt}</h2><p>{gd}</p></div></div><div class="rc-grid{cols}" style="margin-bottom:56px">'
        h += ''.join(card(e, k) for e in es) + '</div>'
    if t['note']:
        h += f'<div class="callout reveal">{INFO}<p>{t["note"]}</p></div>'
    h += f'<div class="callout coral reveal" style="margin-top:20px">{INFO}<p><strong>About these materials.</strong> Each page includes an explanation, instructions, a practical example, and an activity. Age suggestions are a guide, and you know the person best. These are educational self-help resources, not a diagnosis or a substitute for individualized professional care. In a crisis, call or text 988 or call 911.</p></div>'
    h += '</div></section>\n<section class="section band-sand" style="padding:50px 0"><div class="wrap"><div class="section-head center reveal" style="margin-bottom:24px"><h2 style="font-size:1.8rem">Explore more toolkits</h2></div>' + nav(k) + '</div></section>\n'
    h += cta('Want support beyond the printables?', 'These tools work best alongside connection. Reach out to talk about counseling, parent coaching, or a workshop for your group.')
    h += FOOTER
    os.makedirs(os.path.join(ROOT, 'toolkits'), exist_ok=True)
    open(os.path.join(ROOT, 'toolkits', t['page'] + '.html'), 'w').write(h)


# =================================================================== hub
def hub():
    entries = [dict(s=e['slug'], t=e['title'], a=k and TK[k]['page'] if False else None) for k in TK for e in TK[k]['entries']]
    flat = []
    audmap = {'feelings': 'children', 'parent': 'parents', 'teen': 'teens', 'adult': 'adults', 'trauma': 'trauma'}
    for k in TK:
        for e in cat[k]['entries']:
            flat.append(dict(s=e['slug'], t=e['title'], a=audmap[k], k=e['kind'], g=e['age'], d=e['teaches'], tp=e['topics'], st=bool(e['start']), pg=e['pages']))
    open(os.path.join(ROOT, 'js', 'catalog.js'), 'w').write('window.CATALOG=' + json.dumps(flat, separators=(',', ':')) + ';')
    starts = sum(1 for e in flat if e['st'])
    h = head('Free Resource Center | Printable Emotional Wellness Tools | Therapy with Sazzy',
             f'{TOTAL} free printable worksheets, guides, and activities for children, teens, adults, and parents, plus a Trauma & Healing Resource Center. Learn. Grow. Heal. Thrive.', '/resources.html') + HEADER
    h += f'''
<section class="page-hero rc-hero" style="--c:#f7e8c8"><div class="wrap">
  <div>
    <div class="crumbs"><a href="/">Home</a> / Resources</div>
    <span class="eyebrow">Free resource center</span>
    <h1>Practical tools for everyday emotional wellness.</h1>
    <p class="lead">Worksheets, guides, and activities you can print and use today. Made for children, teens, adults, and parents, and free to everyone. You don&rsquo;t have to be a client.</p>
    <div class="cta-row"><a class="btn btn-primary" href="#center">Explore the resource center {ARROW}</a><a class="btn btn-ghost" href="#center" data-pick-start>Start with the {starts} foundations</a></div>
    <div class="rc-stats"><span class="chip"><i></i>{TOTAL} free printables</span><span class="chip"><i></i>5 toolkits</span><span class="chip"><i></i>Instructions and examples included</span></div>
  </div>
  <div class="fan reveal"><img src="/resources/thumbs/my-feelings-chart.jpg" alt="" ><img src="/resources/thumbs/behavior-abc-tracker.jpg" alt=""><img src="/resources/thumbs/anxiety-management-guide.jpg" alt=""></div>
</div></section>
<div class="tagline-band"><div class="wrap"><span><b>Learn.</b></span><span><b>Grow.</b></span><span><b>Heal.</b></span><span><b>Thrive.</b></span></div></div>

<section class="section" id="toolkits"><div class="wrap">
  <div class="section-head center reveal"><span class="eyebrow">Explore &amp; learn</span><h2>Five toolkits. One for every kind of support.</h2><p class="lead">Choose a toolkit to see every resource inside, preview each page, and download exactly what you need.</p></div>
  <div class="tk-grid">'''
    badge = {'feelings': 'Ages 4–12', 'parent': 'Parents & caregivers', 'teen': 'Ages 12–18', 'adult': 'Adults', 'trauma': 'Healing'}
    for i, (k, t) in enumerate(TK.items()):
        a, s, d = COLOR[k]
        h += f'''
    <a class="tk-card reveal" href="/toolkits/{t["page"]}.html" style="--a:{a};--s:{s};--d:{d};--d2:{i*.06}s"><span class="tk-badge">{badge[k]}</span><div class="stack">{thumbs(k, FAN[k], 'stack')}</div><h3>{t["title"]}</h3><p>{t["short"]}</p><div class="tk-meta"><span>{t["n"]} resources · {t["pages"]} pages</span><span class="more">Open toolkit {ARROW}</span></div></a>'''
    h += f'''
  </div>
</div></section>

<section class="section band-sand" id="center"><div class="wrap">
  <div class="section-head reveal"><span class="eyebrow">Explore your resource center</span><h2>Find the right resource in three steps.</h2><p class="lead">Tell me who it&rsquo;s for and what you&rsquo;re working on, and I&rsquo;ll narrow the collection.</p></div>
  <div class="center-panel reveal" id="rc-center">
    <p class="step-label"><i>1</i> Who are you looking for resources for?</p>
    <div class="tabs" id="rc-tabs" role="group" aria-label="Audience"></div>
    <p class="step-label"><i>2</i> Choose a topic</p>
    <div class="chips" id="rc-chips" role="group" aria-label="Topic"></div>
    <p class="step-label"><i>3</i> Search, or start with the foundations</p>
    <div class="search-row"><input type="search" id="rc-q" placeholder="Search resources, e.g. “worry”, “routine”, “grounding”" aria-label="Search resources"><label class="toggle"><input type="checkbox" id="rc-start"> Show the {starts} foundation resources</label></div>
    <div class="rc-summary"><h3 id="rc-title">Your resource collection</h3><span id="rc-count" aria-live="polite"></span></div>
    <div class="rc-grid" id="rc-grid"></div>
  </div>
</div></section>

<section class="section"><div class="wrap"><div class="feature reveal">
  <img src="/resources/thumbs/grounding-techniques-for-emotional-distress.jpg" alt="Preview of the Grounding Techniques guide" loading="lazy">
  <div><span class="eyebrow">Resource of the month</span><h2>Grounding Techniques for Emotional Distress</h2><p class="lead" style="color:#b9c9dc">Eight simple ways to bring your attention back to the present when emotions feel too big. Includes a practice log so you can see what works for you.</p>
  <div class="cta-row"><a class="btn btn-coral" href="/resources/grounding-techniques-for-emotional-distress.pdf" download>{DL} Download free</a><a class="btn btn-light" href="/toolkits/trauma-healing.html">Trauma &amp; Healing center</a></div></div>
</div></div></section>

<section class="section" style="padding-top:0"><div class="wrap">
  <div class="callout reveal">{INFO}<p><strong>How to use these.</strong> Print them, fill them out together, and keep what works. Each includes an explanation, instructions, an example, and an activity. They are educational self-help materials, not a diagnosis or a substitute for individualized professional care. If you or someone you love is in crisis, call or text 988 or call 911.</p></div>
</div></section>
'''
    h += cta('Want something specific?', 'Tell me what would be most useful for you or your family, and it may shape the next resource.')
    h += FOOTER.replace('<script src="/js/main.js" defer></script>', '<script src="/js/main.js" defer></script>\n<script src="/js/catalog.js"></script>\n<script src="/js/resources.js" defer></script>')
    open(os.path.join(ROOT, 'resources.html'), 'w').write(h)


for k in TK:
    toolkit_page(k)
hub()

# sitemap
sm = open(os.path.join(ROOT, 'sitemap.xml')).read()
for t in TK.values():
    loc = f'<url><loc>{DOMAIN}/toolkits/{t["page"]}.html</loc></url>\n'
    if loc not in sm:
        sm = sm.replace('</urlset>', loc + '</urlset>')
open(os.path.join(ROOT, 'sitemap.xml'), 'w').write(sm)
print('built hub + 5 toolkit pages;', TOTAL, 'resources')
