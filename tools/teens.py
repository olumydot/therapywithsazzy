from rlib import *

K = 'teen'
A = 'Ages 12–18'
WS, GD, ACT, REF = 'Printable worksheet', 'Educational guide', 'Activity', 'Self-reflection'
RES = []


def numbox(n, title, text, cls='tint'):
    return f'<div class="box {cls}" style="margin-bottom:7px;display:flex;gap:8px;align-items:flex-start"><span class="num">{n}</span><div><b>{title}</b><div style="font-size:10.5pt;line-height:1.35">{text}</div></div></div>'


def wheel(labels, w='3.4in'):
    import math
    n = len(labels)
    s = f'<svg viewBox="0 0 300 300" style="width:{w};height:auto"><g stroke="#16243a" stroke-width="2.5">'
    cols = ['#dff1ee', '#fbf0d4', '#fde9e3', '#e4eaf6', '#ebe7f5', '#e6f4f1', '#fbe3a8', '#d3ece8']
    for i in range(n):
        a0 = math.radians(i * 360 / n - 90); a1 = math.radians((i + 1) * 360 / n - 90)
        x0, y0, x1, y1 = 150 + 140 * math.cos(a0), 150 + 140 * math.sin(a0), 150 + 140 * math.cos(a1), 150 + 140 * math.sin(a1)
        s += f'<path d="M150 150L{x0:.1f} {y0:.1f}A140 140 0 0 1 {x1:.1f} {y1:.1f}Z" fill="{cols[i % len(cols)]}"/>'
    s += '</g><circle cx="150" cy="150" r="30" fill="#fff" stroke="#16243a" stroke-width="2.5"/><text x="150" y="154" text-anchor="middle" font-family="Arial" font-weight="700" font-size="13" fill="#16243a">ME</text>'
    for i, l in enumerate(labels):
        a = math.radians((i + .5) * 360 / n - 90)
        s += f'<text x="{150 + 100*math.cos(a):.1f}" y="{150 + 100*math.sin(a):.1f}" text-anchor="middle" font-family="Arial" font-weight="700" font-size="11" fill="#16243a">{l}</text>'
    return s + '</svg>'


def box_breath(w='1.6in'):
    return f'<svg viewBox="0 0 180 180" style="width:{w};height:auto"><rect x="30" y="30" width="120" height="120" rx="10" fill="#dff1ee" stroke="#16243a" stroke-width="4"/><g font-family="Arial" font-weight="700" font-size="12" fill="#16243a" text-anchor="middle"><text x="90" y="22">IN · 4</text><text x="168" y="94" transform="rotate(90 168 94)">HOLD · 4</text><text x="90" y="172">OUT · 4</text><text x="12" y="94" transform="rotate(-90 12 94)">HOLD · 4</text></g><circle cx="30" cy="150" r="8" fill="#E8806A"/></svg>'

# 1 --------------------------------------------------------------- stress check-in
def scale_row(t, lo, hi): return f'<div style="margin-bottom:8px"><div class="lab">{t}</div>{circles(10, 28)}<div class="small" style="display:flex;justify-content:space-between"><span>{lo}</span><span>{hi}</span></div></div>'
RES.append(R(K, 'the-stress-check-in', 'The Stress Check-In', A, WS, ['stress', 'anxiety'], 'Identifying sources of stress',
    dial_ill('1.3in'), 'Stress shows up in your body, mind, and mood. A two-minute check-in helps you notice it before it piles up.',
    ['Circle a number for each area (1 low, 10 high).', 'List what is adding to your stress.', 'Choose one thing that would help.'],
    '"Body 7, mind 8, mood 5. Stress: two tests and a fight with my friend. Help: talk to her."',
    scale_row('Body: how tense or tired?', 'relaxed', 'very tense') + scale_row('Mind: how racing or foggy?', 'clear', 'racing') + scale_row('Mood: how heavy or on edge?', 'light', 'heavy') + scale_row('Energy: how drained?', 'full', 'empty') +
    '<div class="lab">What is adding to my stress?</div><div>' + pills(['School', 'Friends', 'Family', 'Sports or activities', 'Social media', 'Future', 'Money', 'Health', 'Sleep']) + '</div>' + field('One thing that would help a little', 1, 24) +
    '<div class="box teal small" style="margin-top:6px">If your numbers stay high for a couple of weeks, talk with a parent, school counselor, or trusted adult. You do not have to handle it alone.</div>'))

