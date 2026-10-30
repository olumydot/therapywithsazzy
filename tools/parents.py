from rlib import *

K = 'parent'
WS, GD, ACT, REF = 'Printable worksheet', 'Educational guide', 'Activity', 'Self-reflection'
RES = []
P = 'Parents & caregivers'


def numbox(n, title, text, cls='tint'):
    return f'<div class="box {cls}" style="margin-bottom:7px;display:flex;gap:8px;align-items:flex-start"><span class="num">{n}</span><div><b>{title}</b><div style="font-size:10.5pt;line-height:1.35">{text}</div></div></div>'

# 1 ------------------------------------------------------------------ triggers
trig = ['Hunger or thirst', 'Tiredness', 'Transitions', 'Being told "no"', 'Hard tasks or homework', 'Loud or busy places', 'Waiting', 'Screen-time ending', 'Sibling conflict', 'Changes in routine', 'Feeling left out', 'Separation from caregiver']
RES.append(R(K, 'understanding-my-childs-triggers', "Understanding My Child's Triggers", 'Ages 3–12', WS, ['parenting', 'emotional-regulation'], 'Recognizing patterns behind behavior',
    magnifier_ill('1.2in', '#E0A93B'), 'A trigger is something that makes a hard moment more likely. When you spot patterns, you can prepare instead of react.',
    ['Check the triggers you have noticed.', 'Pick the top three.', 'Plan one change for each.'],
    '"Trigger: leaving the park. Early sign: whining. Plan: a 5-minute warning and a countdown."',
    f'<div class="grid g2" style="gap:8px"><div class="box tint"><div class="lab">Common triggers (check any)</div>{cbs(trig)}</div><div>' + box('<div class="lab">Early warning signs I notice</div>' + lines(3, 22), 'sand') + '<div style="height:8px"></div>' + box('<div class="lab">What usually helps</div>' + lines(3, 22), 'teal') + '</div></div>' +
    tbl(['Top trigger', 'What I will try before it happens'], [['1.', ''], ['2.', ''], ['3.', '']], 36) + '<div class="small" style="margin-top:6px"><i>Behavior is communication. Ask: what might my child be trying to tell me?</i></div>', start=False))

# 2 ------------------------------------------------------------------ ABC
RES.append(R(K, 'behavior-abc-tracker', 'Behavior ABC Tracker', 'Ages 3–12', WS, ['parenting', 'anger'], 'Antecedent, Behavior, Consequence',
    clock_ill('1.2in'), 'ABC tracking shows what happens before (A), during (B), and after (C) a behavior, so patterns become clear.',
    ['Write it down soon after, in plain facts.', 'Fill in A, B, and C for each event.', 'After a week, look for patterns.'],
    '"A: asked to stop tablet. B: screamed and threw the remote. C: I gave 10 more minutes."',
    '<div class="grid g3" style="gap:6px;margin-bottom:6px"><div class="box coral center"><b>A</b> · Antecedent<div class="small">What happened right before?</div></div><div class="box sand center"><b>B</b> · Behavior<div class="small">What did I see and hear?</div></div><div class="box teal center"><b>C</b> · Consequence<div class="small">What happened right after?</div></div></div>' +
    tbl(['Date / time', 'A: Before', 'B: Behavior', 'C: After'], [['', '', '', '']] * 6, 54) +
    '<div class="box wb" style="margin-top:8px"><div class="lab">Patterns I notice (time of day, place, people, tasks):</div>' + lines(2, 22) + '</div>', start=True))

# 3 ------------------------------------------------------------------ reinforcement
RES.append(R(K, 'positive-reinforcement-planner', 'Positive Reinforcement Planner', 'Ages 3–12', WS, ['parenting', 'confidence'], 'Encouraging desired behaviors',
    star_ill('1.2in'), 'What we notice and celebrate grows. Specific praise and small rewards help new skills stick.',
    ['Pick one skill to build.', 'Plan your praise and a small reward.', 'Track it for a week and celebrate effort.'],
    '"You put your shoes on by yourself. Great job getting ready!"',
    field('Skill we are building (specific and observable)', 1, 24) + field('What it looks like when they do it', 2, 22) +
    grid(2, [box('<div class="lab">Specific praise I can use</div>' + lines(3, 22) + '<div class="small">"You took a breath when you felt mad."</div>', 'teal'), box('<div class="lab">Rewards (small and soon)</div>' + lines(3, 22) + '<div class="small">Time together, game choice, sticker.</div>', 'coral')], 10, 'margin:6px 0') +
    '<div class="lab">Weekly tracker</div>' + tbl(['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun'], [[''] * 7], 44) + '<div class="box sand" style="margin-top:8px"><b>Tips:</b> Reinforce right away. Notice effort, not only results. Aim for more praise than corrections. Connection is the best reward.</div>', start=True))

