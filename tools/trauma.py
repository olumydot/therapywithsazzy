from rlib import *

K = 'trauma'
A = 'Adults & teens'
WS, GD, ACT, REF = 'Printable worksheet', 'Educational guide', 'Activity', 'Self-reflection'
RES = []
GENTLE = '<div class="box lilac small" style="margin-top:8px"><b>Go at your own pace.</b> Skip anything that feels like too much, and stop any time. Trauma education and self-help materials are not a substitute for individualized trauma-informed care.</div>'


def numbox(n, title, text, cls='tint'):
    return f'<div class="box {cls}" style="margin-bottom:7px;display:flex;gap:8px;align-items:flex-start"><span class="num">{n}</span><div><b>{title}</b><div style="font-size:10.5pt;line-height:1.35">{text}</div></div></div>'


def icon_tile(kind, color):
    paths = {
        'fight': '<path d="M52 10L26 52h20l-8 38 36-52H52z" fill="#fff" stroke="#16243a" stroke-width="4" stroke-linejoin="round"/>',
        'flight': '<path d="M12 50h62M52 28l26 22-26 22" fill="none" stroke="#16243a" stroke-width="8" stroke-linecap="round" stroke-linejoin="round"/>',
        'freeze': '<rect x="26" y="20" width="14" height="60" rx="4" fill="#fff" stroke="#16243a" stroke-width="4"/><rect x="58" y="20" width="14" height="60" rx="4" fill="#fff" stroke="#16243a" stroke-width="4"/>',
        'fawn': '<path d="M50 86S14 62 14 38a19 19 0 0 1 36-8 19 19 0 0 1 36 8c0 24-36 48-36 48z" fill="#fff" stroke="#16243a" stroke-width="4" stroke-linejoin="round"/>',
    }
    return f'<svg viewBox="0 0 100 100" style="width:.8in;height:.8in"><circle cx="50" cy="50" r="46" fill="{color}"/>{paths[kind]}</svg>'


# 1 ------------------------------------------------------------ understanding trauma (2 pages)
pg2 = cont(K, 'Understanding Trauma · What Helps',
    '<div class="grid g2" style="gap:10px"><div class="box teal"><div class="lab">What helps recovery</div>' + cbs(['Safety and predictability', 'Supportive relationships', 'Sleep, food, and movement', 'Learning how trauma affects the body', 'Gentle routines', 'Professional trauma-informed care', 'Patience with yourself']) + '</div><div class="box sand"><div class="lab">What does not help</div>' + bl(['Being told to "just get over it"', 'Forcing yourself to talk before you are ready', 'Isolating completely', 'Using alcohol or drugs to numb', 'Judging your reactions']) + '</div></div>' +
    '<div class="box wb" style="margin-top:10px"><div class="lab">Self-check: Have I noticed any of these lately?</div><div style="columns:2;font-size:10.5pt;margin-top:4px">' + cbs(['Trouble sleeping or nightmares', 'Feeling on edge or easily startled', 'Avoiding reminders', 'Feeling numb or disconnected', 'Strong guilt or shame', 'Difficulty trusting', 'Sudden strong emotions', 'Trouble concentrating']) + '</div><div class="small" style="margin-top:6px">Noticing these does not mean something is wrong with you. They are common responses. If they last or interfere with life, support can help.</div></div>' +
    '<div class="box blue" style="margin-top:10px"><div class="lab">When to reach out for help</div>' + bl(['Your reactions are getting in the way of daily life or relationships', 'You are having thoughts of harming yourself or others', 'You are using substances to cope', 'You feel stuck, hopeless, or unsafe']) + '<div class="small" style="margin-top:4px">Call or text <b>988</b> for crisis support, or <b>911</b> in an emergency.</div></div>' +
    '<div class="box lilac" style="margin-top:10px"><div class="lab">A reminder</div><div style="font:italic 12pt Fr,serif;line-height:1.5">Healing and growth do not have to happen all at once. Progress is not about perfection. It is about building safety and skills, one step at a time.</div></div>' + GENTLE, 'Part 2')
