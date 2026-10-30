from rlib import *

K = 'adult'
A = 'Adults'
WS, GD, ACT, REF = 'Printable worksheet', 'Educational guide', 'Activity', 'Self-reflection'
RES = []


def numbox(n, title, text, cls='tint'):
    return f'<div class="box {cls}" style="margin-bottom:7px;display:flex;gap:8px;align-items:flex-start"><span class="num">{n}</span><div><b>{title}</b><div style="font-size:10.5pt;line-height:1.35">{text}</div></div></div>'

# 1 ---------------------------------------------------------------- coping plan
RES.append(R(K, 'personal-coping-plan', 'Personal Coping Plan', A, WS, ['stress', 'emotional-regulation', 'anxiety'], 'Developing individualized coping strategies',
    shield_ill('1.2in', '#4F6FB5'), 'A plan made while calm is easier to use when stress is high. It gathers your warning signs, tools, and supports in one place.',
    ['Fill in each section when you feel steady.', 'Keep it where you can find it quickly.', 'Update it every few months.'],
    '"Warning sign: I stop answering texts. Tool: a 10-minute walk. Person: my sister."',
    grid(2, [box('<div class="lab">1. My early warning signs</div><div class="small">body, thoughts, behavior</div>' + lines(3, 22), 'coral'), box('<div class="lab">2. Things that help me settle</div><div class="small">on my own</div>' + lines(3, 22), 'teal'),
             box('<div class="lab">3. People I can reach out to</div>' + lines(3, 22), 'blue'), box('<div class="lab">4. Places that help me feel better</div>' + lines(3, 22), 'sand')], 10) +
    box('<div class="lab">5. Professional supports</div><div class="small">counselor, doctor, support group</div>' + lines(2, 22), 'lilac', 'margin-top:10px') +
    '<div class="warn" style="margin-top:10px"><b>If you are in crisis or thinking of harming yourself:</b> call or text <b>988</b> (Suicide &amp; Crisis Lifeline) or call <b>911</b>. Go to your nearest emergency department.</div>', start=True))

# 2 ---------------------------------------------------------------- wellness check-in
areas = ['Emotional', 'Physical', 'Social', 'Work / purpose', 'Rest', 'Joy / meaning']
RES.append(R(K, 'emotional-wellness-check-in', 'Emotional Wellness Check-In', A, WS, ['stress', 'emotional-regulation'], 'Monitoring emotional well-being',
    sun_ill('1.2in', '#4F6FB5'), 'A quick check-in helps you notice what needs attention before stress builds. Do it weekly.',
    ['Rate each area from 1 to 5.', 'Notice the lowest area.', 'Choose one small step.'],
    '"Rest: 2. Step: no screens after 10 pm for 3 nights."',
    ''.join(f'<div class="row" style="margin-bottom:7px"><div style="width:1.5in" class="lab">{a}</div><div style="flex:1">{circles(5, 30)}</div></div>' for a in areas) +
    '<div class="small" style="margin:2px 0 8px">1 = struggling · 5 = thriving</div>' +
    grid(2, [box('<div class="lab">What is going well</div>' + lines(3, 22), 'teal'), box('<div class="lab">What needs attention</div>' + lines(3, 22), 'coral')], 10) +
    '<div class="box wb" style="margin-top:10px"><div class="lab">One small step I will take this week:</div>' + lines(2, 22) + '</div>' +
    '<div class="box sand" style="margin-top:8px"><div class="lab">Date: ________  Mood in one word: ________  Energy (1 to 10): ____</div></div>'))

# 3 ---------------------------------------------------------------- triggers
RES.append(R(K, 'understanding-your-triggers', 'Understanding Your Triggers', A, WS, ['emotional-regulation', 'stress', 'trauma'], 'Recognizing emotional patterns',
    magnifier_ill('1.2in', '#4F6FB5'), 'A trigger is something that sets off a strong emotional reaction, often tied to past experiences. Understanding yours gives you more choice.',
    ['Notice a strong reaction.', 'Trace it: what happened, felt, and thought?', 'Choose a new response.'],
    '"Trigger: boss says \'we need to talk.\' Feeling: dread. Old story: I\'m in trouble. New response: ask what it\'s about."',
    tbl(['What happened', 'Feeling & body', 'The story I told myself', 'A new response'], [['', '', '', '']] * 5, 52) +
    grid(2, [box('<div class="lab">Patterns I notice</div>' + lines(3, 22), 'sand'), box('<div class="lab">What I need when triggered</div>' + cbs(['Space', 'Reassurance', 'To be heard', 'Time to think', 'Movement', 'Support']), 'teal')], 10, 'margin-top:10px') +
    '<div class="box wb small" style="margin-top:8px">Triggers connected to trauma can be intense. Consider working with a trauma-informed counselor for support.</div>'))