# 4 ------------------------------------------------------------------ boundaries
RES.append(R(K, 'setting-healthy-boundaries', 'Setting Healthy Boundaries', 'Ages 3–12', GD, ['parenting', 'relationships'], 'Establishing consistent expectations',
    shield_ill('1.2in', '#E0A93B'), 'Boundaries are the safe edges that help children feel secure. They work best when they are calm, clear, and consistent.',
    ['Choose 3 to 5 important rules.', 'Say them in a short, positive way.', 'Decide in advance how you will follow through.'],
    '"Rule: We use gentle hands. If someone hits, we stop the game and take a break."',
    grid(3, [box('<div class="center"><span class="stick">Calm</span></div><div style="font-size:10.5pt;margin-top:4px">Lower your voice. Your calm helps your child borrow calm.</div>', 'teal'), box('<div class="center"><span class="stick">Clear</span></div><div style="font-size:10.5pt;margin-top:4px">Short, specific, and positive: "Feet on the floor."</div>', 'sand'), box('<div class="center"><span class="stick">Consistent</span></div><div style="font-size:10.5pt;margin-top:4px">Follow through the same way each time, kindly.</div>', 'blue')], 8) +
    '<h2>Our household rules</h2>' + tbl(['Rule (positive wording)', 'Why it matters', 'What happens if it is not followed'], [['', '', '']] * 4, 44) +
    grid(2, [say('<b>Try saying:</b> "I won\'t let you hit. I\'ll help you stop."'), warn('<b>Avoid:</b> threats you cannot keep, long lectures in the heat of the moment.')], 10, 'margin-top:8px')))

# 5 ------------------------------------------------------------------ outbursts
ph = [('Before', 'Prevent', ['Know the triggers', 'Give a warning', 'Offer a choice'], 'teal'), ('During', 'Stay steady', ['Keep everyone safe', 'Few words, calm voice', 'Do not negotiate'], 'coral'), ('After', 'Reconnect', ['Wait until calm', 'Name the feeling', 'Plan a try-again'], 'blue')]
RES.append(R(K, 'managing-emotional-outbursts', 'Managing Emotional Outbursts', 'Ages 3–12', GD, ['parenting', 'anger', 'emotional-regulation'], 'Responding to dysregulation',
    dial_ill('1.3in'), 'During a meltdown, a child\'s thinking brain goes offline. Your job is to keep things safe and calm, not to teach in the moment.',
    ['Use the Before, During, and After plan.', 'Practice your calm phrase.', 'Review what worked.'],
    '"You\'re really upset. I\'m here. I\'ll stay close until you\'re ready."',
    grid(3, [box(f'<div class="center"><span class="stick">{t}</span><div class="lab" style="margin-top:3px">{s}</div></div>' + bl(i), c) for t, s, i, c in ph], 8) +
    grid(2, [say('<b>Calm phrases:</b><br>"I\'m right here."<br>"Big feelings are okay. Hitting is not."<br>"We can talk when your body is calm."'), warn('<b>Skip in the moment:</b> arguing, bargaining, shaming, lecturing, taking away things unrelated to the behavior.')], 10, 'margin-top:8px') +
    box('<div class="lab">My calm plan</div><div class="small">The first thing I will do:</div>' + lines(1, 22) + '<div class="small">A phrase I will say:</div>' + lines(1, 22) + '<div class="small">How I will calm myself:</div>' + lines(1, 22), 'sand', 'margin-top:8px') +
    '<div class="warn" style="margin-top:8px"><b>Safety first.</b> If anyone is at risk of harm, or outbursts are frequent, intense, or getting worse, contact your child\'s pediatrician or a licensed professional.</div>', start=True))

