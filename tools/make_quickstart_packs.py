"""Builds the four printable toolkit PDFs in ../resources/ (needs Google Chrome).
Run: python3 tools/make_quickstart_packs.py
"""
import os, subprocess, tempfile

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, '..', 'resources')
CHROME = '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome'
FONT = 'file://' + os.path.join(HERE, 'Fraunces.ttf')

MARK = '<svg viewBox="0 0 64 64"><path d="M50.6 29.6 A21 21 0 1 1 35.6 13.5" fill="none" stroke="#0F2A4A" stroke-width="5.2" stroke-linecap="round"/><path d="M30 49 C30 39 34 31 43 23 C48 18.5 52 14.5 55 9" fill="none" stroke="#2E9C95" stroke-width="4.2" stroke-linecap="round"/><path d="M31.2 40.5 C24 40.5 19.5 36 19.5 29.5 C26.5 29.5 31.2 33.5 31.2 40.5Z" fill="#6CC4BC"/><path d="M36.5 31.5 C43 33 47.5 31 49.5 25.5 C43.5 23.5 38.5 25.5 36.5 31.5Z" fill="#6CC4BC"/><circle cx="56.5" cy="7.5" r="4.3" fill="#E8806A"/></svg>'

CSS = '''
@font-face{font-family:Fr;src:url(%s);font-weight:100 900}
@page{size:Letter;margin:0}
*{box-sizing:border-box}
body{margin:0;font:12.5pt/1.5 -apple-system,"Helvetica Neue",Arial,sans-serif;color:#16243a}
.page{width:8.5in;height:11in;padding:.55in .65in .5in;position:relative;page-break-after:always;overflow:hidden;background:#fff}
.page:last-child{page-break-after:auto}
.top{display:flex;align-items:center;gap:10px;border-bottom:2px solid #d3ece8;padding-bottom:10px;margin-bottom:18px}
.top svg{width:34px;height:34px}
.top b{font:600 13pt Fr,Georgia,serif;color:#0F2A4A}
.top span{margin-left:auto;font-size:8.5pt;letter-spacing:.14em;text-transform:uppercase;color:#1f7a74;font-weight:700}
h1{font:600 28pt/1.1 Fr,Georgia,serif;color:#0F2A4A;margin:0 0 6px}
h2{font:600 15pt Fr,Georgia,serif;color:#0F2A4A;margin:16px 0 6px}
.sub{color:#56657a;margin:0 0 14px;font-size:12pt}
.foot{position:absolute;left:.65in;right:.65in;bottom:.32in;font-size:7.8pt;color:#6b7a8e;border-top:1px solid #e3e8ef;padding-top:6px;display:flex;justify-content:space-between;gap:20px}
.line{border-bottom:1.3px solid #9fb0c4;height:25px}
.box{border:1.5px solid #9fb0c4;border-radius:12px;padding:10px 14px}
.tint{background:#fbf6ee}.teal{background:#e6f4f1;border-color:#bfe0da}.coral{background:#fdeee9;border-color:#f3cfc4}.sand{background:#f7f0e2;border-color:#e8dcc4}
.grid{display:grid;gap:12px}
.g2{grid-template-columns:1fr 1fr}.g3{grid-template-columns:repeat(3,1fr)}.g4{grid-template-columns:repeat(4,1fr)}
.cb{display:inline-block;width:13px;height:13px;border:1.6px solid #0F2A4A;border-radius:3px;margin-right:8px;vertical-align:-2px;flex:none}
ul.cbs{list-style:none;margin:0;padding:0}ul.cbs li{margin:4px 0;display:flex}
.small{font-size:10pt;color:#56657a}
.lab{font-weight:700;color:#0F2A4A;font-size:11pt}
table{width:100%%;border-collapse:collapse}
th{background:#0F2A4A;color:#fff;font-size:9pt;text-align:left;padding:7px 8px;font-weight:600}
td{border:1.3px solid #b9c6d6;height:62px;vertical-align:top;padding:4px}
.face{text-align:center;border:1.5px solid #cfd9e6;border-radius:14px;padding:8px 6px 6px}
.face svg{width:62px;height:62px}.face b{display:block;font-size:12pt;color:#0F2A4A}
.card{border:1.6px dashed #6CC4BC;border-radius:14px;padding:12px 14px;height:1.92in;overflow:hidden}
.card h3{font:600 14pt Fr,Georgia,serif;margin:0 0 4px;color:#0F2A4A}
.card ol{margin:4px 0 0;padding-left:18px;font-size:10.5pt;line-height:1.4}
.num{display:inline-grid;place-items:center;width:26px;height:26px;border-radius:50%%;background:#0F2A4A;color:#fff;font-weight:700;font-size:11pt;margin-right:8px}
''' % FONT