# 4 ---------------------------------------------------------------- stress workbook (2 pages)
p2 = cont(K, 'Stress Management Workbook · Weekly Plan',
    '<div class="lab">My stress thermometer</div>' + ''.join(f'<div class="row" style="margin:4px 0"><div style="width:.9in;height:.42in;background:{c};border-radius:10px;display:grid;place-items:center;font-weight:700">{n}</div><div class="line" style="flex:1"></div></div>' for n, c in [('High', '#e8806a'), ('Medium', '#f2a96b'), ('Low', '#8fd3c8')]) +
    '<div class="small" style="margin:2px 0 8px">Describe what each level looks like for you and what you do about it.</div>' +
    '<div class="lab">Weekly stress plan</div>' + tbl(['Day', 'Biggest stressor', 'Tool I will use', 'Did it help? (1 to 5)'], [[d, '', '', ''] for d in ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']], 30) +
    grid(2, [box('<div class="lab">Things I can let go of</div>' + lines(3, 22), 'sand'), box('<div class="lab">Things I can say no to</div>' + lines(3, 22), 'blue')], 10, 'margin-top:10px') +
    '<div class="box teal" style="margin-top:10px"><div class="lab">Daily non-negotiables (check what you can do)</div>' + cbs(['Sleep 7+ hours', 'A short walk or movement', 'One real meal with no screen', 'A moment of quiet', 'Connect with one person']) + '</div>', 'Part 2 · Plan')
RES.append(R(K, 'stress-management-workbook', 'Stress Management Workbook', A, WS, ['stress', 'anxiety'], 'Identifying and managing stress',
    dial_ill('1.3in'), 'Stress is not always bad, but chronic stress wears you down. This workbook helps you find sources, signals, and tools.',
    ['Sort stressors by what you can change.', 'List your body and mind signals.', 'Pick tools and plan your week on page 2.'],
    '"Can change: my schedule. Can\'t change: traffic. Tool: leave 15 minutes earlier."',
    grid(2, [box('<div class="lab">My biggest stressors</div>' + lines(4, 22), 'coral'), box('<div class="lab">How stress shows up</div><div style="font-size:10pt">' + pills(['Headaches', 'Tight shoulders', 'Poor sleep', 'Irritable', 'Forgetful', 'Overeating', 'Withdrawn', 'Racing mind']) + '</div>', 'sand')], 10) +
    '<div class="grid g2" style="gap:10px;margin-top:10px"><div class="box teal"><div class="lab">I can change or influence</div>' + lines(3, 22) + '</div><div class="box blue"><div class="lab">I cannot change (so I will accept or adapt)</div>' + lines(3, 22) + '</div></div>' +
    '<div class="lab" style="margin:10px 0 4px">Tools menu (circle your go-tos)</div><div>' + pills(['Deep breathing', 'Walk outside', 'Exercise', 'Journaling', 'Talk to a friend', 'Music', 'Stretching', 'Prayer or meditation', 'Hobby', 'Nap', 'Say no', 'Take a break', 'Time in nature']) + '</div>', start=True, extra=(p2,)))

# 5 ---------------------------------------------------------------- values & boundaries
vals = ['Family', 'Health', 'Honesty', 'Growth', 'Faith', 'Freedom', 'Security', 'Creativity', 'Service', 'Connection', 'Rest', 'Adventure', 'Respect', 'Learning', 'Peace', 'Purpose']
RES.append(R(K, 'values-and-boundaries-worksheet', 'Values & Boundaries Worksheet', A, WS, ['relationships', 'stress'], 'Identifying personal priorities',
    shield_ill('1.2in', '#4F6FB5'), 'Values show what matters most. Boundaries protect it. When they match, life feels more aligned.',
    ['Circle your top 5 values.', 'Notice where your life crowds them out.', 'Write a boundary to protect each.'],
    '"Value: family time. Boundary: no work email after 6 pm."',
    '<div class="lab">Circle your top five values</div><div class="grid g4" style="gap:6px;margin:6px 0">' + ''.join(f'<div class="box blue center" style="padding:4px">{v}</div>' for v in vals) + '</div>' +
    '<div class="lab" style="margin-top:8px">Boundaries that protect them</div>' + tbl(['Value', 'What crowds it out', 'My boundary'], [['', '', '']] * 4, 42) +
    '<div class="box teal" style="margin-top:8px"><b>Boundary sentence:</b> "I can\'t ______, but I can ______." or "I need ______ so that ______." Calm, clear, and kind is enough.</div>' + field('The first boundary I will practice this week', 1, 24)))

# 6 ---------------------------------------------------------------- mindfulness
mind = [('Mindful breath', '2 min', ['Sit comfortably.', 'Notice the breath at your nose or belly.', 'When the mind wanders, return gently.']), ('Body scan', '5 min', ['Start at your toes.', 'Move slowly up to your head.', 'Notice tension and soften it.']), ('Mindful moment', '1 min', ['Pause what you are doing.', 'Name 3 things you see, hear, feel.', 'Take one slow breath.'])]
RES.append(R(K, 'mindfulness-exercises', 'Mindfulness Exercises', A, ACT, ['stress', 'anxiety', 'emotional-regulation'], 'Developing present-moment awareness',
    lungs_ill('1.2in', '#4F6FB5'), 'Mindfulness is noticing what is happening right now without judging it. Short practices work best when done often.',
    ['Pick one practice.', 'Try it for a week.', 'Log how you feel before and after.'],
    '"After a 2-minute breath practice my stress dropped from 7 to 5."',
    grid(3, [box(f'<div class="center"><span class="stick">{t}</span><div class="small" style="margin:3px 0">{m}</div></div>' + ''.join(f'<div style="font-size:10.5pt;margin:2px 0"><b>{i+1}.</b> {s}</div>' for i, s in enumerate(st)), c) for (t, m, st), c in zip(mind, ['teal', 'sand', 'blue'])], 8) +
    '<div class="lab" style="margin-top:10px">Practice log</div>' + tbl(['Day', 'Practice', 'Stress before (1-10)', 'Stress after', 'What I noticed'], [[d, '', '', '', ''] for d in ['Mon', 'Tue', 'Wed', 'Thu', 'Fri']], 34) +
    '<div class="box sand small" style="margin-top:8px"><b>If your mind wanders,</b> that is normal. If an exercise feels uncomfortable, open your eyes, look around, and stop. If memories or sensations feel overwhelming, consider speaking with a counselor.</div>'))

# 7 ---------------------------------------------------------------- self-compassion
RES.append(R(K, 'self-compassion-journal', 'Self-Compassion Journal', A, REF, ['confidence', 'emotional-regulation'], 'Reducing self-criticism',
    heart_hands('1.2in'), 'Self-compassion means treating yourself with the kindness you would offer a good friend. It builds resilience, not complacency.',
    ['Notice a moment of self-criticism.', 'Respond using the three parts.', 'Write a kind letter to yourself.'],
    '"I messed up the presentation. Many people struggle with this. I will ask for feedback and rest tonight."',
    grid(3, [box('<div class="center"><span class="stick">1 · Mindfulness</span></div><div style="font-size:10.5pt">"This is a hard moment."</div>' + lines(2, 22), 'teal'), box('<div class="center"><span class="stick">2 · Common humanity</span></div><div style="font-size:10.5pt">"Others feel this way too."</div>' + lines(2, 22), 'sand'), box('<div class="center"><span class="stick">3 · Kindness</span></div><div style="font-size:10.5pt">"May I be gentle with myself."</div>' + lines(2, 22), 'blue')], 8) +
    box('<div class="lab">What I am criticizing myself for</div>' + lines(2, 22), 'coral', 'margin-top:10px') +
    box('<div class="lab">What I would say to a good friend in this situation</div>' + lines(3, 22), 'teal', 'margin-top:8px') +
    box('<div class="lab">A kind letter to myself</div>' + lines(4, 22), 'lilac', 'margin-top:8px')))

# 8 ---------------------------------------------------------------- cognitive restructuring
RES.append(R(K, 'cognitive-restructuring', 'Cognitive Restructuring', A, WS, ['anxiety', 'emotional-regulation'], 'Challenging unhelpful thinking',
    brain_ill('1.2in', '#4F6FB5'), 'Thoughts are not facts. This thought record helps you test unhelpful thoughts and find a more balanced view.',
    ['Capture the situation and your automatic thought.', 'List evidence for and against.', 'Write a balanced thought and re-rate your feeling.'],
    '"Thought: \'I\'ll fail.\' For: I\'m nervous. Against: I\'ve passed before. Balanced: \'It\'s hard, and I can prepare.\'"',
    tbl(['Situation', 'Automatic thought', 'Feeling (0-100)'], [['', '', '']] * 2, 38) +
    grid(2, [box('<div class="lab">Evidence FOR the thought</div>' + lines(3, 22), 'coral'), box('<div class="lab">Evidence AGAINST the thought</div>' + lines(3, 22), 'teal')], 10, 'margin:8px 0') +
    grid(2, [box('<div class="lab">A more balanced thought</div>' + lines(3, 22), 'sb'), box('<div class="lab">Feeling now (0-100)</div>' + lines(1, 22) + '<div class="small">What changed?</div>' + lines(1, 22), 'sb')], 10) +
    '<div class="lab" style="margin-top:8px">Common thinking traps</div><div>' + pills(['All-or-nothing', 'Catastrophizing', 'Mind reading', 'Should statements', 'Overgeneralizing', 'Emotional reasoning', 'Personalizing', 'Filtering the positive']) + '</div>'))

# 9 ---------------------------------------------------------------- healthy relationship checklist
RES.append(R(K, 'healthy-relationship-checklist', 'Healthy Relationship Checklist', A, WS, ['relationships'], 'Recognizing relationship patterns',
    people_ill('1.3in', '#4F6FB5'), 'Healthy relationships feel safe, respectful, and balanced. This checklist helps you see the patterns in a relationship, with kindness to yourself.',
    ['Pick one relationship.', 'Check what is true most of the time.', 'Reflect on what you need.'],
    '"Mostly healthy, but I feel dismissed when I share feelings. I could ask for more listening."',
    '<div class="grid g2" style="gap:10px"><div class="box teal"><span class="stick" style="background:#1f7a74">Signs of health</span>' + cbs(['I feel safe being myself', 'We both listen', 'Disagreements are respectful', 'Trust goes both ways', 'We support each other\'s goals', 'I can say no without punishment', 'We make decisions together', 'We repair after conflict']) + '</div><div class="box coral"><span class="stick" style="background:#c9604a">Red flags</span>' + cbs(['Controlling or jealous', 'Put-downs or name-calling', 'Cutting me off from others', 'Guilt-tripping', 'Ignoring my boundaries', 'Walking on eggshells', 'Threats or intimidation', 'Hot-and-cold behavior']) + '</div></div>' +
    grid(2, [box('<div class="lab">What I need more of</div>' + lines(2, 22), 'sb'), box('<div class="lab">A boundary or conversation I could try</div>' + lines(2, 22), 'sb')], 10, 'margin-top:10px') +
    '<div class="warn" style="margin-top:8px"><b>If you feel unsafe</b> in a relationship, help is available: National Domestic Violence Hotline 1-800-799-7233 (text START to 88788), or call 911 in an emergency.</div>'))

# 10 ---------------------------------------------------------------- burnout prevention
RES.append(R(K, 'burnout-prevention-guide', 'Burnout Prevention Guide', A, GD, ['stress'], 'Recognizing emotional exhaustion',
    battery_ill('1.4in'), 'Burnout is exhaustion from prolonged stress, often at work or in caregiving. It builds slowly, so catching early signs matters.',
    ['Check the signs you notice.', 'List what drains and what recharges you.', 'Make one change this week.'],
    '"Drains: back-to-back meetings. Recharges: lunch outside. Change: block a 30-minute lunch."',
    '<div class="grid g2" style="gap:10px"><div class="box coral"><div class="lab">Early warning signs</div>' + cbs(['Constant exhaustion', 'Dreading work or tasks', 'Cynical or detached', 'Feeling ineffective', 'Irritable', 'Trouble sleeping', 'Getting sick often', 'Losing joy in things']) + '</div><div class="box teal"><div class="lab">Prevention toolkit</div>' + cbs(['Set work hours', 'Take real breaks', 'Say no to extras', 'Ask for help or delegate', 'Move your body', 'Protect sleep', 'Time with people you like', 'Hobbies outside work']) + '</div></div>' +
    grid(2, [box('<div class="lab">What drains me</div>' + lines(3, 22), 'sand'), box('<div class="lab">What recharges me</div>' + lines(3, 22), 'blue')], 10, 'margin-top:10px') +
    '<div class="box wb" style="margin-top:10px"><div class="lab">One change I will make this week:</div>' + lines(2, 22) + '</div><div class="box lilac small" style="margin-top:8px">If exhaustion, hopelessness, or low mood are lasting, talk with a doctor or licensed mental health professional.</div>'))

# 11 ---------------------------------------------------------------- growth planner
RES.append(R(K, 'personal-growth-planner', 'Personal Growth Planner', A, WS, ['confidence'], 'Setting meaningful goals',
    plant_ill('1.2in', '#4F6FB5'), 'Growth works best with clear, kind goals and small steps. Choose what matters to you, not what you think you should want.',
    ['Pick 1 to 2 areas.', 'Write a specific goal with a first step.', 'Check in every two weeks.'],
    '"Goal: walk 20 minutes three times a week. First step: lay out shoes tonight."',
    tbl(['Area', 'My goal (specific)', 'First step', 'By when'], [['Emotional', '', '', ''], ['Relationships', '', '', ''], ['Health', '', '', ''], ['Work / purpose', '', '', ''], ['Joy / learning', '', '', '']], 50) +
    grid(2, [box('<div class="lab">What might get in the way</div>' + lines(2, 22), 'coral'), box('<div class="lab">How I will handle it</div>' + lines(2, 22), 'teal')], 10, 'margin-top:10px') +
    '<div class="lab" style="margin-top:8px">90-day check-ins</div>' + tbl(['Day 30', 'Day 60', 'Day 90'], [['', '', '']], 54)))

# 12 ---------------------------------------------------------------- resilience
pil = [('Connection', 'People I can lean on'), ('Meaning', 'What gives my life purpose'), ('Body care', 'Sleep, food, movement'), ('Flexible thinking', 'Seeing options and reframing'), ('Skills', 'Coping tools I trust')]
RES.append(R(K, 'building-resilience', 'Building Resilience', A, WS, ['stress', 'confidence', 'emotional-regulation'], 'Developing adaptive coping skills',
    bridge_ill('1.4in', '#4F6FB5'), 'Resilience is the ability to adapt and recover from hard times. It is built through everyday habits and supports, not just toughness.',
    ['Rate each pillar from 1 to 5.', 'Choose the one to strengthen.', 'Plan one concrete action.'],
    '"Connection: 2. Action: text an old friend and invite them for a walk."',
    ''.join(f'<div class="row" style="margin-bottom:7px"><div style="width:1.6in"><b>{t}</b><div class="small">{d}</div></div><div style="flex:1">{circles(5, 28)}</div></div>' for t, d in pil) +
    grid(2, [box('<div class="lab">A hard time I got through</div>' + lines(3, 22) + '<div class="small">What helped me?</div>' + lines(1, 22), 'teal'), box('<div class="lab">Strengths I used</div>' + lines(3, 22), 'sand')], 10, 'margin-top:8px') +
    '<div class="box wb" style="margin-top:8px"><div class="lab">The pillar I will strengthen and my first action:</div>' + lines(2, 22) + '</div>'))

# ======================================================== educational topics
def topic(slug, title, ill, what, left_title, left, right_title, right, ex, how, reflect, topics, extra_box=None):
    body = f'<div class="grid g2" style="gap:10px"><div class="box teal"><div class="lab">{left_title}</div>{bl(left)}</div><div class="box sand"><div class="lab">{right_title}</div>{bl(right)}</div></div>'
    if extra_box: body += extra_box
    body += '<div class="box wb" style="margin-top:10px"><div class="lab">Reflect</div>' + ''.join(f'<div class="small" style="margin-top:4px">{q}</div>{lines(1, 22)}' for q in reflect) + '</div>'
    return R(K, slug, title, A, GD, topics, title, ill, what, how, ex, body, group='topics')

RES.append(topic('understanding-your-nervous-system', 'Understanding Your Nervous System', dial_ill('1.3in'),
    'Your nervous system constantly scans for safety or threat. Knowing its states helps you understand reactions and choose tools to shift.',
    'Activated (stress response)', ['Racing heart and thoughts', 'Tension, restlessness', 'Irritability or panic', 'Tools: slow exhale breathing, movement, cold water'], 'Settled (rest and connect)', ['Steady breathing', 'Curious and open', 'Able to think and feel', 'Tools: connection, nature, gentle routines'],
    '"I noticed my shoulders at my ears. A long exhale helped me settle."', ['Notice your state.', 'Name it kindly.', 'Try one shifting tool.'],
    ['Which state do I spend the most time in?', 'What reliably helps me shift toward settled?'], ['stress', 'emotional-regulation', 'trauma'],
    extra_box='<div class="box blue center" style="margin-top:10px"><div class="lab">Where am I right now?</div>' + dial_ill('2.8in') + '<div class="small">Calm &nbsp;···&nbsp; Alert &nbsp;···&nbsp; Overwhelmed</div></div>'))
RES.append(topic('emotional-boundaries-vs-emotional-walls', 'Emotional Boundaries vs. Emotional Walls', shield_ill('1.2in', '#4F6FB5'),
    'A boundary says, "This is what I need to feel safe, and I stay connected." A wall says, "I keep everyone out." Boundaries protect connection. Walls prevent it.',
    'Emotional boundaries', ['Flexible and selective', 'Clear, calm communication', 'Allow closeness and safety', '"I need time, and I\'ll be back."'], 'Emotional walls', ['Rigid and all-or-nothing', 'Avoidance or shutting down', 'Keep people out, including safe ones', '"I\'m fine. Leave me alone."'],
    '"I told my friend I needed a quiet evening, and asked to talk tomorrow."', ['Notice when you withdraw.', 'Ask: am I protecting or hiding?', 'Practice one boundary sentence.'],
    ['Where do I have a wall that may no longer be needed?', 'Where do I need a clearer boundary?'], ['relationships']))
RES.append(topic('managing-anxiety-and-uncertainty', 'Managing Anxiety and Uncertainty', lungs_ill('1.2in', '#4F6FB5'),
    'Anxiety often comes from not knowing. The mind tries to solve the unknown by worrying. Learning to tolerate uncertainty is a skill.',
    'What helps', ['Name it: "I am feeling uncertain."', 'Separate what you know from what you don\'t', 'Focus on the next small step', 'Slow breathing and grounding', 'Limit news and doom-scrolling'], 'What keeps it going', ['Seeking constant reassurance', 'Avoiding the situation', 'Mentally rehearsing worst cases', 'Trying to control everything', 'Skipping sleep and movement'],
    '"I don\'t know the outcome. I do know I can prepare and handle what comes."', ['Write what is known and unknown.', 'Choose one next step.', 'Schedule a 15-minute worry window.'],
    ['What am I trying to control right now?', 'What would it be like to accept not knowing for today?'], ['anxiety', 'stress']))
RES.append(topic('healthy-communication-habits', 'Developing Healthy Communication Habits', chat_ill('1.2in', '#4F6FB5'),
    'Healthy communication is clear, respectful, and curious. Small habits make a big difference in relationships.',
    'Habits to build', ['Listen to understand, not to win', 'Use "I" statements', 'Ask before assuming', 'Pause when upset', 'Say what you need'], 'Habits to ease', ['Interrupting', 'Name-calling or sarcasm', 'Silent treatment', 'Bringing up old issues', '"Always" and "never"'],
    '"I felt worried when you were late. Can we agree to text if plans change?"', ['Pick one habit to build.', 'Practice with a low-stakes topic.', 'Notice how others respond.'],
    ['Which habit do I most want to build?', 'What is hardest for me to say out loud?'], ['relationships'],
    extra_box='<div class="box blue center" style="margin-top:10px"><div class="lab">Try this formula</div><div style="font:600 12pt Fr,serif;line-height:1.6">When ______ happens, I feel ______.<br>I need ______. Would you be willing to ______?</div></div>'))
RES.append(topic('recognizing-unhealthy-relationship-dynamics', 'Recognizing Unhealthy Relationship Dynamics', people_ill('1.3in', '#4F6FB5'),
    'Unhealthy patterns can be subtle: over time they can erode your confidence and safety. Naming them is the first step to deciding what to do.',
    'Patterns to notice', ['Walking on eggshells', 'Control over money, time, or friends', 'Constant criticism or contempt', 'Gaslighting: making you doubt your reality', 'Cycles of tension, blowup, and "making up"'], 'Steps you can take', ['Trust your feelings', 'Talk with someone safe', 'Keep a record of what happens', 'Plan for safety if needed', 'Seek counseling or advocacy support'],
    '"I realized I\'d stopped seeing my friends. That\'s a sign I should look closer."', ['Name one pattern.', 'Tell one trusted person.', 'Learn about support options.'],
    ['What patterns do I notice that concern me?', 'Who is safe for me to talk to?'], ['relationships', 'trauma'],
    extra_box='<div class="warn" style="margin-top:10px"><b>If you are unsafe:</b> National Domestic Violence Hotline 1-800-799-7233 (text START to 88788). In an emergency call 911. For crisis support call or text 988.</div>'))
