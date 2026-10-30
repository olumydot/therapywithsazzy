from rlib import *

K = 'feelings'
A = 'Ages 4–12'
WS, ACT, REF = 'Printable worksheet', 'Activity', 'Self-reflection'
RES = []

# 1 ------------------------------------------------------------ My Feelings Chart
feels = ['Happy', 'Sad', 'Angry', 'Worried', 'Frustrated', 'Excited', 'Confused']
cells = [F(n, extra='<div class="small" style="margin-top:2px">I feel this when…</div><div class="line" style="height:20px"></div><div class="line" style="height:20px"></div>') for n in feels]
cells.append(f'<div class="face">{blank_face()}<b>My own feeling</b><div class="small">Draw it and name it</div><div class="line" style="height:20px"></div></div>')
RES.append(R(K, 'my-feelings-chart', 'My Feelings Chart', 'Ages 4–10', WS, ['emotional-regulation'], 'Identifying happy, sad, angry, worried, frustrated, excited, and confused',
    Fsvg('Happy'), 'Feelings have names. When we can name a feeling, it gets easier to handle. This chart shows seven common feelings.',
    ['Look at each face and say its name out loud.', 'Finish the sentence: "I feel this when…"', 'Color the faces that you felt today.'],
    '"I feel <b>worried</b> when I have a test. I feel <b>excited</b> when it is my birthday."',
    grid(4, cells, 10) + '<div style="margin-top:12px" class="box sb"><span class="lab">Today I felt: </span>&nbsp;&nbsp;<span class="small">(circle the faces above)</span><div class="small" style="margin-top:4px">All feelings are okay. Feelings come and go, like weather.</div></div>', start=True))

# 2 ------------------------------------------------------------ Thermometer
lv = [('5', 'Huge', 'I might explode, scream, or run away.', '#e8806a'), ('4', 'Big', 'My body feels hot or tight. It is hard to think.', '#f2a96b'), ('3', 'Medium', 'I feel it a lot. I need to do something.', '#f5d58a'), ('2', 'Small', 'I notice it a little.', '#c3e29c'), ('1', 'Tiny', 'Calm and okay.', '#8fd3c8')]
rows = ''.join(f'<div class="row" style="margin-bottom:8px;align-items:stretch"><div style="width:.8in;background:{c};border-radius:12px;display:grid;place-items:center;text-align:center"><div><div style="font:600 22pt Fr,serif;color:#0F2A4A;line-height:1">{n}</div><b style="font-size:9pt">{t}</b></div></div><div class="box" style="flex:1"><div class="small" style="margin-bottom:2px">{d}</div><span class="lab">What helps me: </span><div class="line" style="height:20px"></div></div></div>' for n, t, d, c in lv)
RES.append(R(K, 'feelings-thermometer', 'Feelings Thermometer', 'Ages 5–12', WS, ['emotional-regulation', 'anger'], 'Understanding how big a feeling is, from 1 to 5',
    thermometer('1in'), 'Feelings come in different sizes. A small feeling needs a small tool. A big feeling needs a big tool and a break.',
    ['Think of a feeling you had today.', 'Point to how big it was on the thermometer.', 'Write what helps at each level.'],
    '"My mad was a <b>4</b>. When I am a 4, I take a break and squeeze a pillow."',
    f'<div class="row" style="align-items:flex-start;gap:14px"><div style="width:1.1in;flex:none">{thermometer("1.1in")}</div><div style="flex:1">{rows}</div></div><div class="box sb" style="margin-top:8px"><span class="lab">Right now my feeling is a ____ . </span> <span class="lab">The feeling is: ______________</span></div>', start=False))