RES.append(R(K, 'understanding-trauma-a-beginners-guide', "Understanding Trauma: A Beginner's Guide", A, GD, ['trauma', 'emotional-regulation'], 'What trauma is, how it shows up, and why healing is possible',
    anchor_ill('1.2in', '#7B6AAE'), 'Trauma is a lasting response to an overwhelming experience. It is about what happened to you, not what is wrong with you.',
    ['Read the guide at your own pace.', 'Notice what feels familiar. No pressure to share.', 'Continue to page 2 for what helps.'],
    '"I used to think I was overreacting. Learning about trauma helped me see my reactions made sense."',
    '<div class="box lilac"><div class="lab">What is trauma?</div><div style="font-size:10.5pt;line-height:1.45">Trauma is the emotional and physical response to an event or series of events that overwhelmed your ability to cope and felt threatening or unsafe. What makes something traumatic is not only the event, but how it affected you and whether you had support afterward.</div></div>' +
    '<div class="lab" style="margin:10px 0 5px">Types of trauma</div>' + grid(4, [box(f'<b>{t}</b><div class="small">{d}</div>', c) for t, d, c in [('Single event', 'An accident, assault, disaster, or sudden loss', 'coral'), ('Repeated', 'Ongoing experiences, such as abuse or violence', 'sand'), ('Complex', 'Prolonged, often early in life and within relationships', 'blue'), ('Developmental', 'Early neglect or unsafe caregiving', 'teal')]], 8) +
    '<div class="lab" style="margin:10px 0 5px">How it can show up</div>' + grid(4, [box(f'<b>{t}</b>' + bl(i), 'tint') for t, i in [('Body', ['Tension, fatigue', 'Startle response', 'Sleep trouble']), ('Emotions', ['Fear, anger', 'Numbness', 'Shame']), ('Thoughts', ['Flashbacks', 'Self-blame', 'Hypervigilance']), ('Behavior', ['Avoidance', 'Withdrawal', 'Irritability'])]], 8) + GENTLE, start=True, extra=(pg2,), z=1.0))

# 2 ------------------------------------------------------------ complex trauma
RES.append(R(K, 'what-is-complex-trauma', 'What Is Complex Trauma?', A, GD, ['trauma', 'relationships'], 'Understanding repeated, long-term trauma',
    puzzle_ill('1.2in', '#7B6AAE'), 'Complex trauma comes from repeated or long-lasting experiences, often in relationships and early in life. It can shape how we see ourselves and others.',
    ['Read about how complex trauma differs.', 'Notice patterns, not labels.', 'Consider support from a trauma-informed professional.'],
    '"I learned to stay quiet to stay safe. As an adult it made speaking up feel dangerous."',
    '<div class="grid g2" style="gap:10px"><div class="box coral"><div class="lab">Single-event trauma</div>' + bl(['One overwhelming event', 'Clear "before and after"', 'Often involves fear and flashbacks']) + '</div><div class="box lilac"><div class="lab">Complex trauma</div>' + bl(['Repeated or ongoing experiences', 'Often early life, in relationships', 'Can affect identity and trust', 'Can affect emotional regulation']) + '</div></div>' +
    '<div class="lab" style="margin:10px 0 5px">Areas it can affect</div>' + grid(4, [box(f'<div class="center"><b>{t}</b><div class="small">{d}</div></div>', c) for t, d, c in [('Self-view', 'Shame, feeling "not enough"', 'blue'), ('Relationships', 'Trust, closeness, boundaries', 'teal'), ('Emotions', 'Intensity, numbness, mood swings', 'sand'), ('Body', 'Chronic tension, health issues', 'coral')]], 8) +
    '<div class="box wb" style="margin-top:10px"><div class="lab">Strengths that come from surviving</div>' + cbs(['Being observant', 'Resourcefulness', 'Empathy', 'Independence', 'Determination', 'Creativity']) + '<div class="small" style="margin-top:4px">The strategies that kept you safe made sense then. Healing means building new options.</div></div>' +
    box('<div class="lab">Reflect (only if it feels okay)</div><div class="small">What strengths helped me get through hard times?</div>' + lines(2, 22), 'sb', 'margin-top:8px') + GENTLE))