# 6 ------------------------------------------------------------------ communication
RES.append(R(K, 'parent-child-communication-guide', 'Parent-Child Communication Guide', 'Ages 3–18', GD, ['parenting', 'relationships'], 'Listening and responding effectively',
    chat_ill('1.2in', '#E0A93B'), 'Children open up when they feel heard. Small changes in how we listen and respond make a big difference.',
    ['Practice the four listening steps.', 'Swap one "instead of" phrase this week.', 'Notice how your child responds.'],
    '"Instead of \'Stop crying!\' try \'You\'re really sad. Tell me about it.\'"',
    grid(4, [box(f'<div class="center"><span class="num" style="margin:0">{i+1}</span><div class="lab" style="margin-top:3px">{t}</div><div class="small">{d}</div></div>', c) for i, (t, d, c) in enumerate([('Stop', 'Put the phone down', 'teal'), ('Look', 'Eye level, open face', 'sand'), ('Listen', 'Do not fix or interrupt', 'blue'), ('Reflect', '"It sounds like…"', 'coral')])], 8) +
    '<h2>Instead of… try…</h2>' + tbl(['Instead of', 'Try'], [['"Stop crying."', '"It\'s okay to feel sad. I\'m here."'], ['"You\'re fine."', '"That seemed scary. What was it like?"'], ['"Because I said so."', '"Here\'s the reason. I know it\'s hard."'], ['"Why did you do that?"', '"What happened? What were you needing?"'], ['', '']], 30) +
    '<div class="box wb" style="margin-top:8px"><div class="lab">One phrase I will practice this week:</div>' + lines(2, 22) + '</div>'))

# 7 ------------------------------------------------------------------ visual routine
stp = ''.join(f'<div class="box tint center" style="padding:6px"><div class="num" style="margin:0 auto 3px">{i}</div><div class="box teal" style="height:.75in;margin:3px 0"><span class="small">picture</span></div><div class="line" style="height:20px"></div><i class="cb" style="margin:4px 0 0"></i></div>' for i in range(1, 7))
RES.append(R(K, 'creating-a-visual-routine', 'Creating a Visual Routine', 'Ages 3–10', ACT, ['parenting', 'emotional-regulation'], 'Building structure and predictability',
    calendar_ill('1.2in', '#E0A93B'), 'Pictures and steps make routines predictable. Predictable days lower stress and reduce arguments.',
    ['Pick one routine (morning, after school, bedtime).', 'Draw or paste a picture for each step.', 'Let your child check off each step.'],
    '"Morning: 1 wake up, 2 get dressed, 3 breakfast, 4 brush teeth, 5 shoes, 6 backpack."',
    '<div class="lab" style="margin-bottom:6px">Routine: ☐ Morning &nbsp; ☐ After school &nbsp; ☐ Bedtime &nbsp; ☐ Other: ________</div>' + f'<div class="grid g3" style="gap:8px">{stp}</div>' +
    '<div class="box sand" style="margin-top:10px"><b>Tips:</b> Keep it to 4–6 steps. Use real photos for younger children. Review it together when calm. Celebrate effort ("You did steps 1 to 4!"). Give a warning before changes.</div>'))

# 8 ------------------------------------------------------------------ consequences vs punishment
RES.append(R(K, 'consequences-vs-punishment', 'Consequences vs. Punishment', 'Ages 3–12', GD, ['parenting'], 'Understanding effective discipline',
    brain_ill('1.2in', '#E0A93B'), 'Discipline means teaching. Consequences teach a skill. Punishment aims to make a child feel bad, and often teaches fear instead.',
    ['Compare the two columns.', 'Rewrite one punishment as a consequence.', 'Use the checklist before you respond.'],
    '"Punishment: \'No dessert for a week!\' Consequence: \'You wrote on the wall, so we\'ll clean it together.\'"',
    '<div class="grid g2" style="gap:10px"><div class="box coral"><span class="stick" style="background:#c9604a">Punishment</span>' + bl(['Often harsh or unrelated', 'Comes from anger', 'Focuses on blame', 'Can create fear or shame']) + '</div><div class="box teal"><span class="stick" style="background:#1f7a74">Consequence</span>' + bl(['Related to the behavior', 'Calm and predictable', 'Focuses on learning', 'Builds responsibility']) + '</div></div>' +
    '<div class="box wb" style="margin-top:10px"><div class="lab">Check before you respond</div>' + cbs(['Is it related to what happened?', 'Is it respectful and calm?', 'Is it something I can follow through on?', 'Will it help my child learn a skill?']) + '</div>' +
    tbl(['A behavior I want to change', 'Related, calm consequence', 'Skill I want to teach'], [['', '', '']] * 3, 44)))

