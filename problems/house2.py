import sympy as sp
# ROOM 1: ladder kinematics. Ladder length L, foot at (x,0), top at (0,y), angle theta with floor.
L,th,u,t=sp.symbols('L theta u t',positive=True)
x=L*sp.cos(th); y=L*sp.sin(th)
# foot moves right at u: dx/dt = u -> -L sin th thdot = u -> thdot = -u/(L sin th)
thd=-u/(L*sp.sin(th))
xc=x/2; yc=y/2
vcx=sp.diff(xc,th)*thd; vcy=sp.diff(yc,th)*thd
print("R1 centre vel", sp.simplify(vcx), sp.simplify(vcy), "speed", sp.simplify(sp.sqrt(vcx**2+vcy**2)))
print("R1 sweep", sp.simplify(thd), " top speed", sp.simplify(sp.diff(y,th)*thd))
# instantaneous centre: point P=(x,y) (foot's x, top's y); distance to centre = L/2
print("R1 IC dist to centre", sp.simplify(sp.sqrt((x-xc)**2+(y-yc)**2)))
# ROOM 2: rod length L mass m on ice, impulse J at one end perpendicular
m,J,s=sp.symbols('m J s',positive=True)
v=J/m; w=J*(L/2)/(m*L**2/12)
print("R2 v",v," omega",sp.simplify(w)," still point from centre", sp.simplify(v/w), " from struck end", sp.simplify(L/2+v/w))
KE=sp.Rational(1,2)*m*v**2+sp.Rational(1,2)*m*L**2/12*w**2
print("R2 KE", sp.simplify(KE), " punch", sp.simplify(sp.Rational(1,2)*m*v**2), " hook about centre", sp.simplify(sp.Rational(1,2)*m*L**2/12*w**2))
# numbers: m=0.60 kg, L=1.2 m, J=1.8 N s
num={m:sp.Rational(6,10),L:sp.Rational(12,10),J:sp.Rational(18,10)}
print("R2 nums v",v.subs(num)," w",w.subs(num)," still pt from struck end",(L/2+v/w).subs(num), " KE", KE.subs(num))
# ROOM 3: ladder dynamics, frictionless wall and floor, released from rest at th0
g,th0=sp.symbols('g theta0',positive=True)
thf=sp.symbols('thf',positive=True)
# energy: (1/2) m (L^2/3) thd^2 = m g (L/2)(sin th0 - sin th)
thd2=3*g*(sp.sin(th0)-sp.sin(th))/L
# wall force = m * d/dt(vcx). vcx = -(L/2) sin th thd ; horizontal velocity magnitude (L/2) sin th |thd|
# leaves wall when d/dt of (sin th * |thd|) = 0 -> maximize f = sin^2 th * thd2
f=sp.sin(th)**2*thd2
sol=sp.solve(sp.diff(f,th),th)
print("R3 critical", sol)
print("R3 check sin th = 2/3 sin th0:", sp.simplify(sp.diff(f,th).subs(sp.sin(th),2*sp.sin(th0)/3)))
# also via forces: N_wall = m * a_cx ; compute directly
T=sp.symbols('T')
thT=sp.Function('q')(T)
xcT=L*sp.cos(thT)/2
acx=sp.diff(xcT,T,2)
# substitute thd^2 and thdd from energy
qd=sp.Symbol('qd'); qdd=sp.Symbol('qdd'); q=sp.Symbol('q')
acx_e=acx.subs(sp.Derivative(thT,(T,2)),qdd).subs(sp.Derivative(thT,T),qd).subs(thT,q)
qdd_e=sp.diff(3*g*(sp.sin(th0)-sp.sin(q))/L,q)/2   # d(qd^2)/dq /2
Nw=sp.simplify(m*acx_e.subs({qdd:qdd_e, qd**2:3*g*(sp.sin(th0)-sp.sin(q))/L}))
Nw=sp.simplify(Nw.subs(qd, sp.sqrt(3*g*(sp.sin(th0)-sp.sin(q))/L)))
print("R3 wall force", sp.factor(Nw))
print("R3 Z about IC", sp.Rational(1,12)+sp.Rational(1,4), "L^2")
# numeric: th0 = 60 deg, L=1.2 -> height of top when it leaves: L sin th
th0n=sp.pi/3
hl=(L*2*sp.sin(th0n)/3).subs(L,sp.Rational(12,10))
print("R3 start height", sp.N((L*sp.sin(th0n)).subs(L,1.2)), " leaves at", sp.N(hl), " angle deg", sp.N(sp.asin(2*sp.sin(th0n)/3)*180/sp.pi))
# ROOM 4: superball, uniform solid sphere, rough elastic bounce.
# x to the right; ball moving +x at vx; omega positive = forward roll (clockwise looking with +x right, +y up).
R=sp.symbols('R',positive=True); vx,om,v1,w1=sp.symbols('v_x omega v1 w1',real=True)
I=sp.Rational(2,5)*m*R**2
# angular momentum about contact point (clockwise positive): m v R + I w
Leq=sp.Eq(m*vx*R+I*om, m*v1*R+I*w1)
Eeq=sp.Eq(m*vx**2+I*om**2, m*v1**2+I*w1**2)
sols=sp.solve([Leq,Eeq],[v1,w1],dict=True)
for s_ in sols: print("R4 bounce", sp.simplify(s_[v1]), "|", sp.simplify(s_[w1]))
s1=[s_ for s_ in sols if sp.simplify(s_[v1]-vx)!=0][0]
v2=sp.simplify(s1[v1].subs({vx:s1[v1],om:s1[w1]},simultaneous=True)); w2=sp.simplify(s1[w1].subs({vx:s1[v1],om:s1[w1]},simultaneous=True))
print("R4 second bounce", v2, w2)
# contact (bottom) point velocity before and after: v - R w (clockwise positive w gives bottom velocity v - R w)
print("R4 contact slip before", vx-R*om, " after", sp.simplify(s1[v1]-R*s1[w1]))
# numbers: thrown at 2.1 m/s with no spin, R = 0.025 m
n4={vx:sp.Rational(21,10),om:0,R:sp.Rational(25,1000)}
print("R4 nums first", s1[v1].subs(n4), sp.N(s1[w1].subs(n4)), " second", v2.subs(n4), w2.subs(n4))
# energy split after first bounce, per mass
print("R4 zip after", sp.simplify((s1[v1]**2/2).subs(om,0)), " hook per mass about centre", sp.simplify((sp.Rational(2,5)*R**2*s1[w1]**2/2).subs(om,0)))
# ROOM 5: ball radius b rolling without slipping inside fixed cylinder radius Rc, small oscillations
Rc,b,phi=sp.symbols('R_c b phi',positive=True)
# centre moves on circle radius Rc-b; rolling: b*w = (Rc-b)*phidot  (magnitudes)
# KE = 1/2 m ((Rc-b) phid)^2 + 1/2 (2/5 m b^2) w^2 = 1/2 m (7/5) (Rc-b)^2 phid^2
# equivalently: about contact Z = 7/5 b^2, sweep w = (Rc-b)phid/b
Zc=sp.Rational(7,5)*b**2
KEcoef=sp.simplify(Zc*((Rc-b)/b)**2)
print("R5 KE per mass coeff of phid^2/2:", KEcoef)
Om2=sp.simplify(g*(Rc-b)/KEcoef)
print("R5 omega^2 small osc", Om2, " period", sp.simplify(2*sp.pi/sp.sqrt(Om2)))
n5={g:sp.Rational(98,10),Rc:sp.Rational(30,100),b:sp.Rational(5,100)}
print("R5 nums period", sp.N((2*sp.pi/sp.sqrt(Om2)).subs(n5)), " sliding bead period", sp.N((2*sp.pi*sp.sqrt((Rc-b)/g)).subs(n5)))
# rolling sign check: ball inside fixed cylinder, centre moving counterclockwise about axis -> ball spins clockwise
# ROOM 5 check: acceleration of the marble's contact point points along the line to the marble's centre
T=sp.symbols('T'); p=sp.Function('p')(T)
# centre at (R-b)(sin p, -cos p); marble rotation angle chi with b*chi_dot = -(R-b) p_dot (turns opposite)
Rcs,bs=sp.symbols('R_c b',positive=True)
c=sp.Matrix([(Rcs-bs)*sp.sin(p), -(Rcs-bs)*sp.cos(p)])
chi=-(Rcs-bs)*p/bs   # material angle, up to const
# material point that is at contact at time T0: position c + b*(direction outward) where outward = (sin p, -cos p)
# general material point fixed in marble: offset b*(sin(chi+a), -cos(chi+a)), choose a so it's at contact at T0
a=sp.symbols('a')
P=c+bs*sp.Matrix([sp.sin(chi+a), -sp.cos(chi+a)])
vel=P.diff(T); acc=P.diff(T,2)
T0=sp.symbols('T0')
# contact condition: chi+a = p  at T0 -> a = p + (R-b)p/b at T0
sub_a={a:(p+(Rcs-bs)*p/bs)}
vel0=sp.simplify(vel.subs(sub_a)); acc0=sp.simplify(acc.subs(sub_a))
print("R5 contact vel", vel0.T)
d=(P-c).subs(sub_a)
cross=sp.simplify(acc0[0]*d[1]-acc0[1]*d[0])
print("R5 contact accel x offset (0 means along line to centre)", cross)
print("R5 accel along offset sign", sp.simplify((acc0.T*d)[0]))