# 3 ------------------------------------------------------------ Where do I feel it
key = [('Angry', '#E8806A'), ('Worried', '#6a8fd6'), ('Sad', '#9a7bc4'), ('Happy', '#f2c14a'), ('Excited', '#f2a96b'), ('Calm', '#6CC4BC')]
kh = ''.join(f'<div class="row" style="margin-bottom:6px"><span style="width:22px;height:22px;border-radius:50%;background:{c};border:2px solid #16243a;display:inline-block"></span><b>{n}</b></div>' for n, c in key)
RES.append(R(K, 'where-do-i-feel-it', 'Where Do I Feel It?', 'Ages 4–12', ACT, ['emotional-regulation'], 'Recognizing how emotions show up in the body',
    body_outline('.8in'), 'Feelings live in our bodies, too. Tight tummy? Hot face? Fast heart? These are clues that tell us how we feel.',
    ['Pick a color for each feeling in the key.', 'Think of a time you felt that feeling.', 'Color the body where you felt it.'],
    '"When I\'m nervous, my tummy gets fluttery, so I color it blue."',
    f'<div class="row" style="align-items:flex-start;gap:16px"><div style="width:1.9in" class="box sb"><div class="lab" style="margin-bottom:6px">Color key</div>{kh}<div class="small" style="margin-top:8px">Make up your own colors for other feelings!</div></div><div class="center" style="flex:1">{body_outline("2.5in")}</div><div style="width:1.9in"><div class="box wb" style="margin-bottom:8px"><b>Clues:</b>{bl(["Fast heartbeat", "Tight tummy", "Hot face", "Shaky hands", "Heavy chest", "Wiggly legs"])}</div><div class="box"><div class="lab">My body tells me I am angry when…</div>{lines(3, 22)}</div></div></div>'))

# 4 ------------------------------------------------------------ Calm-down menu
cats = [('Breathe', '#e6f4f1', ['Smell the flower, blow the candle', 'Belly breaths', 'Five-finger breathing']), ('Move', '#fbf0d4', ['Jumping jacks', 'Wall push-ups', 'Stretch like a cat', 'Dance it out']),
        ('Senses', '#fde9e3', ['Hold a cool cloth', 'Squeeze a stress ball', 'Look at a calm jar', 'Listen to soft music']), ('Connect', '#e4eaf6', ['Ask for a hug', 'Talk to a safe person', 'Cuddle a pet or toy']), ('Create', '#ebe7f5', ['Draw or color', 'Build with blocks', 'Write a note'])]
mc = ''.join(f'<div class="box" style="background:{c};border-color:transparent"><div class="lab" style="margin-bottom:3px;font-size:12pt">{n}</div>{cbs(i)}<div class="line" style="height:20px"></div><div class="small">Add your own</div></div>' for n, c, i in cats)
RES.append(R(K, 'my-calm-down-menu', 'My Calm-Down Menu', 'Ages 4–12', WS, ['emotional-regulation', 'anger'], 'Choosing healthy ways to calm your body and mind',
    toolbox('1.2in'), 'A menu lets you choose. This menu is full of calm-down ideas. You pick the ones that work for you.',
    ['Try each idea when you are calm.', 'Check the ones you like.', 'Star your top 3 favorites.'],
    '"When I\'m mad, I pick from my menu: 3 belly breaths, then draw."',
    grid(2, [mc.split('</div></div>')[0] + '</div></div>'] if False else [], 0) + f'<div class="grid g2" style="gap:10px">{mc}<div class="box wb center" style="display:grid;place-items:center"><div><div class="stick">My top 3</div><div style="margin-top:6px;font-size:12pt">★ ___________________<br>★ ___________________<br>★ ___________________</div></div></div></div>', start=True))

# 5 ------------------------------------------------------------ Anger detective
steps = [('Clue 1: The Trigger', 'What happened right before I got mad?', 2), ('Clue 2: My Body', 'What did my body feel? (hot face, tight fists…)', 2), ('Clue 3: What I Did', 'What did I say or do?', 2), ('Clue 4: What Happened Next', 'How did it turn out?', 2)]
cl = ''.join(f'<div class="box {c}"><span class="stick">{t}</span><div class="small" style="margin:3px 0">{q}</div>{lines(n, 22)}</div>' for (t, q, n), c in zip(steps, ['coral', 'sand', 'teal', 'blue']))
RES.append(R(K, 'the-anger-detective', 'The Anger Detective', 'Ages 7–12', ACT, ['anger', 'emotional-regulation'], 'Identifying triggers and reactions',
    magnifier_ill('1.2in'), 'Anger is not bad. It is a clue that something is wrong or unfair. Detectives investigate before they act.',
    ['Pick a time you got angry.', 'Look for each clue and write what you find.', 'Solve the case: plan what to try next time.'],
    '"Trigger: my brother grabbed my toy. Body: hot face. I did: yelled. Next time: I\'ll say, \'Please ask first.\'"',
    f'<div class="grid g2" style="gap:10px">{cl}</div><div class="box wb" style="margin-top:10px"><span class="stick">Case solved</span><div class="lab" style="margin-top:4px">Next time I get mad, I will…</div>{lines(2, 22)}</div>'))