# 9 ------------------------------------------------------------------ ADHD
adhd = [('Time', 'Visual timers, countdowns, and clocks they can see.'), ('Getting started', 'Break tasks into tiny steps. Start together for the first 2 minutes.'), ('Organization', 'One home for each item. Checklists and color-coded folders.'), ('Emotions', 'Name feelings, offer breaks, and practice calm skills together.'), ('Focus', 'Reduce distractions. Short work bursts with movement breaks.'), ('Memory', 'Give one direction at a time. Write it or show it.')]
RES.append(R(K, 'adhd-parenting-guide', 'ADHD Parenting Guide', 'Ages 5–14', GD, ['parenting', 'emotional-regulation'], 'Supporting executive functioning',
    puzzle_ill('1.2in', '#E0A93B'), 'Children with ADHD often struggle with skills like planning, starting tasks, and managing emotions. These are skill gaps, not laziness or defiance.',
    ['Pick one challenge area.', 'Try a strategy for two weeks.', 'Notice strengths and celebrate them.'],
    '"Instead of \'Clean your room!\': \'Put the books on the shelf. I\'ll set a 5-minute timer.\'"',
    grid(3, [box(f'<b>{t}</b><div style="font-size:10pt;line-height:1.35">{d}</div>', c) for (t, d), c in zip(adhd, ['teal', 'sand', 'blue', 'coral', 'lilac', 'tint'])], 8) +
    grid(2, [box('<div class="lab">My child\'s strengths</div>' + lines(3, 22), 'sb'), box('<div class="lab">One challenge and my plan</div>' + lines(3, 22), 'sb')], 10, 'margin-top:8px') +
    '<div class="box wb small" style="margin-top:8px">ADHD is diagnosed by a qualified professional. This guide is general education. Talk with your child\'s pediatrician or a licensed provider about assessment and supports.</div>'))

# 10 ------------------------------------------------------------------ autism / sensory
sens = ['Sound', 'Light', 'Touch', 'Taste or smell', 'Movement']
RES.append(R(K, 'understanding-autism', 'Understanding Autism', 'Ages 3–14', GD, ['parenting', 'relationships'], 'Supporting sensory and developmental differences',
    puzzle_ill('1.2in', '#6CC4BC'), 'Autistic children may experience sensory input, communication, and routines differently. Different minds need different supports, and they are not broken.',
    ['Complete the sensory profile.', 'Add one support for each area.', 'Share it with teachers and caregivers.'],
    '"Sound: bothered by the hand dryer. Support: noise-reducing headphones in public bathrooms."',
    '<div class="lab">My child\'s sensory profile</div>' + tbl(['Sense', 'More sensitive', 'Less sensitive / seeks', 'What helps'], [[s, '☐', '☐', ''] for s in sens], 36) +
    grid(3, [box('<b>Communication supports</b>' + bl(['Visual schedules', 'Clear, literal words', 'Extra processing time']), 'teal'), box('<b>Predictability</b>' + bl(['Warn about changes', 'Use first-then', 'Keep routines']), 'sand'), box('<b>Strengths to celebrate</b>' + lines(3, 20), 'blue')], 8, 'margin-top:8px') +
    '<div class="box wb small" style="margin-top:8px">Autism is diagnosed by qualified professionals. This guide is neurodiversity-informed education, not an assessment. Support should recognize your child as an individual.</div>'))

# 11 ------------------------------------------------------------------ confidence
RES.append(R(K, 'building-your-childs-confidence', "Building Your Child's Confidence", 'Ages 4–14', GD, ['confidence', 'parenting'], 'Encouraging independence and resilience',
    plant_ill('1.2in', '#E0A93B'), 'Confidence grows when children try, struggle a little, and succeed. Our job is to support, not to rescue.',
    ['Pick one task your child can do more independently.', 'Teach it, then step back.', 'Praise effort and growth.'],
    '"You worked hard on that puzzle even when it was tricky!"',
    '<div class="lab">The independence ladder</div>' + ''.join(f'<div class="row" style="margin:3px 0 3px {i*26}px"><span class="num">{i+1}</span><div class="box tint" style="flex:1;padding:5px 10px"><b>{t}</b> <span class="small">· {d}</span></div></div>' for i, (t, d) in enumerate([('I do it for you', 'when starting'), ('I do it with you', 'side by side'), ('You do it, I watch', 'cheer and coach'), ('You do it, I check', 'small review'), ('You do it alone', 'celebrate!')])) +
    grid(2, [box('<div class="lab">Say this</div>' + bl(['"I see how hard you tried."', '"What\'s your plan?"', '"Mistakes help us grow."']), 'teal'), box('<div class="lab">Task we are practicing</div>' + lines(3, 22), 'sand')], 10, 'margin-top:8px')))