# 2 --------------------------------------------------------------- overthinking
RES.append(R(K, 'overthinking-worksheet', 'Overthinking Worksheet', A, WS, ['anxiety', 'emotional-regulation'], 'Challenging repetitive thoughts',
    brain_ill('1.2in', '#2E9C95'), 'Overthinking is your brain looping on a worry. Separating facts from guesses breaks the loop.',
    ['Write the looping thought.', 'Sort facts from the story your brain is telling.', 'Choose one small step or let it go.'],
    '"Thought: \'Everyone thinks I\'m weird.\' Fact: I got invited to lunch. Story: they\'re judging me."',
    field('The thought that keeps looping', 2, 22) + grid(2, [box('<div class="lab">Facts (what I know)</div>' + lines(3, 22), 'teal'), box('<div class="lab">Story (what I\'m guessing)</div>' + lines(3, 22), 'coral')], 10, 'margin:6px 0') +
    grid(3, [box('<div class="lab">Worst case</div>' + lines(2, 22)), box('<div class="lab">Best case</div>' + lines(2, 22)), box('<div class="lab">Most likely</div>' + lines(2, 22))], 8) +
    grid(2, [box('<div class="lab">In my control</div>' + lines(2, 22), 'sb'), box('<div class="lab">Not in my control</div>' + lines(2, 22), 'sb')], 10, 'margin-top:8px') + field('One small step I can take (or let go of)', 1, 24), start=True))