# 6 ------------------------------------------------------------ Stop think choose
lights = [('#e8806a', 'STOP', 'Freeze. Hands still. Take 1 deep breath.'), ('#f5d58a', 'THINK', 'What could happen if I do this? Is there another way?'), ('#8fd3c8', 'CHOOSE', 'Pick the choice that keeps everyone safe and feels okay later.')]
lt = ''.join(f'<div class="row" style="margin-bottom:8px;align-items:stretch"><div style="width:.95in;background:{c};border-radius:14px;display:grid;place-items:center;font:700 13pt Arial;color:#16243a">{t}</div><div class="box" style="flex:1"><div style="font-size:11pt">{d}</div>{lines(1, 22)}</div></div>' for c, t, d in lights)
RES.append(R(K, 'stop-think-choose', 'Stop, Think, Choose', 'Ages 5–12', WS, ['emotional-regulation', 'anger'], 'Learning impulse control',
    stop_ill('1.2in'), 'When feelings are big, our body wants to act fast. This tool helps you pause so you can choose what to do.',
    ['Practice the 3 steps when you are calm.', 'Read each pretend situation.', 'Write or draw your best choice.'],
    '"Someone cut in line. I <b>stopped</b>, <b>thought</b> about it, and <b>chose</b> to tell the teacher."',
    lt + '<h2>Practice</h2>' + grid(2, [box(f'<b>{s}</b>' + lines(2, 22)) for s in ['A friend takes my pencil without asking.', 'I lose a game I wanted to win.', 'I feel left out at recess.', 'My little sibling knocks over my tower.']], 8)))

# 7 ------------------------------------------------------------ Worry monster
RES.append(R(K, 'my-worry-monster', 'My Worry Monster', 'Ages 4–10', ACT, ['anxiety', 'emotional-regulation'], 'Externalizing and managing worries',
    monster('1.2in'), 'Worries can feel huge in our heads. Putting them outside, onto a monster, makes them smaller and easier to talk about.',
    ['Name your worry monster.', 'Write or draw your worries in its tummy.', 'Choose one thing that can make a worry smaller.'],
    '"My monster is Wiggles. His worry is: \'What if no one plays with me?\'"',
    f'<div class="row" style="align-items:flex-start;gap:16px"><div class="center" style="width:2.3in">{monster("2.2in", 3)}<div class="lab">My monster\'s name: ________</div></div><div style="flex:1"><div class="box sb" style="height:1.55in;margin-bottom:8px"><div class="lab">Worries in the monster\'s tummy</div><div class="small">Write or draw them here.</div></div>' + grid(2, [box('<div class="lab">Is my worry about…</div><div style="font-size:10.5pt;margin-top:3px">☐ Now ☐ Later ☐ Maybe never</div>'), box('<div class="lab">What would I tell a friend?</div>' + lines(2, 20))], 8) + '<div class="box wb" style="margin-top:8px"><div class="lab">To make the worry smaller I can…</div>' + cbs(['Take 3 slow breaths', 'Tell a safe person', 'Draw it, then fold it up', 'Do something fun']) + '</div></div></div>', start=False))