# 12 ------------------------------------------------------------------ co-parenting
RES.append(R(K, 'co-parenting-communication', 'Co-Parenting Communication', 'Parents & caregivers', GD, ['parenting', 'relationships'], "Keeping the child's needs central",
    bridge_ill('1.4in', '#E0A93B'), 'Children do best when the adults around them communicate calmly and respectfully, even if the adults disagree.',
    ['Use the B.I.F.F. rule for messages.', 'Check your message against the checklist.', 'Wait before sending if you feel upset.'],
    '"Can we agree on bedtime at 8:00 for both homes? It will help Maya sleep."',
    grid(4, [box(f'<div class="center"><div style="font:600 24pt Fr,serif;color:#7d5a0c;line-height:1">{l}</div><b>{w}</b><div class="small">{d}</div></div>', c) for l, w, d, c in [('B', 'Brief', 'Short and to the point', 'teal'), ('I', 'Informative', 'Facts, not blame', 'sand'), ('F', 'Friendly', 'Polite, neutral tone', 'blue'), ('F', 'Firm', 'Clear, no argument', 'coral')]], 8) +
    '<div class="box wb" style="margin-top:10px"><div class="lab">Before I send</div>' + cbs(['Is this about the child, not the other adult?', 'Would I be okay if my child read it?', 'Is it clear what I am asking?', 'Did I wait 10 minutes if I\'m upset?']) + '</div>' +
    '<div class="box sb" style="margin-top:10px"><div class="lab">Message planner</div><div class="small">What I need to say:</div>' + lines(2, 22) + '<div class="small">Rewritten using B.I.F.F.:</div>' + lines(3, 22) + '</div>'))

# ======================================================== practical guides
def guide(slug, title, age, ill, why, needs, steps, script, avoid, topics=('parenting',)):
    body = grid(2, [box('<div class="lab">Why this happens</div><div style="font-size:10.5pt">' + why + '</div>', 'teal'), box('<div class="lab">What your child may need</div><div style="font-size:10.5pt">' + needs + '</div>', 'sand')], 10) + \
        '<div class="lab" style="margin:10px 0 5px">Try this</div>' + ''.join(numbox(i + 1, t, d, c) for i, ((t, d), c) in enumerate(zip(steps, ['tint', 'blue', 'tint', 'blue']))) + \
        grid(2, [say('<b>Try saying:</b><br>' + script), warn('<b>Avoid:</b><br>' + avoid)], 10, 'margin-top:4px') + \
        '<div class="box wb" style="margin-top:8px"><div class="lab">My plan this week</div>' + lines(2, 22) + '</div>'
    return R(K, slug, title, age, 'Quick-response guide', list(topics), title, ill, why.split('.')[0] + '.', [s[0] for s in steps[:3]], '"' + script.split('<br>')[0].strip('"') + '"', body, group='guides')

RES.append(guide('when-your-child-refuses-to-listen', 'When Your Child Refuses to Listen', 'Ages 3–12', chat_ill('1.2in', '#E0A93B'),
    'Children may not hear or follow directions when they are absorbed, overwhelmed, or testing limits. It often is not defiance.', 'Your attention first, short directions, and a little time to switch gears.',
    [('Get close', 'Move near, make eye contact, and say their name.'), ('Be short', 'One clear direction: "Shoes on, please."'), ('Give a moment', 'Wait 5 to 10 seconds before repeating.'), ('Follow through', 'Calmly help, or use the consequence you named.')],
    '"I need you to put your shoes on. I\'ll help if you need me."', 'Repeating louder, long explanations, or yelling from another room.'))
RES.append(guide('when-your-child-screams-cries-or-is-aggressive', 'When Your Child Screams, Cries, or Becomes Aggressive', 'Ages 3–12', dial_ill('1.3in'),
    'Intense emotions can overwhelm a child\'s ability to think or talk, so the body takes over with crying, yelling, or lashing out.', 'Safety, calm adults, and help to return to calm before any talking.',
    [('Keep everyone safe', 'Move objects or siblings, stay close, and block hits gently.'), ('Lower your voice', 'Fewer words, slow breathing, and a calm face.'), ('Name it', '"You\'re furious. I won\'t let you hurt. I\'m here."'), ('Reconnect later', 'Once calm, talk about what happened and what to try next.')],
    '"I\'m here. I won\'t let you hurt anyone. We\'ll talk when you\'re calm."', 'Matching their volume, shaming, or trying to reason during the peak.'))