DISCLAIMER = 'Educational self-help resource from Therapy with Sazzy, an initiative of Beyond Boundaries Consulting, LLC. Not a substitute for individualized professional care. In a crisis call or text 988, or call 911.'

def page(title, sub, body, label):
    return f'''<section class="page"><div class="top">{MARK}<b>Therapy with Sazzy</b><span>{label}</span></div>
<h1>{title}</h1><p class="sub">{sub}</p>{body}
<div class="foot"><span>{DISCLAIMER}</span><span>therapywithsazzy.com</span></div></section>'''

def lines(n): return ''.join('<div class="line"></div>' for _ in range(n))
def cbs(items): return '<ul class="cbs">' + ''.join(f'<li><i class="cb"></i><span>{i}</span></li>' for i in items) + '</ul>'
def field(label, n=1, cls=''): return f'<div class="{cls}"><div class="lab">{label}</div>{lines(n)}</div>'

def face(bg, feat):
    return f'<svg viewBox="0 0 64 64"><circle cx="32" cy="32" r="29" fill="{bg}"/><g fill="#16243a" stroke="#16243a" stroke-width="3" stroke-linecap="round" stroke-linejoin="round">{feat}</g></svg>'
E2 = '<circle cx="23" cy="28" r="3" stroke="none"/><circle cx="41" cy="28" r="3" stroke="none"/>'
FACES = [
 ('Happy', '#fbe3a8', E2 + '<path d="M22 39c4 8 16 8 20 0" fill="none"/>'),
 ('Calm', '#cdeae5', '<path d="M18 29q5 4 10 0M36 29q5 4 10 0" fill="none"/><path d="M24 41c4 4 12 4 16 0" fill="none"/>'),
 ('Excited', '#fbe3a8', E2 + '<path d="M20 38c3 9 21 9 24 0z" stroke-width="2"/>'),
 ('Proud', '#f7d9a8', '<path d="M18 29q5-4 10 0M36 29q5-4 10 0" fill="none"/><path d="M21 38c5 8 17 8 22 0" fill="none"/>'),
 ('Worried', '#cfe0f5', E2 + '<path d="M17 25l9-4M47 25l-9-4" fill="none"/><path d="M24 44c3-3 13-3 16 0" fill="none"/>'),
 ('Scared', '#d8d4ee', '<circle cx="23" cy="28" r="4.5" fill="#fff" stroke-width="2"/><circle cx="41" cy="28" r="4.5" fill="#fff" stroke-width="2"/><circle cx="23" cy="28" r="1.6" stroke="none"/><circle cx="41" cy="28" r="1.6" stroke="none"/><ellipse cx="32" cy="44" rx="5" ry="6" stroke-width="2"/>'),
 ('Sad', '#d9e0ee', E2 + '<path d="M24 46c3-4 13-4 16 0" fill="none"/>'),
 ('Lonely', '#dfe3ea', E2 + '<path d="M20 47c4-3 20-3 24 0" fill="none"/><path d="M18 22q5-3 9-1M46 22q-5-3-9-1" fill="none" stroke-width="2"/>'),
 ('Frustrated', '#fbd0c6', E2 + '<path d="M16 22l10 5M48 22l-10 5" fill="none"/><path d="M24 45h16" fill="none"/>'),
 ('Angry', '#f7b8a8', E2 + '<path d="M15 21l12 7M49 21l-12 7" fill="none" stroke-width="3.6"/><path d="M22 46q10-8 20 0" fill="none"/>'),
 ('Tired', '#e3e0ea', '<path d="M18 29h10M36 29h10" fill="none"/><ellipse cx="32" cy="43" rx="4.5" ry="3.5" stroke-width="2"/>'),
 ('Embarrassed', '#f9d6d6', E2 + '<circle cx="16" cy="37" r="4" fill="#f08f8f" stroke="none" opacity=".7"/><circle cx="48" cy="37" r="4" fill="#f08f8f" stroke="none" opacity=".7"/><path d="M24 44q4 3 8 0t8 0" fill="none" stroke-width="2.4"/>'),
]