# 8 ------------------------------------------------------------ What can I control
RES.append(R(K, 'what-can-i-control', 'What Can I Control?', 'Ages 6–12', WS, ['anxiety', 'emotional-regulation'], 'Separating controllable and uncontrollable situations',
    circles_control('1.3in'), 'Some things are up to us. Some are not. When we focus on what we can control, worry gets lighter.',
    ['Read each item.', 'Write it in the right circle or list.', 'Pick one thing you can do today.'],
    '"I can\'t control the <b>weather</b>, but I can control if I bring a <b>raincoat</b>."',
    f'<div class="row" style="align-items:flex-start;gap:14px"><div class="center" style="width:2.8in">{circles_control("2.7in")}</div><div style="flex:1">' + grid(1, [box('<span class="stick">Sort these</span><div style="margin-top:5px">' + pills(['My effort', 'The weather', 'What others say', 'How I react', 'The past', 'My words', 'Other people\'s feelings', 'Who I ask for help']) + '</div>', 'sb')], 6) + '<div class="box teal" style="margin-top:8px"><div class="lab">I CAN control:</div>' + lines(2, 21) + '</div><div class="box coral" style="margin-top:8px"><div class="lab">I CAN\'T control:</div>' + lines(2, 21) + '</div></div></div><div class="box wb" style="margin-top:10px"><div class="lab">One thing I can do today about something that worries me:</div>' + lines(1, 22) + '</div>'))

# 9 ------------------------------------------------------------ Strengths
st = ['Kind', 'Brave', 'Funny', 'Creative', 'Helpful', 'A good listener', 'Curious', 'Strong', 'Honest', 'Patient', 'Good at sharing', 'A good friend', 'Hard working', 'Caring', 'Smart', 'A problem solver']
RES.append(R(K, 'my-personal-strengths', 'My Personal Strengths', 'Ages 5–12', WS, ['confidence'], 'Building confidence and self-esteem',
    hero_badge('1.1in'), 'Everybody has strengths. Noticing yours helps you feel proud and ready for hard things.',
    ['Circle every strength that sounds like you.', 'Ask someone who knows you well to add one.', 'Write about a time you used a strength.'],
    '"I am <b>kind</b>. I helped my friend when she fell."',
    f'<div class="row" style="align-items:flex-start;gap:14px"><div style="flex:1"><div class="lab" style="margin-bottom:5px">Circle your strengths</div><div>{pills(st)}</div></div><div class="center" style="width:1.8in">{hero_badge("1.7in")}<div class="lab" style="margin-top:2px">I am a ____ hero!</div></div></div>' + grid(2, [box('<div class="lab">Someone told me I\'m…</div>' + lines(2, 22), 'sb'), box('<div class="lab">A time I used my strength…</div>' + lines(2, 22), 'sb')], 10, 'margin-top:10px') + '<div class="box wb" style="margin-top:10px"><div class="lab">Something I\'m proud of:</div>' + lines(2, 22) + '</div>'))

# 10 ------------------------------------------------------------ Safe people
fing = ''.join(f'<div class="box" style="text-align:center;{"background:#fde9e3" if i%2==0 else "background:#e6f4f1"};border-color:transparent"><div style="font:600 20pt Fr,serif;color:#a8432d">{i+1}</div><div class="lab">Name</div>{lines(1, 22)}<div class="small" style="margin-top:6px">How they help me</div>{lines(2, 20)}</div>' for i in range(5))
RES.append(R(K, 'my-safe-people', 'My Safe People', 'Ages 4–12', WS, ['relationships', 'emotional-regulation'], 'Identifying trusted adults and support systems',
    people_ill('1.3in', '#E8806A'), 'A safe person listens, helps, and keeps you safe. It is always okay to ask for help.',
    ['Think of 5 grown-ups you trust.', 'Write one name on each finger.', 'Share your hand with a parent or teacher.'],
    '"1. Mom. 2. Grandpa. 3. Ms. Lee at school. 4. Coach. 5. Auntie."',
    f'<div class="grid g5" style="gap:8px">{fing}</div>' + grid(3, [box('<div class="lab">At home</div>' + lines(2, 22), 'teal'), box('<div class="lab">At school</div>' + lines(2, 22), 'sand'), box('<div class="lab">In my community</div>' + lines(2, 22), 'blue')], 10, 'margin-top:10px') + '<div class="box coral" style="margin-top:10px"><b>If I feel unsafe or someone hurts me,</b> I tell a safe person right away. It is never my fault, and I will not get in trouble for telling.</div>'))