# 3 ------------------------------------------------------------ FFFF
fx = [('Fight', 'fight', '#f3cfc4', ['Anger, irritability', 'Arguing, controlling', 'Feeling tense and ready to defend'], 'Safe ways to release energy, assertive communication'), ('Flight', 'flight', '#fbe3a8', ['Anxiety, restlessness', 'Staying busy, perfectionism', 'Avoiding or escaping'], 'Slowing down, grounding, facing small steps'),
      ('Freeze', 'freeze', '#d6d1e4', ['Feeling stuck or numb', 'Going blank, spacing out', 'Difficulty acting or speaking'], 'Gentle movement, orienting, warmth, safe company'), ('Fawn', 'fawn', '#cfe0f5', ['People-pleasing', 'Difficulty saying no', 'Putting others\' needs first to stay safe'], 'Practicing boundaries, naming your needs')]
RES.append(R(K, 'fight-flight-freeze-and-fawn', 'Understanding Fight, Flight, Freeze, and Fawn', A, GD, ['trauma', 'anxiety', 'emotional-regulation'], 'Recognizing automatic survival responses',
    dial_ill('1.3in', '#7B6AAE'), 'When your brain senses danger, it can automatically respond in one of four ways. These are survival reactions, not character flaws.',
    ['Read the four responses.', 'Circle the ones you notice in yourself.', 'Note what helps you shift back to safe.'],
    '"I always say yes to everything. I learned it\'s a fawn response, a way I kept the peace."',
    '<div class="grid g2" style="gap:10px">' + ''.join(f'<div class="box" style="background:{bg};border-color:transparent"><div class="row">{icon_tile(ic, "#ffffff")}<div style="font:600 18pt Fr,serif;color:#16243a">{n}</div></div>{bl(sym)}<div class="small" style="margin-top:4px"><b>Helps:</b> {h}</div></div>' for n, ic, bg, sym, h in fx) + '</div>' +
    grid(2, [box('<div class="lab">The response I notice most in me</div>' + lines(2, 22), 'sb'), box('<div class="lab">What helps me come back to safe</div>' + lines(2, 22), 'sb')], 10, 'margin-top:10px') + GENTLE))

# 4 ------------------------------------------------------------ triggers
chain = ['A reminder (sight, sound, smell, words)', 'My body reacts (heart, tension, stomach)', 'My mind tells a story ("I\'m in danger")', 'I react (shut down, snap, escape)']
RES.append(R(K, 'understanding-emotional-triggers', 'Understanding Emotional Triggers', A, WS, ['trauma', 'emotional-regulation', 'anxiety'], 'Tracing how reminders lead to reactions',
    magnifier_ill('1.2in', '#7B6AAE'), 'A trigger is a reminder, often outside of awareness, that sets off a strong reaction tied to past experiences. Tracing the chain gives you more choice.',
    ['Notice a strong reaction.', 'Trace the chain step by step.', 'Choose a grounding tool and a kind response.'],
    '"The smell of smoke (trigger) made my heart race and I felt unsafe. I used the 5-4-3-2-1 skill."',
    '<div class="row" style="gap:6px;align-items:stretch">' + ''.join(f'<div class="box lilac" style="flex:1;text-align:center"><span class="num" style="margin:0 auto 3px">{i+1}</span><div style="font-size:10pt">{c}</div></div>' + ('<div style="align-self:center;font-weight:700;color:#4a3d80">&rarr;</div>' if i < 3 else '') for i, c in enumerate(chain)) + '</div>' +
    tbl(['What reminded me', 'What my body did', 'What my mind said', 'What I did', 'What could help'], [['', '', '', '', '']] * 4, 42) +
    grid(2, [box('<div class="lab">Common triggers (check any)</div>' + cbs(['Certain places', 'Smells or sounds', 'Anniversaries', 'Raised voices', 'Feeling trapped', 'Being touched unexpectedly']), 'sand'), box('<div class="lab">Patterns I notice</div>' + lines(4, 22), 'sb')], 10, 'margin-top:10px') + GENTLE))