RES.append(guide('when-your-child-says-no', 'When Your Child Says "No!"', 'Ages 2–10', stop_ill('1.2in'),
    '"No" is a normal sign of growing independence. Children are learning they have their own wants.', 'Choices, a sense of control, and clear limits delivered kindly.',
    [('Stay calm', 'Take a breath. This is development, not disrespect.'), ('Offer two choices', '"Do you want to wear the red or blue shirt?"'), ('Hold the limit', 'Some things are not optional: safety, health.'), ('Notice cooperation', 'Praise any "yes": "Thanks for putting your coat on."')],
    '"You don\'t want to go. I hear you. It\'s time to leave. Walk or hop?"', 'Power struggles, bribing every time, or giving in after repeated no\'s.'))
RES.append(guide('screen-time-conflicts', 'Managing Screen-Time Conflicts', 'Ages 4–16', phone_ill('1.2in', '#E0A93B'),
    'Screens are engaging by design, and stopping mid-activity is hard for children (and adults) because of how attention shifts.', 'Predictable rules, advance warnings, and good alternatives.',
    [('Agree on rules together', 'When, where, how long, and what happens at the end.'), ('Give a warning', '5-minute and 1-minute countdowns with a timer.'), ('Use the same ending routine', 'Save, turn off, then a fun next activity.'), ('Model it', 'Show your own healthy phone habits.')],
    '"Five more minutes, then we turn it off and pick a game together."', 'Surprise shutoffs, using screens as the only reward, or arguing at the end.'))
RES.append(guide('boundaries-without-constant-arguments', 'Setting Boundaries Without Constant Arguments', 'Ages 4–14', shield_ill('1.2in', '#E0A93B'),
    'Children test boundaries to learn where they are. Arguments grow when rules change or we explain too much in the moment.', 'Predictable rules, brief responses, and your calm follow-through.',
    [('Decide ahead', 'Know your rules and consequences before conflicts start.'), ('Say it once, kindly', 'Short, clear, and calm. Skip the debate.'), ('Acknowledge feelings', '"You\'re disappointed. The answer is still no."'), ('Follow through', 'Consistency teaches more than words.')],
    '"I hear that you disagree. The answer is no. I\'m happy to talk after dinner."', 'Over-explaining, changing the rule when they push, or arguing back.'))
RES.append(guide('when-siblings-fight', 'When Siblings Fight', 'Ages 3–14', people_ill('1.3in', '#E0A93B'),
    'Siblings compete for attention and resources. Fighting is normal, and it is also a chance to teach conflict skills.', 'A chance to be heard, help solving problems, and time apart when heated.',
    [('Stay neutral', 'Do not decide who started it. Focus on solving.'), ('Separate if needed', 'Give each child space to calm down first.'), ('Let each speak', 'One at a time: "What happened? What do you need?"'), ('Problem-solve together', 'Ask: "What could you do next time?"')],
    '"I see two upset kids. Take a break, then we\'ll find a fair solution."', 'Taking sides, comparing siblings, or always stepping in immediately.'))
RES.append(guide('helping-children-transition-between-activities', 'Helping Children Transition Between Activities', 'Ages 3–10', clock_ill('1.2in', '#E0A93B'),
    'Switching activities is hard when a child is absorbed or when the next activity is less fun. Many children need extra support to shift.', 'Warnings, visuals, and something to look forward to.',
    [('Warn early', '10, 5, and 1 minute warnings.'), ('Use a visual timer', 'Let them see time passing.'), ('Preview what is next', '"First clean up, then snack."'), ('Give a job', 'Let them carry the bag or push the button.')],
    '"Five more minutes of play, then it\'s snack time. I\'ll set the timer."', 'Sudden stops, vague "soon," or rushing the child.', ('parenting', 'emotional-regulation')))
RES.append(guide('building-trust-and-connection', 'Building Trust and Strengthening the Parent-Child Relationship', 'Ages 2–18', heart_hands('1.2in'),
    'Trust grows through small, consistent moments of attention, reliability, and repair when things go wrong.', 'Your undivided attention, honesty, and warmth.',
    [('Special time', '10 undistracted minutes a day, child-led.'), ('Keep promises', 'Do what you say. If you cannot, say so honestly.'), ('Repair after conflict', '"I yelled. I\'m sorry. Let\'s try again."'), ('Show interest', 'Ask about their world and really listen.')],
    '"I love you no matter what. I\'m here whenever you need me."', 'Only noticing mistakes, breaking promises, or avoiding repair.', ('parenting', 'relationships')))
