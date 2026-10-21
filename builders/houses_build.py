import re,textwrap
O='/home/claude/out/'
H=open(O+'Claude The Haunted Problem Set 2610192207.txt').read().split('\n')
S2=open(O+'Claude The Second House Solutions 2610200657.txt').read()

def omega(t):
    return re.sub(r'\bZ\b','Ω',t)

# ---------- Haunted: slice the rooms
def block(start,end): return '\n'.join(H[start-1:end])
# line numbers (1-based) from the original: rooms start at 24,63,100,196,273,366
rooms={1:(24,62),2:(63,99),3:(100,195),4:(196,272),5:(273,365)}
def split_room(n):
    a,b=rooms[n]
    lines=H[a-1:b]
    head=lines[:2]
    # statement = indented block following heading
    i=3
    while lines[i].strip()=='' : i+=1
    st=[]
    while i<len(lines) and (lines[i].startswith('    ') or lines[i].strip()==''):
        st.append(lines[i]); i+=1
        if lines[i-1].strip()=='' and i<len(lines) and not lines[i].startswith('    '): break
    body=lines[i:]
    return head,[l for l in st],body
parts={n:split_room(n) for n in rooms}

# ---------- Problems (Haunted)
P=[]
P+=["THE HAUNTED PROBLEM SET: PROBLEMS","=================================","",
"Written by Claude (Anthropic), 2026-10-20 STAMPT. The five problems",
"of The Haunted Problem Set, statements only; the worked solutions",
"are in The Haunted Solutions STAMP. Not doc's text. The statements",
"are paraphrased from MIT OpenCourseWare 8.01SC (Fall 2016), Problem",
"Set 12; the figures aren't reproduced, and where a figure set the",
"geometry (problems 2 and 4) the problem says what it assumes.","",
"Use g = 10 m/s^2.",""]
stm={
1:["1. The bicycle wheel","--------------------","",
"    A wheel of radius R rolls without slipping on level ground, its",
"    centre moving at steady speed V in the +x direction. A bead on",
"    the rim is at the top, at (x0, 2R), when t = 0.",
"    (a) Find the bead's coordinates x(t) and y(t) for an observer",
"        on the ground.",
"    (b) Find the bead's velocity at the top and at the bottom of",
"        the wheel, and say what it means for the bottom.",""],
2:["2. The ball in the ring","-----------------------","",
"    A ball of radius b rolls without slipping on the inside of a",
"    ring of radius R > b. The ball turns at angular speed omega_b",
"    about its own centre, and the ring turns at angular speed",
"    omega_r about its centre. Find the speed of the ball's centre.",
"",
"    (The figure isn't reproduced. This version takes the ball",
"    against the inside of the ring, with omega_b, omega_r and the",
"    centre's motion all counted counterclockwise as we look.)",""],
3:["3. The cube that meets a ridge","------------------------------","",
"    A uniform cube of mass m and edge s slides without friction at",
"    speed v across a level floor and hits a low ridge with its",
"    leading bottom edge. The collision is instantaneous and",
"    inelastic: afterward the cube pivots freely about the ridge.",
"    Its moment of inertia about an axis through the centres of two",
"    opposite faces is m s^2 / 6.",
"    (a) Find the cube's angular speed just after the collision.",
"    (b) Find the largest v, call it v_max, for which the cube",
"        does not tip over the ridge.",
"    (c) Find the fraction of the cube's kinetic energy that",
"        survives the collision.",
"    (d) Give v_max for s = 0.30 m.",
"",
"    (This version takes the ridge's height as negligible.)",""],
4:["4. The yo-yo on the slope","-------------------------","",
"    A yo-yo of mass m has rims of radius R, an axle of radius R/3,",
"    and moment of inertia m R^2 / 2 about its centre. It sits on a",
"    slope at angle phi, and its string is pulled with force F. The",
"    coefficient of static friction is mu_s. Find the largest F for",
"    which the yo-yo rolls without slipping, and the smallest.",
"",
"    (The figure isn't reproduced. This version takes the string",
"    leaving the top of the axle and pulled up the slope, parallel",
"    to it.)",""],
5:["5. The billiard ball that skids","-------------------------------","",
"    A uniform ball of mass m and radius R, moment of inertia",
"    2 m R^2 / 5 about its centre, is struck by a cue: a sharp",
"    horizontal blow at height h above its centre line. It leaves",
"    the cue with speed v0 and some rotation, skids, and when it",
"    finally rolls without slipping its speed is 9 v0 / 7.",
"    (a) Find h / R.",
"    (b) For v0 = 2.1 m/s, find the speed with which the ball",
"        rolls away and the energy burned in the skid for each",
"        kilogram of ball.",
"    (c) At what height h would the ball roll at once, with no",
"        skid? What happens for a blow higher, and for one lower?",""]}
for n in range(1,6): P+=stm[n]
P+=["Source: MIT OpenCourseWare 8.01SC Classical Mechanics, Fall 2016,",
"Problem Set 12 (Bicycle Wheel; Rolling Without Slipping; Cubical",
"Block Collision with Low Ridge; Yo-yo Rolling on Inclined Plane;",
"Billiards). Statements paraphrased; parts added to some; geometry",
"for problems 2 and 4 assumed as stated."]
open('hp.txt','w').write('\n'.join(P)+'\n')

# ---------- Solutions (Haunted)
intro=H[11:23]   # "Five rooms..." paragraph, lines 12..23
intro='\n'.join(intro)
SOL=["THE HAUNTED PROBLEM SET: SOLUTIONS","==================================","",
"Written by Claude (Anthropic), 2026-10-20 STAMPT. Worked solutions",
"to the five problems in The Haunted Problems STAMP, in stealth",
"mode: each one starts in the textbook's terms and ends a little",
"further into dr. kraemer's straight-> mechanics vocabulary. Not",
"doc's manuscript text; the ideas and vocabulary are his, these",
"words are the model's.",""]
SOL.append(intro.strip('\n')); SOL.append('')
for n in range(1,6):
    head,st,body=parts[n]
    SOL+=head+['']
    SOL+=[l for l in body]
t='\n'.join(SOL)

# register + side by side (rooms 6,7)
tail='\n'.join(H[365:421])
t+='\n'+tail+'\n'
t+="\nProblem Set 12 is MIT OpenCourseWare 8.01SC Classical Mechanics,\nFall 2016. Answers checked symbolically.\n"
open('hs_raw.txt','w').write(t)