# ============================================================ FEELINGS
def feelings():
    P = []
    f = ''.join(f'<div class="face">{face(bg, ft)}<b>{n}</b><div class="small">I feel it in my</div><div class="line" style="height:20px"></div></div>' for n, bg, ft in FACES)
    P.append(page('Feelings Identification Chart', 'All feelings are okay. Point to the face that matches, or circle more than one. Then notice where you feel it in your body.',
        f'<div class="grid g3">{f}</div><div class="box teal" style="margin-top:14px"><div class="lab">Today I feel ______________________ because ______________________________________</div><div class="small" style="margin-top:6px">Remember: feelings are information. They are not good or bad, and they change.</div></div>', 'The Feelings Toolkit'))

    zones = [('9–10', 'Biggest', '#e8806a', 'Stop, stay safe, and get a trusted grown-up. Breathe slowly. Wait before talking or deciding.'),
             ('7–8', 'Big', '#f2a96b', 'Take a break. Use a calm-down card. Move your body or ask for a hug.'),
             ('4–6', 'Medium', '#f5d58a', 'Notice it. Name it. Try a deep breath or a quick reset.'),
             ('1–3', 'Small', '#8fd3c8', 'Great time to practice a skill. Check in on your body.')]
    z = ''.join(f'<div style="display:flex;gap:14px;align-items:stretch;margin-bottom:12px"><div style="width:150px;background:{c};border-radius:14px;display:grid;place-items:center;text-align:center;padding:10px"><div><div style="font:600 24pt Fr,Georgia,serif;color:#0F2A4A">{n}</div><b>{l}</b></div></div><div class="box" style="flex:1"><div class="lab">What helps at this level</div><div class="small" style="margin:2px 0 4px">{t}</div>{lines(1)}</div></div>' for n, l, c, t in zones)
    P.append(page('Emotional Intensity Thermometer', 'Feelings come in different sizes. Rate how big your feeling is right now, then choose what helps at that size.',
        z + '<div class="box tint"><span class="lab">Right now my feeling is a ____ out of 10. </span><span class="lab">The feeling is: ______________</span></div>', 'The Feelings Toolkit'))

    cards = [('Belly breathing', ['Put a hand on your belly.', 'Breathe in through your nose for 4.', 'Breathe out slowly for 6, like blowing a candle.', 'Repeat 5 times.']),
             ('5-4-3-2-1 senses', ['Name 5 things you see.', '4 things you can touch.', '3 things you hear.', '2 things you smell.', '1 thing you taste.']),
             ('Squeeze &amp; release', ['Make tight fists for 5 seconds.', 'Let go and feel the difference.', 'Now scrunch shoulders, then drop them.', 'Do toes, then legs.']),
             ('Cool down', ['Splash cool water on your face or hold something cool.', 'Take 3 slow breaths.', 'Notice how your body feels now.']),
             ('Count it out', ['Count backwards from 20.', 'Go slowly.', 'If you lose count, start again. That is okay.']),
             ('Ask for a hug', ['Say, "I need a hug" or "I need space."', 'Take 3 slow breaths together.', 'Tell them how you feel when you are ready.']),
             ('Move your body', ['Do 10 jumping jacks or wall push-ups.', 'Stretch up high, then touch your toes.', 'Shake out your hands and feet.']),
             ('Draw it out', ['Draw how your feeling looks.', 'Give it a color and a shape.', 'Change the drawing to show it getting smaller.'])]
    cd = ''.join(f'<div class="card"><h3>{t}</h3><ol>{"".join(f"<li>{s}</li>" for s in st)}</ol></div>' for t, st in cards)
    P.append(page('Calm-Down Strategy Cards', 'Cut along the dashed lines. Keep them in a bag, pocket, or calm-down corner. Practice when you are calm so they are easier when you are not.',
        f'<div class="grid g2">{cd}</div>', 'The Feelings Toolkit'))

    P.append(page('What Can I Do When I Feel Overwhelmed?', 'Overwhelmed means a lot is happening at once. Slow down and take it one step at a time.',
        field('1. Right now I feel…', 1) + field('2. My body is telling me… (tight, hot, shaky, tired)', 1) +
        field('3. What is making things feel like too much?', 2) +
        '<h2>4. Circle the things that might help</h2><div class="grid g3 small" style="color:#16243a;font-size:11pt">' +
        ''.join(f'<div class="box teal" style="text-align:center;padding:8px 6px">{x}</div>' for x in ['Take 5 slow breaths', 'Take a short break', 'Get a drink of water', 'Move my body', 'Ask for help', 'Tell someone how I feel', 'Write or draw it', 'Make a small list', 'Listen to calm music']) +
        '</div><div style="height:8px"></div>' + field('5. What is ONE small thing I can do next?', 2) + field('6. Who can I ask for help? (a grown-up or someone I trust)', 1) +
        '<div class="box coral" style="margin-top:14px"><b>Remember:</b> You do not have to do everything at once. Taking one small step counts.</div>', 'The Feelings Toolkit'))
    return P