# 5 ------------------------------------------------------------ grounding
tech = [('5-4-3-2-1', 'Name 5 things you see, 4 you feel, 3 you hear, 2 you smell, 1 you taste.'), ('Feet on the floor', 'Press your feet down. Notice the floor holding you.'), ('Cool it down', 'Hold something cold or splash cool water on your face.'), ('Orient to the room', 'Slowly look around. Name where you are and today\'s date.'),
        ('Longer exhale', 'Breathe in for 4, out for 6 to 8. Repeat 5 times.'), ('Hold an object', 'Choose a small item. Describe its texture, weight, and color.'), ('Categories', 'Pick a category (animals, cities). Name as many as you can.'), ('Butterfly hug', 'Cross arms over chest. Tap alternate hands slowly.')]
RES.append(R(K, 'grounding-techniques-for-emotional-distress', 'Grounding Techniques for Emotional Distress', A, GD, ['trauma', 'anxiety', 'emotional-regulation', 'stress'], 'Using the senses and body to settle strong emotions',
    anchor_ill('1.2in', '#7B6AAE'), 'Grounding brings your attention to the present, where you are safe now. Practice when you are calm so the skills are ready when you need them.',
    ['Rate your distress from 0 to 10.', 'Try a technique for 1 to 3 minutes.', 'Rate again and note what helped.'],
    '"Distress 8. I did cold water and feet on the floor. After: 5."',
    '<div class="grid g4" style="gap:7px">' + ''.join(f'<div class="box {c}" style="padding:7px 9px"><div class="row" style="gap:5px"><span class="num" style="width:20px;height:20px;font-size:8.5pt">{i+1}</span><b style="font-size:10pt">{t}</b></div><div style="font-size:9.5pt;line-height:1.3;margin-top:2px">{d}</div></div>' for i, ((t, d), c) in enumerate(zip(tech, ['lilac', 'teal', 'blue', 'sand', 'lilac', 'teal', 'blue', 'sand']))) + '</div>' +
    '<div class="lab" style="margin-top:10px">Practice log</div>' + tbl(['What I used', 'Distress before (0-10)', 'Distress after (0-10)', 'What I noticed'], [['', '', '', '']] * 4, 34) +
    '<div class="box wb" style="margin-top:8px"><div class="lab">My top 3 grounding tools:</div><div class="line"></div></div>' + GENTLE, start=True))

# 6 ------------------------------------------------------------ window of tolerance
RES.append(R(K, 'the-window-of-tolerance', 'The Window of Tolerance', A, GD, ['trauma', 'emotional-regulation', 'stress'], 'Understanding the zone where you can cope',
    zone_ill('1.2in'), 'The window of tolerance is the zone where you can feel your emotions and think clearly. Stress and trauma can push you out of it, in either direction.',
    ['Find where you are right now.', 'Note signs of being above or below the window.', 'Choose a tool to return.'],
    '"I\'m above my window: racing heart, snapping. A long exhale and a walk helped."',
    f'<div class="box" style="padding:6px">{window_chart()}</div>' +
    '<div class="grid g3" style="gap:8px;margin-top:8px"><div class="box coral"><div class="lab">Too much</div><div class="small">Tools that calm down</div>' + bl(['Long exhale', 'Cool water', 'Slow walking']) + '</div><div class="box teal"><div class="lab">In the window</div><div class="small">Tools that keep you here</div>' + bl(['Routines', 'Connection', 'Rest', 'Mindfulness']) + '</div><div class="box lilac"><div class="lab">Too little</div><div class="small">Tools that gently activate</div>' + bl(['Stretching', 'Music', 'Talking to someone', 'Cold or sensory cues']) + '</div></div>' +
    grid(2, [box('<div class="lab">Signs I am above my window</div>' + lines(1, 22), 'sb'), box('<div class="lab">Signs I am below my window</div>' + lines(1, 22), 'sb')], 10, 'margin-top:8px') + GENTLE))