# 3 --------------------------------------------------------------- self esteem journal
RES.append(R(K, 'my-self-esteem-journal', 'My Self-Esteem Journal', A, REF, ['confidence'], 'Building self-worth',
    journal_ill('1.2in'), 'Your brain remembers mistakes loudly. Journaling helps you notice what you do well and who you are.',
    ['Answer the prompts honestly.', 'Add one entry a day for a week.', 'Reread it on tough days.'],
    '"Today I stood up for my friend. That took courage."',
    '<div class="lab">Five things I like about myself</div>' + ''.join(f'<div class="row"><span class="num">{i}</span><div class="line" style="flex:1"></div></div>' for i in range(1, 6)) +
    grid(2, [box('<div class="lab">A time I handled something hard</div>' + lines(3, 22), 'teal'), box('<div class="lab">What a friend would say is great about me</div>' + lines(3, 22), 'sand')], 10, 'margin:8px 0') +
    '<div class="lab">This week</div>' + tbl(['Day', 'One thing I did well or am proud of'], [[d, ''] for d in ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']], 26), start=True))

# 4 --------------------------------------------------------------- boundaries
RES.append(R(K, 'setting-boundaries-teens', 'Setting Boundaries', A, GD, ['relationships', 'confidence'], 'Healthy interpersonal relationships',
    shield_ill('1.2in', '#2E9C95'), 'A boundary is a limit that protects your feelings, time, body, and stuff. Good boundaries make relationships healthier.',
    ['Check the boundaries that matter to you.', 'Practice a sentence for one.', 'Notice how it feels to hold it.'],
    '"I\'m not comfortable sharing my passwords. I\'m happy to hang out another way."',
    '<div class="grid g2" style="gap:10px"><div class="box teal"><div class="lab">My personal boundaries checklist</div>' + cbs(['My body and personal space', 'My phone and passwords', 'My time and energy', 'My feelings (not being teased)', 'My privacy and secrets', 'My belongings', 'Saying no without guilt', 'Taking breaks from people']) + '</div><div>' +
    box('<div class="lab">A boundary sentence</div><div style="font-size:10.5pt;line-height:1.5">"I\'m not okay with ______.<br>I need ______.<br>I can ______ instead."</div>', 'sand') + '<div style="height:8px"></div>' + box('<div class="lab">One boundary I will practice</div>' + lines(3, 22), 'blue') + '</div></div>' +
    tbl(['Situation', 'What I need', 'How I\'ll say it'], [['', '', '']] * 3, 40) + '<div class="box wb small" style="margin-top:8px">Boundaries are not mean. You can be kind and clear at the same time. If someone repeatedly ignores your boundaries or you feel unsafe, tell a trusted adult.</div>'))

# 5 --------------------------------------------------------------- peer pressure
RES.append(R(K, 'managing-peer-pressure', 'Managing Peer Pressure', A, WS, ['relationships', 'confidence'], 'Making independent decisions',
    people_ill('1.3in', '#2E9C95'), 'Peer pressure can be loud or quiet. Knowing your values and having your exit lines ready makes it easier to choose for yourself.',
    ['Name a pressure you may face.', 'Check it against your values.', 'Pick a line and an exit plan.'],
    '"They want me to skip class. My value: doing well. Line: \'Nah, I\'m good.\' Exit: text my mom."',
    grid(2, [box('<div class="lab">Pressure I may face</div>' + lines(2, 22), 'coral'), box('<div class="lab">What I value</div>' + lines(2, 22), 'teal')], 10) +
    '<div class="lab" style="margin:10px 0 4px">Ways to say no</div><div>' + pills(['"Nah, I\'m good."', '"That\'s not my thing."', '"I\'ve got to be somewhere."', '"I\'m not into that."', 'Change the subject', 'Use humor', 'Walk away', 'Blame a parent']) + '</div>' +
    grid(2, [box('<div class="lab">My exit plan</div>' + cbs(['Text a trusted person', 'Call for a ride', 'Go to a safe space', 'Leave with a friend']), 'sand'), box('<div class="lab">Who has my back?</div>' + lines(3, 22), 'blue')], 10, 'margin-top:8px') +
    '<div class="box wb" style="margin-top:8px"><div class="lab">Before I decide, I ask myself:</div>' + cbs(['Is it safe?', 'Is it respectful to me and others?', 'Will I be okay with it tomorrow?', 'Is it my choice?']) + '</div>'))

# 6 --------------------------------------------------------------- social media
RES.append(R(K, 'social-media-and-mental-health', 'Social Media & Mental Health', A, GD, ['stress', 'confidence', 'anxiety'], 'Understanding digital wellness',
    phone_ill('1.2in'), 'Social media can connect us and also stress us out. Noticing how you feel before and after helps you take charge.',
    ['Track how you feel after 3 apps.', 'Check your digital habits.', 'Pick one change to try.'],
    '"After 30 minutes scrolling I felt worse about myself, so I muted a few accounts."',
    tbl(['App / platform', 'How I felt before', 'How I felt after', 'Better, same, or worse?'], [['', '', '', '']] * 3, 40) +
    grid(2, [box('<div class="lab">Healthy habits</div>' + cbs(['Phone-free meals', 'No phone for 30 min before bed', 'Mute or unfollow what drains me', 'Follow people who inspire me', 'Take breaks', 'Remember posts are highlight reels']), 'teal'), box('<div class="lab">Warning signs</div>' + cbs(['Comparing myself a lot', 'Feeling left out', 'Losing sleep', 'FOMO (fear of missing out)', 'Anxious without my phone', 'Getting into arguments online']), 'coral')], 10, 'margin-top:8px') +
    '<div class="box sb" style="margin-top:8px"><div class="lab">One change I\'ll try this week:</div>' + lines(2, 22) + '</div>'))

# 7 --------------------------------------------------------------- anxiety guide
RES.append(R(K, 'anxiety-management-guide', 'Anxiety Management Guide', A, GD, ['anxiety', 'emotional-regulation'], 'Managing anxious thoughts',
    lungs_ill('1.2in', '#2E9C95'), 'Anxiety is your body\'s alarm system. It can be helpful, but sometimes it sounds the alarm when there is no danger.',
    ['Spot your body\'s signals and thoughts.', 'Try one calming tool for 2 minutes.', 'Face the smaller steps of what you avoid.'],
    '"My chest tightens before presentations. I do box breathing for 2 minutes and feel steadier."',
    f'<div class="grid g3" style="gap:8px"><div class="box coral"><div class="lab">My body signals</div>{cbs(["Racing heart", "Tight chest", "Sweaty hands", "Stomachache", "Shaky", "Headache"])}</div><div class="box sand"><div class="lab">My thoughts</div>{lines(4, 22)}</div><div class="box teal center"><div class="lab">Box breathing</div>{box_breath("1.7in")}</div></div>' +
    grid(2, [box('<div class="lab">5-4-3-2-1 grounding</div><div style="font-size:10.5pt">5 things you see · 4 you feel · 3 you hear · 2 you smell · 1 you taste</div>', 'blue'), box('<div class="lab">Reframe the thought</div><div style="font-size:10.5pt">"What if it goes badly?" → "What if it goes okay? What would I do if it didn\'t?"</div>', 'lilac')], 10, 'margin-top:8px') +
    '<div class="lab" style="margin-top:8px">My anxiety ladder (small to big)</div>' + ''.join(f'<div class="row" style="margin:3px 0 3px {i*30}px"><span class="num">{i+1}</span><div class="line" style="flex:1"></div></div>' for i in range(4)) +
    '<div class="box wb small" style="margin-top:6px">If anxiety is getting in the way of school, friends, or sleep, talk to a parent, counselor, or doctor. Support helps.</div>', start=True))

# 8 --------------------------------------------------------------- emotional regulation plan
RES.append(R(K, 'emotional-regulation-plan', 'Emotional Regulation Plan', A, WS, ['emotional-regulation', 'anger'], 'Responding rather than reacting',
    dial_ill('1.3in'), 'You cannot always control feelings, but you can choose how to respond. A plan made when you are calm is easier to use when you are not.',
    ['Fill in your triggers and usual reactions.', 'Choose a better response for each.', 'Practice the Pause, Name, Choose steps.'],
    '"Trigger: being interrupted. Usually: snap. Better: take a breath, say, \'Let me finish.\'"',
    grid(3, [box(f'<div class="center"><span class="num" style="margin:0">{i}</span><div class="lab" style="margin-top:3px">{t}</div><div class="small">{d}</div></div>', c) for i, (t, d, c) in enumerate([('Pause', 'Breathe before reacting.', 'teal'), ('Name', 'What am I feeling? Why?', 'sand'), ('Choose', 'What response fits my values?', 'blue')], 1)], 8) +
    '<div style="height:8px"></div>' + tbl(['Trigger', 'What I usually do', 'A better response'], [['', '', '']] * 4, 44) +
    grid(2, [box('<div class="lab">Warning signs I am heating up</div>' + lines(2, 22), 'coral'), box('<div class="lab">My go-to reset tools</div>' + cbs(['Walk or move', 'Music', 'Breathing', 'Talk to someone', 'Write it out']), 'teal')], 10, 'margin-top:8px')))

# 9 --------------------------------------------------------------- conflict resolution
RES.append(R(K, 'conflict-resolution-guide', 'Conflict Resolution Guide', A, GD, ['relationships', 'anger'], 'Navigating disagreements',
    chat_ill('1.2in', '#2E9C95'), 'Conflict is normal. How we handle it decides whether it hurts a relationship or strengthens it.',
    ['Calm down first.', 'Use an I-statement.', 'Listen, then find a middle ground.'],
    '"I feel hurt when plans change last minute. Can we agree to text earlier?"',
    '<div class="box teal" style="text-align:center"><div class="lab">The I-statement</div><div style="font:600 13pt Fr,serif;line-height:1.7">I feel <u>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</u> when <u>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</u><br>because <u>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</u>. I need <u>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</u>.</div></div>' +
    '<div style="height:8px"></div>' + ''.join(numbox(i + 1, t, d, c) for i, ((t, d), c) in enumerate(zip([('Cool down', 'Take a break if you are heated. Come back in 20 minutes.'), ('Say your side', 'Use I-statements. No name-calling.'), ('Listen', 'Repeat back what you heard before replying.'), ('Find middle ground', 'What can both of us live with?')], ['tint', 'blue', 'tint', 'blue']))) +
    box('<div class="lab">A conflict I want to work on</div>' + lines(2, 22) + '<div class="lab" style="margin-top:6px">My I-statement:</div>' + lines(2, 22), 'sand', 'margin-top:6px')))

# 10 --------------------------------------------------------------- identity
RES.append(R(K, 'my-identity-and-values', 'My Identity & Values', A, REF, ['confidence'], 'Understanding personal identity',
    map_ill('1.2in', '#2E9C95'), 'Your identity is made of many parts: where you come from, what you love, and what you believe. Your values guide your choices.',
    ['Fill in each slice of the wheel.', 'Circle your top 5 values.', 'Notice where your actions match your values.'],
    '"Family: Nigerian-American, big on Sunday dinners. Interests: art, soccer. Value: honesty."',
    f'<div class="row" style="align-items:flex-start;gap:14px"><div class="center" style="width:3.5in">{wheel(["Family", "Culture", "Interests", "Strengths", "Beliefs", "Goals"], "3.4in")}<div class="small">Write in the slices.</div></div><div style="flex:1"><div class="lab">Circle your top 5 values</div><div>' + pills(['Honesty', 'Family', 'Kindness', 'Growth', 'Freedom', 'Loyalty', 'Creativity', 'Faith', 'Courage', 'Fairness', 'Respect', 'Adventure', 'Peace', 'Success', 'Health']) + '</div></div></div>' +
    grid(2, [box('<div class="lab">A time I acted on my values</div>' + lines(3, 22), 'sb'), box('<div class="lab">A time it was hard to</div>' + lines(3, 22), 'sb')], 10, 'margin-top:8px')))

# 11 --------------------------------------------------------------- friendships
RES.append(R(K, 'healthy-vs-unhealthy-friendships', 'Healthy vs. Unhealthy Friendships', A, GD, ['relationships'], 'Recognizing relationship patterns',
    heart_hands('1.2in'), 'Good friends support you and respect your limits. Notice how you feel around people, because your feelings are information.',
    ['Read both columns.', 'Think of a friendship and check what fits.', 'Decide one step: strengthen, set a boundary, or step back.'],
    '"After hanging out with Sam I feel good about myself. With Chris I feel nervous and put down."',
    '<div class="grid g2" style="gap:10px"><div class="box teal"><span class="stick" style="background:#1f7a74">Healthy</span>' + cbs(['They respect my no', 'They celebrate my wins', 'I can be myself', 'We solve problems together', 'Trust goes both ways', 'I feel good after we hang out']) + '</div><div class="box coral"><span class="stick" style="background:#c9604a">Unhealthy</span>' + cbs(['Teasing that hurts', 'Pressure to do things', 'Jealousy or control', 'Gossip or secrets shared', 'One-sided effort', 'I feel drained or anxious after']) + '</div></div>' +
    '<div class="box sb" style="margin-top:10px"><div class="lab">What does a healthy friendship look like to me?</div>' + lines(3, 22) + '</div>' +
    tbl(['Friend (initials only)', 'How I feel around them', 'My next step'], [['', '', '']] * 3, 38) +
    '<div class="box wb small" style="margin-top:8px">If a relationship involves threats, hurting you, or making you feel unsafe, tell a trusted adult right away.</div>'))

# 12 --------------------------------------------------------------- future vision
RES.append(R(K, 'my-future-vision', 'My Future Vision', A, ACT, ['confidence'], 'Exploring goals and aspirations',
    flag_ill('1.2in', '#2E9C95'), 'A vision is not a fixed plan. It is a direction. Start with what matters to you and take one small step at a time.',
    ['Dream big in the vision box.', 'Name 3 goals across time.', 'Choose the first small step.'],
    '"In 5 years: studying nursing. Step now: talk to the school counselor about programs."',
    '<div class="box sb" style="height:1.7in"><span class="stick">My vision board</span><div class="small" style="margin-top:3px">Draw, write, or paste pictures of what you want your future to feel and look like.</div></div>' +
    grid(3, [box('<div class="center"><span class="stick">This year</span></div>' + lines(3, 22), 'teal'), box('<div class="center"><span class="stick">In 5 years</span></div>' + lines(3, 22), 'sand'), box('<div class="center"><span class="stick">In 10 years</span></div>' + lines(3, 22), 'blue')], 8, 'margin-top:10px') +
    '<div class="box wb" style="margin-top:10px"><div class="lab">Obstacles I might face → how I\'ll handle them</div>' + lines(2, 22) + '<div class="lab" style="margin-top:4px">First small step I will take this week:</div>' + lines(1, 22) + '</div>'))

# ======================================================== interactive activities
RES.append(R(K, 'who-am-i-beyond-what-people-think', 'Who Am I Beyond What People Think of Me?', A, ACT, ['confidence'], 'Separating identity from others\' opinions',
    star_ill('1.2in', '#2E9C95'), 'What others say about you is not the whole truth. This activity helps you separate their view from your own.',
    ['Fill in what others say or assume about you.', 'Write what is actually true for you.', 'Circle the version that feels most like you.'],
    '"Others say: \'quiet.\' I know: I\'m thoughtful and I notice a lot."',
    tbl(['What people say or assume', 'What I know is true about me'], [['', '']] * 5, 44) +
    grid(2, [box('<div class="lab">Words I choose for myself</div>' + lines(3, 22), 'teal'), box('<div class="lab">Who I am becoming</div>' + lines(3, 22), 'sand')], 10, 'margin-top:10px') +
    '<div class="box wb center" style="margin-top:10px"><b>Your worth is not up for vote.</b></div>', group='activities'))

RES.append(R(K, 'things-i-wish-people-understood', 'Things I Wish People Understood About Me', A, REF, ['relationships', 'confidence'], 'Putting hard-to-say feelings into words',
    chat_ill('1.2in', '#2E9C95'), 'Sometimes it is hard to say what we need. Writing it out can help you share it, or just feel understood by yourself.',
    ['Complete each sentence honestly.', 'Choose one you want someone to know.', 'Decide who and how you might share it.'],
    '"I wish people knew that when I go quiet, I\'m not mad. I\'m recharging."',
    ''.join(f'<div class="box {c}" style="margin-bottom:8px"><span class="lab">{t}</span>{lines(2, 22)}</div>' for t, c in [('I wish people understood that…', 'teal'), ('When I feel stressed, what I need is…', 'sand'), ('Something I\'m really good at that people may not see…', 'blue'), ('Something that\'s hard for me right now…', 'lilac')]) +
    '<div class="box wb" style="margin-top:6px"><div class="lab">One thing I want to share, and with whom:</div>' + lines(2, 22) + '</div><div class="small" style="margin-top:6px">This page is private. Share only what and with whom feels safe.</div>', group='activities'))

RES.append(R(K, 'my-circle-of-influence', 'My Circle of Influence', A, ACT, ['stress', 'confidence'], 'Focusing on what you can influence',
    circles_control('1.3in'), 'You cannot control everything, but you can influence a lot. Focusing there reduces stress and builds power.',
    ['Write what you can control in the center.', 'Add what you can influence in the middle ring.', 'Put what you cannot control outside.'],
    '"I can\'t control the test grade, but I can control my studying and asking for help."',
    f'<div class="row" style="align-items:flex-start;gap:14px"><div class="center" style="width:3.4in">{circles_control("3.3in")}</div><div style="flex:1">' + box('<div class="lab">I control</div>' + lines(3, 22), 'sand') + '<div style="height:8px"></div>' + box('<div class="lab">I influence</div>' + lines(3, 22), 'teal') + '<div style="height:8px"></div>' + box('<div class="lab">I can\'t control</div>' + lines(3, 22), 'coral') + '</div></div>' +
    '<div class="box wb" style="margin-top:10px"><div class="lab">A worry I\'ll shift my energy away from, and what I\'ll do instead:</div>' + lines(2, 22) + '</div>', group='activities'))

RES.append(R(K, 'what-happens-when-i-compare-myself', 'What Happens When I Compare Myself to Others?', A, REF, ['confidence', 'anxiety'], 'Noticing the cost of comparison',
    scale_ill if False else magnifier_ill('1.2in', '#2E9C95'), 'Comparison can motivate us, but often it just makes us feel less than. Awareness helps you choose what to do with it.',
    ['Notice a recent comparison.', 'Write what you feel and think.', 'Flip it into something helpful.'],
    '"I compared my body to a post. I felt down. Flip: bodies are different; I\'ll focus on what mine does."',
    tbl(['Who / what I compared to', 'How it made me feel', 'What I told myself'], [['', '', '']] * 3, 44) +
    grid(2, [box('<div class="lab">What I don\'t see about them</div>' + lines(3, 22) + '<div class="small">Everyone has struggles you can\'t see.</div>', 'sand'), box('<div class="lab">Flip it: how I can use it</div>' + lines(3, 22) + '<div class="small">Inspiration, not a score.</div>', 'teal')], 10, 'margin-top:10px') +
    '<div class="box wb" style="margin-top:10px"><div class="lab">I am more than a comparison. Three things that are uniquely mine:</div>' + lines(3, 22) + '</div>', group='activities'))

chal = ['Compliment yourself', 'Say hi to someone new', 'Share an idea', 'Do something you avoid', 'Write 3 strengths', 'Ask for help', 'Try something new', 'Stand up straight', 'Set a boundary', 'Praise someone else', 'Take a break', 'Say no kindly', 'Celebrate a win', 'Speak up once', 'Wear what you love', 'Forgive a mistake', 'Learn something', 'Thank someone', 'Be kind to you', 'Move your body', 'Try a hard thing', 'Tell someone a truth', 'Make art', 'Help someone', 'Rest guilt-free', 'Reread your journal', 'Set a goal', 'Say \'I did that\'', 'Look in the mirror and smile', 'Reflect: what changed?']
cells = ''.join(f'<div class="box {"teal" if i%2==0 else "sand"}" style="padding:4px 5px;min-height:.62in"><div style="display:flex;justify-content:space-between"><b style="color:#17625d">{i+1}</b><i class="cb"></i></div><div style="font-size:7.8pt;line-height:1.2">{t}</div></div>' for i, t in enumerate(chal))
RES.append(R(K, '30-day-confidence-challenge', 'My 30-Day Confidence Challenge', A, ACT, ['confidence'], 'Building confidence through daily small actions',
    calendar_ill('1.2in', '#2E9C95'), 'Confidence is built by doing, not waiting to feel ready. One small action a day adds up.',
    ['Do the day\'s challenge. Adjust it to fit you.', 'Check the box when done.', 'Reflect at day 30.'],
    '"Day 6: asked for help. It was awkward, but my teacher was glad I did."',
    f'<div class="grid g5" style="gap:5px">{cells}</div>' + grid(2, [box('<div class="lab">My favorite challenge</div>' + lines(2, 20), 'sb'), box('<div class="lab">What changed for me</div>' + lines(2, 20), 'sb')], 10, 'margin-top:8px'), group='activities'))