# ======================================================== Interactive activities
RES.append(R(K, 'superhero-coping-strategy', 'Design Your Superhero Coping Strategy', 'Ages 5–12', ACT, ['emotional-regulation', 'confidence'], 'Turning a coping skill into a superpower',
    hero_badge('1.2in', '#4F6FB5'), 'Superheroes have powers. Your coping skills are your superpowers! Design a hero who uses one.',
    ['Pick a coping skill (like deep breathing).', 'Give it a hero name and a costume.', 'Decide when your hero swoops in.'],
    '"Captain Calm uses the Super Breath to fix big feelings!"',
    f'<div class="row" style="align-items:flex-start;gap:14px"><div class="box sb center" style="width:3in;height:3.8in"><div class="lab">Draw your hero</div><div style="margin-top:6px;opacity:.8">{hero_badge("1.8in")}</div></div><div style="flex:1">{field("Hero name", 1, 24)}{field("Superpower (my coping skill)", 2, 24)}{field("My hero swoops in when I feel…", 2, 24)}{field("Hero catchphrase", 1, 24)}</div></div>', group='activities'))

RES.append(R(K, 'draw-what-anger-looks-like', 'Draw What Anger Looks Like', 'Ages 4–12', ACT, ['anger', 'emotional-regulation'], 'Expressing anger safely through art',
    pencil_ill('1.2in'), 'Sometimes feelings are easier to draw than to say. Make anger visible, then watch it change.',
    ['Draw what your anger looks like: color, shape, size.', 'Add a sound and a feeling in your body.', 'Draw it again, smaller or calmer.'],
    '"My anger is a big red spiky ball. When I breathe, it turns into a small blue circle."',
    grid(2, [f'<div class="box coral" style="height:3.3in"><span class="stick">My anger looks like…</span></div>', f'<div class="box teal" style="height:3.3in"><span class="stick">My anger after I calm down…</span></div>'], 10) + grid(3, [box('<div class="lab">Color</div>' + lines(1, 22)), box('<div class="lab">Sound</div>' + lines(1, 22)), box('<div class="lab">What it needs</div>' + lines(1, 22))], 10, 'margin-top:10px'), group='activities'))

wd = ['Worried', 'Happy', 'Angry', 'Sad', 'Excited', 'Confused']
import random
mix = wd[3:] + wd[:3]
RES.append(R(K, 'match-emotions-to-faces', 'Match Emotions to Faces', 'Ages 4–8', ACT, ['emotional-regulation'], 'Matching feelings words to facial expressions',
    Fsvg('Excited'), 'Faces give us clues about feelings. Matching faces to words builds feelings detective skills.',
    ['Look at each face.', 'Draw a line to the matching feeling word.', 'Make each face yourself in a mirror.'],
    '"Eyebrows down and a frown? That face matches <b>angry</b>."',
    f'<div class="row" style="justify-content:space-between;align-items:center;padding:0 .3in"><div class="grid" style="gap:10px;width:1.4in">' + ''.join(f'<div class="center">{face(*FACE_DEF[n]).replace("<svg", "<svg style=\'width:.78in;height:.78in\'")}</div>' for n in wd) + '</div><div style="flex:1"></div><div class="grid" style="gap:10px;width:1.9in">' + ''.join(f'<div class="box center" style="height:.78in;display:grid;place-items:center;font:700 14pt Arial;color:#16243a;background:#fde9e3">{n}</div>' for n in mix) + '</div></div>' + '<div class="box sb" style="margin-top:12px"><span class="lab">Make your own face! </span><span class="small">Draw a face for how you feel today and name it.</span><div style="height:.9in"></div></div>', group='activities'))