# ============================================================ PARENT
def parent():
    P = []
    steps = ''.join(f'<div class="box" style="display:flex;gap:12px;align-items:center;margin-bottom:10px;height:.82in"><span class="num">{i}</span><div style="flex:1"><div class="lab" style="margin-bottom:2px">Step {i}</div><div class="line" style="height:22px"></div></div><div class="box teal" style="width:1in;height:.6in;text-align:center;font-size:8pt;color:#56657a;padding-top:14px">draw / picture</div><i class="cb" style="width:22px;height:22px"></i></div>' for i in range(1, 7))
    P.append(page('Visual Routine Template', 'Children thrive on predictability. Use pictures or words for each step, and let your child check off each one.',
        '<div class="lab" style="margin-bottom:10px">Routine: ☐ Morning &nbsp; ☐ After school &nbsp; ☐ Bedtime &nbsp; ☐ Other: ____________</div>' + steps +
        '<div class="box sand"><b>Tips:</b> Keep it to 4–6 steps. Use photos or simple drawings. Review it together when everyone is calm. Praise each step finished, not just the last one.</div>', 'The Parent Toolkit'))

    heads = ['Date / time', 'What happened just before? (trigger)', 'What did I see my child do?', 'What did I do?', 'What happened after?', 'What might help next time?']
    P.append(page('Trigger &amp; Response Log', 'Patterns are easier to see on paper. Note what happened before, during, and after, without judgment. Bring it to your next conversation.',
        '<table><tr>' + ''.join(f'<th>{h}</th>' for h in heads) + '</tr>' + '<tr>' + '<td></td>' * 6 + '</tr>' + ('<tr>' + '<td></td>' * 6 + '</tr>') * 7 + '</table>' +
        '<div class="box teal" style="margin-top:12px"><b>Look for patterns:</b> Time of day · hunger or tiredness · transitions · demands · noise or crowds · being told "no" · feeling left out. <i>Behavior is communication. What might it be telling you?</i></div>', 'The Parent Toolkit'))

    P.append(page('Positive Reinforcement Planner', 'What we notice and celebrate grows. Plan how to catch your child doing well.',
        field('Skill we are building (be specific and observable)', 1) + field('What it looks like when they do it', 2) +
        '<div class="grid g2" style="margin-top:6px"><div class="box teal"><div class="lab">Praise I can use</div>' + lines(3) + '<div class="small">Be specific: "You took a breath when you felt mad. Nice calm!"</div></div><div class="box coral"><div class="lab">Rewards (small and soon)</div>' + lines(3) + '<div class="small">Time together, choice of game, sticker, special snack.</div></div></div>' +
        '<h2>Tracker</h2><table><tr>' + ''.join(f'<th style="text-align:center">{d}</th>' for d in ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']) + '</tr><tr>' + '<td style="height:58px"></td>' * 7 + '</tr></table>' +
        '<div class="box sand" style="margin-top:12px"><b>Guidelines:</b> Notice effort, not just results. Reinforce right away. Aim for more praise than corrections. Connection is the best reward.</div>', 'The Parent Toolkit'))

    items = [('Calm yourself first', 'Take a slow breath. Your calm helps your child borrow calm.'),
             ('Be clear and brief', 'State the expectation in a few words. "Shoes on, then we go."'),
             ('Give choices', 'Two acceptable options: "Bath before or after pajamas?"'),
             ('Follow through', 'Do what you said, kindly and every time. Consistency builds trust.'),
             ('Name the feeling, hold the limit', '"You\'re upset. It\'s still time to turn off the tablet."'),
             ('Repair after', 'When things have cooled, reconnect. Talk about what to try next time.')]
    g = ''.join(f'<div class="box {c}" style="margin-bottom:10px;display:flex;gap:12px"><span class="num">{i+1}</span><div><div class="lab">{t}</div><div style="font-size:11.5pt">{d}</div></div></div>' for i, ((t, d), c) in enumerate(zip(items, ['teal', 'tint', 'teal', 'tint', 'teal', 'tint'])))
    P.append(page('Guide to Calm, Consistent Boundaries', 'Boundaries are not punishments. They are the safe edges that help children feel secure.',
        g + '<div class="box coral"><b>When things escalate:</b> Keep everyone safe. Use fewer words and a calm voice. Do not negotiate in the heat of the moment. Wait until your child is calm to talk. If there is a risk of harm to anyone, seek help immediately.</div>', 'The Parent Toolkit'))
    return P

# ============================================================ TEEN
def teen():
    P = []
    rows = ''.join(f'<div style="margin:12px 0"><div class="lab">{t}</div><div style="display:flex;justify-content:space-between;align-items:center;margin-top:6px">' + ''.join(f'<span style="width:30px;height:30px;border-radius:50%;border:1.6px solid #0F2A4A;display:grid;place-items:center;font-size:10pt">{n}</span>' for n in range(1, 11)) + f'</div><div class="small" style="display:flex;justify-content:space-between"><span>{lo}</span><span>{hi}</span></div></div>' for t, lo, hi in [('Body: how tense or tired do I feel?', 'relaxed', 'very tense'), ('Mind: how racing or foggy are my thoughts?', 'clear', 'racing'), ('Mood: how heavy or on-edge do I feel?', 'light', 'heavy'), ('Energy: how drained am I?', 'full', 'empty')])
    P.append(page('Stress Check-In', 'Takes two minutes. Circle a number for each (1 is low, 10 is high). No right answers.',
        rows + field('What is adding to my stress right now?', 2) + field('One thing that would help a little', 1) +
        '<div class="box teal" style="margin-top:10px">If your numbers are mostly high for a couple of weeks, talk with a parent, school counselor, or other trusted adult. You do not have to handle it alone.</div>', 'The Teen Toolkit'))

    P.append(page('Overthinking Worksheet', 'When your mind loops, get it on paper. Separate what is true from what your brain is guessing.',
        field('The thought that keeps looping', 2) +
        '<div class="grid g2"><div class="box teal"><div class="lab">Facts (what I know)</div>' + lines(3) + '</div><div class="box coral"><div class="lab">Story (what I\'m guessing)</div>' + lines(3) + '</div></div>' +
        '<div class="grid g3" style="margin-top:12px"><div class="box"><div class="lab">Worst case</div>' + lines(2) + '</div><div class="box"><div class="lab">Best case</div>' + lines(2) + '</div><div class="box"><div class="lab">Most likely</div>' + lines(2) + '</div></div>' +
        field('What is in my control? What is not?', 2) + field('One small step I can take (or let go of)', 1), 'The Teen Toolkit'))

    cols = [('Quick resets (1–5 min)', ['Slow breathing', 'Cold water on face', 'Step outside', 'Stretch', 'Favorite song']), ('Move', ['Walk', 'Shoot hoops', 'Dance', 'Workout', 'Bike ride']),
            ('Connect', ['Text a friend', 'Talk to family', 'Hang with a pet', 'Join a group']), ('Create', ['Draw or doodle', 'Write or journal', 'Play music', 'Cook or bake']), ('Rest', ['Short nap', 'Warm shower', 'Read', 'Screen break']), ('Reflect', ['Make a to-do list', 'Name the feeling', 'Gratitude: 3 things', 'Write a note to future me'])]
    cg = ''.join(f'<div class="box {c}"><div class="lab" style="margin-bottom:4px">{t}</div>{cbs(i)}<div class="line"></div></div>' for (t, i), c in zip(cols, ['teal', 'tint', 'coral', 'sand', 'teal', 'tint']))
    P.append(page('Coping-Skills Menu', 'Pick what fits how you feel right now. Check what works for you and add your own.',
        f'<div class="grid g2">{cg}</div><div class="box" style="margin-top:12px"><span class="lab">My top 3:</span> 1. __________________ 2. __________________ 3. __________________</div>', 'The Teen Toolkit'))

    P.append(page('Self-Confidence &amp; Strengths Journal', 'Your brain remembers mistakes loudly. This page helps you notice what you do well.',
        field('Three things I am good at', 3) + field('A time I handled something hard', 2) + field('What a friend would say is great about me', 2) +
        '<h2>This week</h2><table><tr><th>Day</th><th>One thing I did well or am proud of</th></tr>' + ''.join(f'<tr><td style="height:31px;width:90px">{d}</td><td></td></tr>' for d in ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']) + '</table>' +
        '<div class="box teal" style="margin-top:10px">Confidence grows from small actions, not from feeling perfect first.</div>', 'The Teen Toolkit'))
    return P

# ============================================================ ADULT
def adult():
    P = []
    P.append(page('Personal Coping Plan', 'A plan made while calm is easier to use when stress is high. Fill it in and keep it where you can find it.',
        field('My early warning signs (body, thoughts, behavior)', 3) + field('Things that help me settle (alone)', 3) +
        '<div class="grid g2"><div>' + field('People I can reach out to', 3) + '</div><div>' + field('Places that help me feel better', 3) + '</div></div>' +
        field('Professional supports (counselor, doctor, support group)', 2) +
        '<div class="box coral" style="margin-top:10px"><b>If you are in crisis or thinking of harming yourself:</b> call or text <b>988</b> (Suicide &amp; Crisis Lifeline) or call <b>911</b>. Go to the nearest emergency department.</div>' +
        '<div class="small" style="margin-top:8px">This plan is a self-help tool and is not a substitute for professional care.</div>', 'The Adult Wellness Toolkit'))

    vals = ['Family', 'Health', 'Honesty', 'Growth', 'Faith', 'Freedom', 'Security', 'Creativity', 'Service', 'Connection', 'Rest', 'Adventure', 'Respect', 'Learning', 'Peace', 'Purpose']
    P.append(page('Values &amp; Boundaries Worksheet', 'Values show what matters. Boundaries protect it.',
        '<div class="lab">1. Circle your top 5 values</div><div class="grid g4" style="margin:8px 0">' + ''.join(f'<div class="box tint" style="text-align:center;padding:6px">{v}</div>' for v in vals) + '</div>' +
        '<div class="lab" style="margin-top:12px">2. Where do I need a clearer boundary?</div><table style="margin-top:6px"><tr><th>Situation / person</th><th>What I need</th><th>How I will say it</th></tr>' + '<tr><td></td><td></td><td></td></tr>' * 4 + '</table>' +
        '<div class="box teal" style="margin-top:12px"><b>A boundary sentence:</b> "I can\'t ______, but I can ______." / "I need ______ so that ______." Calm, clear, and kind is enough. You do not have to over-explain.</div>' + field('The first boundary I will practice this week', 2), 'The Adult Wellness Toolkit'))

    P.append(page('Mindfulness Exercise: 5-Minute Reset', 'Mindfulness is noticing what is happening, without judging it. Find a quiet spot. Read each step, then try it.',
        '<div class="box teal" style="margin-bottom:10px"><span class="num">1</span><b>Arrive (30 sec)</b> Sit comfortably. Feel your feet and the surface under you.</div>' +
        '<div class="box tint" style="margin-bottom:10px"><span class="num">2</span><b>Breathe (1 min)</b> Breathe in for 4, out for 6. Let the exhale be slow.</div>' +
        '<div class="box teal" style="margin-bottom:10px"><span class="num">3</span><b>Scan (2 min)</b> Move attention from head to toes. Notice tension. Soften where you can.</div>' +
        '<div class="box tint" style="margin-bottom:10px"><span class="num">4</span><b>Ground (1 min)</b> Name 5 things you see, 4 you feel, 3 you hear, 2 you smell, 1 you taste.</div>' +
        '<div class="box teal" style="margin-bottom:10px"><span class="num">5</span><b>Return (30 sec)</b> Take a deep breath. Choose one kind thing to do next.</div>' +
        '<div class="box sand"><b>If your mind wanders:</b> that is normal. Gently bring it back. Practice is the point.<br><b>If this feels uncomfortable:</b> open your eyes, look around, and stop. Mindfulness should not be forced. If memories or sensations feel overwhelming, consider talking with a counselor.</div>' + field('After: I noticed…', 4), 'The Adult Wellness Toolkit'))

    P.append(page('Stress &amp; Self-Reflection Journal', 'A few minutes of writing can untangle a lot. Use it daily or weekly.',
        field('Today / this week I felt…', 2) + field('What triggered stress?', 3) + field('How did I respond? Was it how I wanted to?', 3) +
        field('What did I need that I did not get?', 2) + field('One thing I handled well', 2) + field('Something I want to do differently', 2) + field('One thing I am grateful for', 2) +
        '<div class="box teal" style="margin-top:10px"><b>Reflect with kindness.</b> Ask: "What would I say to a friend in this situation?"</div>', 'The Adult Wellness Toolkit'))
    return P

KITS = {'feelings-toolkit': feelings, 'parent-toolkit': parent, 'teen-toolkit': teen, 'adult-wellness-toolkit': adult}

if __name__ == '__main__':
    os.makedirs(OUT, exist_ok=True)
    for name, fn in KITS.items():
        html = f'<!doctype html><meta charset="utf-8"><title>{name}</title><style>{CSS}</style><body>' + ''.join(fn()) + '</body>'
        with tempfile.NamedTemporaryFile('w', suffix='.html', delete=False) as t:
            t.write(html); p = t.name
        pdf = os.path.abspath(os.path.join(OUT, name + '.pdf'))
        subprocess.run([CHROME, '--headless=new', '--disable-gpu', '--no-pdf-header-footer', f'--print-to-pdf={pdf}', 'file://' + p], capture_output=True)
        os.unlink(p)
        print(name, os.path.getsize(pdf) // 1024, 'KB')