# 7 ------------------------------------------------------------ dissociation
RES.append(R(K, 'understanding-dissociation', 'Understanding Dissociation', A, GD, ['trauma', 'emotional-regulation'], 'Recognizing and responding to feeling disconnected',
    brain_ill('1.2in', '#7B6AAE'), 'Dissociation is the mind\'s way of creating distance from overwhelming experiences. It can feel like spacing out, numbness, or being detached from yourself or surroundings.',
    ['Read the spectrum.', 'Notice what triggers it for you.', 'Practice gentle ways to come back.'],
    '"When I\'m overwhelmed, I go blank. Naming objects in the room helps me come back."',
    '<div class="lab">A spectrum, from common to more intense</div>' + '<div class="row" style="gap:0;margin:6px 0">' + ''.join(f'<div style="flex:1;background:{c};padding:8px;text-align:center;font-size:10pt"><b>{t}</b></div>' for t, c in [('Daydreaming', '#e6f4f1'), ('Zoning out', '#ebe7f5'), ('Feeling numb', '#d6d1e4'), ('Feeling detached or unreal', '#c9bfe3')]) + '</div>' +
    grid(2, [box('<div class="lab">What it can feel like</div>' + bl(['Spacing out, going blank', 'Feeling numb or far away', 'Time passing strangely', 'Feeling like things are not real', 'Gaps in memory']), 'lilac'), box('<div class="lab">Ways to come back gently</div>' + bl(['Feel your feet and hands', 'Name 5 things you see', 'Hold something cold', 'Say your name, date, and place', 'Move slowly: stretch, walk']), 'teal')], 10) +
    grid(2, [box('<div class="lab">What tends to lead to it for me</div>' + lines(3, 22), 'sb'), box('<div class="lab">What helps me return</div>' + lines(3, 22), 'sb')], 10, 'margin-top:10px') +
    '<div class="warn" style="margin-top:8px"><b>When to seek help:</b> If dissociation is frequent, long-lasting, or affects daily life or safety, talk with a trauma-informed professional.</div>' + GENTLE))

# 8 ------------------------------------------------------------ reconnecting with body
RES.append(R(K, 'reconnecting-with-your-body', 'Reconnecting With Your Body', A, ACT, ['trauma', 'emotional-regulation', 'stress'], 'Rebuilding a sense of safety in the body',
    lungs_ill('1.2in', '#7B6AAE'), 'After trauma, the body can feel unsafe or numb. Gentle, choice-based practices can rebuild trust with your body, a little at a time.',
    ['Choose one practice and a comfortable length.', 'Notice sensations without judging.', 'Stop whenever you want. You are in charge.'],
    '"I noticed my hands were warm. It was the first calm sensation I felt all week."',
    f'<div class="row" style="align-items:flex-start;gap:14px"><div class="center" style="width:2.2in">{body_outline("2in")}<div class="small">Mark areas that feel okay (✓), neutral (○), or uncomfortable (×).</div></div><div style="flex:1">' + ''.join(numbox(i + 1, t, d, c) for i, ((t, d), c) in enumerate(zip([('Feel your feet', 'Press them down; notice weight and temperature.'), ('Notice your hands', 'Rub palms together. Feel warmth and texture.'), ('Follow your breath', 'Without changing it, notice where it moves.'), ('Orient', 'Slowly look around and name what feels safe.'), ('Gentle movement', 'Stretch, sway, or walk slowly.')], ['lilac', 'teal', 'blue', 'sand', 'lilac']))) + '</div></div>' +
    grid(2, [box('<div class="lab">A part of my body that feels okay</div>' + lines(2, 22), 'sb'), box('<div class="lab">What I noticed after practicing</div>' + lines(2, 22), 'sb')], 10, 'margin-top:6px') + GENTLE))