RES.append(R(K, 'create-a-calm-down-corner', 'Create a Calm-Down Corner', 'Ages 4–12', ACT, ['emotional-regulation'], 'Designing a safe space to regulate',
    sun_ill('1.2in', '#6CC4BC'), 'A calm-down corner is a cozy place to go when feelings get big. It is not a punishment. It is a reset.',
    ['Pick a quiet corner with a grown-up.', 'Choose items from the list.', 'Draw how your corner will look.'],
    '"My corner has a beanbag, a stuffed owl, headphones, and my calm cards."',
    grid(2, [box('<div class="lab">Items to include</div>' + cbs(['Soft pillow or beanbag', 'Stuffed animal', 'Calm-down cards', 'Feelings chart', 'Coloring and paper', 'Stress ball or putty', 'Calm jar', 'Soft blanket', 'Headphones', 'Book']), 'teal'), box('<div class="lab">Our corner rules</div>' + cbs(['I can go there when I need to.', 'I can stay until I feel ready.', 'I can ask a grown-up to sit with me.', 'We never use it as punishment.']) + '<div class="lab" style="margin-top:8px">Our rule ideas:</div>' + lines(2, 22), 'sand')], 10) + '<div class="box sb" style="margin-top:10px;height:2.3in"><span class="stick">Draw my calm-down corner</span></div>', group='activities'))

RES.append(R(K, 'five-finger-breathing', 'Five-Finger Breathing', 'Ages 4–12', ACT, ['emotional-regulation', 'anxiety'], 'Practicing slow breathing with a visual guide',
    lungs_ill('1.2in'), 'You always have your hand with you. Tracing it while you breathe slows your body down.',
    ['Hold up one hand, fingers spread.', 'Trace up each finger as you breathe in.', 'Trace down as you breathe out. Do all five fingers.'],
    '"Slide up the thumb: breathe in. Slide down: breathe out."',
    f'<div class="row" style="align-items:center;gap:20px"><div class="center" style="width:3.3in">{hand("3.2in")}</div><div style="flex:1"><div class="box teal" style="margin-bottom:8px"><span class="num">1</span><b>Up the thumb</b><div class="small">Breathe in through your nose</div></div><div class="box tint" style="margin-bottom:8px"><span class="num">2</span><b>Down the thumb</b><div class="small">Breathe out slowly, like blowing bubbles</div></div><div class="box teal" style="margin-bottom:8px"><span class="num">3</span><b>Keep going</b><div class="small">Do the pointer, middle, ring, and pinky</div></div><div class="box coral"><span class="num">5</span><b>Do it again</b><div class="small">One more time if you need it</div></div></div></div>' + '<div class="box sb" style="margin-top:12px"><span class="lab">After breathing, I feel: </span>' + ' ☐ calmer ☐ the same ☐ sleepy ☐ ready to try again</div>', group='activities'))

drawers = [('Body tool', 'Something I do with my body'), ('Brain tool', 'A helpful thought I can say'), ('Heart tool', 'A feeling I can name'), ('Helper tool', 'A person I can ask'), ('Fun tool', 'Something fun that helps me reset')]
RES.append(R(K, 'emotional-regulation-toolbox', 'Build Your Own Emotional Regulation Toolbox', 'Ages 5–12', ACT, ['emotional-regulation'], 'Collecting your own calming strategies',
    toolbox('1.3in'), 'Every builder has a toolbox. Fill yours with strategies that work for you.',
    ['Think of one tool for each drawer.', 'Write or draw it.', 'Practice a tool when you feel just a little upset.'],
    '"Body tool: jumping jacks. Brain tool: \'I can do hard things.\' Helper tool: Dad."',
    f'<div class="center" style="margin-bottom:8px">{toolbox("1.6in")}</div>' + ''.join(f'<div class="row" style="margin-bottom:7px"><span class="num" style="width:26px;height:26px">{i+1}</span><div class="box {c}" style="flex:1"><span class="lab">{t}</span> <span class="small">· {d}</span>{lines(1, 22)}</div></div>' for i, ((t, d), c) in enumerate(zip(drawers, ['coral', 'teal', 'sand', 'blue', 'lilac']))) + '<div class="box wb center" style="margin-top:8px"><b>Your toolbox is ready!</b> Keep this page where you can find it.</div>', start=True, group='activities'))