# 9 ------------------------------------------------------------ emotional safety
RES.append(R(K, 'building-emotional-safety', 'Building Emotional Safety', A, WS, ['trauma', 'relationships', 'emotional-regulation'], 'Creating safety inside you, around you, and with others',
    shield_ill('1.2in', '#7B6AAE'), 'Healing happens in safety. Safety is built in three places: in your body and mind, in your surroundings, and in your relationships.',
    ['Check what already helps you feel safe.', 'Pick one thing to add in each area.', 'Revisit as your needs change.'],
    '"Safe space: my bedroom with soft lighting. Safe person: my cousin. Inner: a calming phrase."',
    grid(3, [box('<div class="center"><span class="stick" style="background:#4a3d80">Inside me</span></div>' + cbs(['Slow breathing', 'Calming phrases', 'Self-kindness', 'Grounding tools', 'Rest']), 'lilac'), box('<div class="center"><span class="stick" style="background:#17625d">Around me</span></div>' + cbs(['A safe place', 'Predictable routine', 'Locks and lighting', 'Limited triggers', 'Comfort items']), 'teal'), box('<div class="center"><span class="stick" style="background:#223e7a">With others</span></div>' + cbs(['A trusted person', 'Clear boundaries', 'Respectful listeners', 'Support groups', 'Professional help']), 'blue')], 8) +
    grid(2, [box('<div class="lab">My safe place (describe or draw)</div><div style="height:1.4in"></div>', 'sb'), box('<div class="lab">Safe people I can turn to</div>' + lines(3, 22) + '<div class="lab" style="margin-top:6px">A calming phrase I can use:</div>' + lines(1, 22), 'sb')], 10, 'margin-top:10px') +
    '<div class="box wb" style="margin-top:8px"><div class="lab">One thing I will add this week to feel safer:</div>' + lines(2, 22) + '</div>' + GENTLE))

# 10 ------------------------------------------------------------ attachment
att = [('Secure', 'Comfortable with closeness and independence', 'Trusting, communicates needs', 'teal'), ('Anxious', 'Worries about being left or not enough', 'Seeks reassurance, fears distance', 'sand'), ('Avoidant', 'Values independence, uneasy with closeness', 'Withdraws when things get intense', 'blue'), ('Fearful', 'Wants closeness but fears getting hurt', 'Mixed signals, pulls close then away', 'lilac')]
RES.append(R(K, 'understanding-attachment-and-relationships', 'Understanding Attachment and Relationships', A, GD, ['trauma', 'relationships'], 'How early relationships shape how we connect',
    people_ill('1.3in', '#7B6AAE'), 'Attachment patterns form early and shape how we connect as adults. They are not fixed. Relationships and healing can change them.',
    ['Read the four common patterns.', 'Notice which feel familiar, perhaps in different relationships.', 'Think about what helps you feel secure.'],
    '"I tend to pull away when things get close. Now I tell my partner, \'I need a little space, and I\'m not going anywhere.\'"',
    '<div class="grid g2" style="gap:10px">' + ''.join(f'<div class="box {c}"><span class="stick" style="background:#4a3d80">{t}</span><div style="margin-top:4px;font-size:10.5pt"><b>Looks like:</b> {a}</div><div style="font-size:10.5pt"><b>Often:</b> {b}</div></div>' for t, a, b, c in att) + '</div>' +
    grid(2, [box('<div class="lab">Patterns I notice in my relationships</div>' + lines(3, 22), 'sb'), box('<div class="lab">What helps me feel secure</div>' + cbs(['Clear communication', 'Consistency', 'Space and closeness', 'Reassurance', 'Honesty', 'Repair after conflict']), 'sb')], 10, 'margin-top:10px') +
    '<div class="box wb small" style="margin-top:8px">These are common patterns, not labels or diagnoses. Most people show different patterns in different relationships. Therapy can help you build more secure ways of connecting.</div>' + GENTLE))

# 11 ------------------------------------------------------------ safety plan
RES.append(R(K, 'developing-a-personal-safety-plan', 'Developing a Personal Safety Plan', A, WS, ['trauma', 'stress', 'anxiety'], 'Preparing for the hardest moments',
    shield_ill('1.2in', '#7B6AAE'), 'A safety plan is a short list of steps you can follow when distress feels too big. Make it when you are calm, ideally with a trusted person or counselor.',
    ['Fill it out step by step.', 'Share it with someone you trust.', 'Keep it somewhere you can reach quickly.'],
    '"Step 2: put on my headphones and walk. Step 4: call Maria."',
    ''.join(f'<div class="row" style="margin-bottom:6px;align-items:stretch"><span class="num" style="margin-top:4px">{i+1}</span><div class="box {c}" style="flex:1;padding:5px 10px"><span class="lab">{t}</span><div class="line" style="height:21px"></div></div></div>' for i, (t, c) in enumerate([('My warning signs (thoughts, feelings, situations)', 'coral'), ('Things I can do on my own to calm down', 'teal'), ('People and places that help me feel better', 'sand'), ('People I can ask for help (names and numbers)', 'blue'), ('Professionals I can contact', 'lilac'), ('How I will make my space safer', 'tint'), ('My reasons for living / what matters to me', 'sand')])) +
    '<div class="warn" style="margin-top:6px"><b>988 Suicide &amp; Crisis Lifeline:</b> call or text <b>988</b> any time. <b>Crisis Text Line:</b> text HOME to <b>741741</b>. <b>Emergency:</b> call <b>911</b> or go to your nearest emergency department.</div>' + GENTLE, z=1.0))

# 12 ------------------------------------------------------------ self-care recovery plan
areas = [('Physical', 'Sleep, food, movement, medical care'), ('Emotional', 'Feelings, journaling, therapy, creative outlets'), ('Social', 'Connection, boundaries, support groups'), ('Spiritual / meaning', 'Faith, values, nature, purpose'), ('Practical', 'Routines, finances, organization, safety'), ('Rest & joy', 'Play, hobbies, quiet, laughter')]
RES.append(R(K, 'creating-a-self-care-and-recovery-plan', 'Creating a Self-Care and Recovery Plan', A, WS, ['trauma', 'stress', 'confidence'], 'Building a sustainable routine for healing',
    plant_ill('1.2in', '#7B6AAE'), 'Recovery is built through small, steady habits. A plan helps you protect your energy and notice progress.',
    ['Choose one action per area.', 'Schedule it into your week.', 'Review monthly and adjust.'],
    '"Physical: 10-minute walk after lunch. Social: Sunday call with my sister."',
    tbl(['Area of care', 'One action I will take', 'When'], [[f'<b>{a}</b><div class="small">{d}</div>', '', ''] for a, d in areas], 46) +
    grid(2, [box('<div class="lab">Signs I am doing better</div>' + lines(3, 22), 'teal'), box('<div class="lab">Signs I need extra support</div>' + lines(3, 22), 'coral')], 10, 'margin-top:10px') +
    '<div class="box wb" style="margin-top:8px"><div class="lab">A kind message to myself on hard days:</div>' + lines(2, 22) + '</div>' + GENTLE))
