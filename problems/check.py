import sympy as sp, numpy as np
from scipy.integrate import solve_ivp
g=10.0
print("===== P1 =====")
m,R,v0,mu=1.0,0.05,2.1,0.20
I=sp.Rational(2,5)*m*R**2
h=sp.symbols('h')
vf=sp.Rational(9,7)*v0
# floor-line spin: blow m v0 levered at R+h equals rolling spin (I+mR^2) vf/R
hs=sp.solve(sp.Eq(m*v0*(R+h),(I+m*R**2)*vf/R),h)[0]
print("h",hs,"h/R",hs/R)
w0=m*v0*hs/I; wf=vf/R
print("I",I,"w0",w0,"wf",wf,"vf",vf,"spin0",I*w0,"spinf",I*wf)
# general check: final speed formula
H=sp.symbols('H'); V=sp.symbols('V',positive=True)
Ig=sp.Rational(2,5)*R**2
print("vf general", sp.simplify((V*(R+H))/(Ig+R**2)*R))
f=mu*m*g
def rhs(t,y):
    v,w,x=y; slip=R*w-v  # contact slides backward at slip
    s=np.sign(slip)
    return [s*f/m, -s*f*R/float(I), v]
ev=lambda t,y: R*y[1]-y[0]; ev.terminal=True
sol=solve_ivp(rhs,[0,2],[v0,float(w0),0],events=ev,rtol=1e-12,atol=1e-14)
ts=sol.t_events[0][0]; ys=sol.y_events[0][0]
print("num: t",ts,"v",ys[0],"w",ys[1],"x",ys[2])
print("analytic: t",0.3,"v",2.7,"w",54,"x",0.72)
print("dev", ts-0.3, ys[0]-2.7, ys[1]-54, ys[2]-0.72)
K0=0.5*m*v0**2+0.5*float(I)*float(w0)**2
Kf=0.5*m*2.7**2+0.5*float(I)*54**2
print("K0",K0,"Kf",Kf,"lost",K0-Kf,"frac",(K0-Kf)/K0, 10/91)
print("roll-at-once h", sp.solve(sp.Eq(m*v0*h/I, v0/R),h))

print("===== P2 =====")
R2,b=0.30,0.05; L=R2-b
w2=np.sqrt(g/(1.4*L)); wb=np.sqrt(g/L)
print("ring",w2,"T",2*np.pi/w2,"bead ring",wb,"T",2*np.pi/wb,"ratio",wb/w2,np.sqrt(1.4))
# independent: Newton-Euler for ball in trough. centre at L(sin psi, -cos psi).
# unknown friction F tangential, ball sweep Om (ccw). Constraint: contact point velocity zero.
# Use symbolic derivation
psi,dpsi,dd,Ff,Nn,al=sp.symbols('psi dpsi dd F N al')
mm=1
# tangential direction e_t=(cos,sin), radial outward e_r=(sin,-cos)
# tangential eq: m L dd = -m g sin psi + F
# ball rotation ccw: I*al = torque of F at contact (contact at +b e_r from centre): r x F = b e_r x F e_t = b F (e_r x e_t)_z
er=sp.Matrix([sp.sin(psi),-sp.cos(psi),0]); et=sp.Matrix([sp.cos(psi),sp.sin(psi),0])
tz=(b*er).cross(Ff*et)[2]
# no slip: v_centre + Om x (b e_r) =0 ; v_centre = L dpsi e_t ; Om z x b e_r = Om b (z x e_r)
zxer=sp.Matrix([0,0,1]).cross(er)
Om=sp.symbols('Om')
nos=sp.solve(sp.Eq((L*dpsi*et+Om*b*zxer)[0],0),Om)[0]
print("ball sweep (ccw)",sp.simplify(nos))
# al = d/dt nos = factor*dd
fac=sp.simplify(nos/dpsi)
eqs=[sp.Eq(mm*L*dd,-mm*g*sp.sin(psi)+Ff), sp.Eq(sp.Rational(2,5)*mm*b**2*fac*dd, tz)]
s=sp.solve(eqs,[dd,Ff],dict=True)[0]
print("psi'' =",sp.simplify(s[dd]), " coeff",sp.nsimplify(sp.simplify(s[dd]/sp.sin(psi))))
fdd=sp.lambdify(psi,s[dd])
sol=solve_ivp(lambda t,y:[y[1],fdd(y[0])],[0,20],[0.01,0],rtol=1e-12,atol=1e-14,dense_output=True)
tt=np.linspace(0,20,200001); yy=sol.sol(tt)[0]
# zero crossings up
zc=[tt[i] for i in range(len(tt)-1) if yy[i]<0<=yy[i+1]]
Tn=np.mean(np.diff(zc)); print("num period ball",Tn,"dev",Tn-2*np.pi/w2)
sol=solve_ivp(lambda t,y:[y[1],-g/L*np.sin(y[0])],[0,20],[0.01,0],rtol=1e-12,atol=1e-14,dense_output=True)
yy=sol.sol(tt)[0]; zc=[tt[i] for i in range(len(tt)-1) if yy[i]<0<=yy[i+1]]
Tb=np.mean(np.diff(zc)); print("num period bead",Tb,"dev",Tb-2*np.pi/wb)
print("profiles card: centre",L**2/0.01,"ball own",0.4*b**2/0.01,"x25",0.4*b**2/0.01*25)

print("===== P3 =====")
M,m3,R3,a3=2.0,1.0,0.30,0.15
Mt=M+m3; l=m3*a3/Mt
IO=M*R3**2/2+m3*a3**2; IG=IO-Mt*l**2
print("l",l,"IO",IO,"IG",IG)
th,thd=sp.symbols('theta thetadot')
# positions: O=(R th, R); mass at O+(-a sin, -a cos)
IB=sp.simplify(M*R3**2/2+M*R3**2 + m3*((-a3*sp.sin(th))**2+(R3-a3*sp.cos(th))**2))
print("I_B(theta)",sp.expand(sp.simplify(IB)))
IB2=IG+Mt*((l*sp.sin(th))**2+(R3-l*sp.cos(th))**2)
print("check via G", sp.simplify(sp.expand(IB-IB2)))
U=Mt*g*l*(1-sp.cos(th))
print("U",sp.expand(U))
w3=np.sqrt(Mt*g*l/float(IB.subs(th,0))); wax=np.sqrt(Mt*g*l/IO)
print("I_B(0)",float(IB.subs(th,0)),"ring",w3,"T",2*np.pi/w3,"axle ring",wax,"T",2*np.pi/wax,"ratio",w3 and (2*np.pi/w3)/(2*np.pi/wax))
c0=0.6; th0=np.arctan2(0.8,0.6); print("th0 deg",np.degrees(th0))
drop=Mt*g*l*(1-c0); IB0=float(IB.subs(th,0))
wb3=np.sqrt(2*drop/IB0); vG=wb3*(R3-l)
print("heft",drop,"sweep bottom",wb3,"vG",vG,"punch",0.5*Mt*vG**2,"hook",0.5*IG*wb3**2, "shares",Mt*(R3-l)**2/IB0, IG/IB0)
# independent Newton-Euler sim
tt_,x1,x2=sp.symbols('t x1 x2')
TH=sp.Function('TH')(tt_)
xG=R3*TH-l*sp.sin(TH); yG=R3-l*sp.cos(TH)
ff,nn,thdd=sp.symbols('f n thdd')
axG=sp.diff(xG,tt_,2); ayG=sp.diff(yG,tt_,2)
rep={sp.Derivative(TH,(tt_,2)):thdd, sp.Derivative(TH,tt_):x2}
axG=axG.subs(rep).subs(TH,x1); ayG=ayG.subs(rep).subs(TH,x1)
PmG=sp.Matrix([R3*x1,0])-sp.Matrix([R3*x1-l*sp.sin(x1),R3-l*sp.cos(x1)])
torque=PmG[0]*nn-PmG[1]*ff
eqs=[sp.Eq(Mt*axG,ff),sp.Eq(Mt*ayG,nn-Mt*g),sp.Eq(IG*(-thdd),torque)]
so=sp.solve(eqs,[thdd,ff,nn],dict=True)[0]
fth=sp.lambdify((x1,x2),so[thdd]); fn=sp.lambdify((x1,x2),so[nn]); fF=sp.lambdify((x1,x2),so[ff])
# Lagrange form
lag=sp.lambdify((x1,x2),(-sp.diff(U,th).subs(th,x1)-sp.Rational(1,2)*sp.diff(IB,th).subs(th,x1)*x2**2)/IB.subs(th,x1))
print("NE vs Lagrange at (0.7,1.3):",fth(0.7,1.3),lag(0.7,1.3))
sol=solve_ivp(lambda t,y:[y[1],fth(y[0],y[1])],[0,10],[th0,0],rtol=1e-12,atol=1e-14,dense_output=True)
ev=lambda t,y:y[0]; ev.terminal=True
s1=solve_ivp(lambda t,y:[y[1],fth(y[0],y[1])],[0,10],[th0,0],rtol=1e-12,atol=1e-14,events=ev)
yb=s1.y_events[0][0]; print("num bottom sweep",yb[1],"dev",abs(yb[1])-wb3,"time to bottom",s1.t_events[0][0])
# min normal force and friction need over the swing
T_=np.linspace(0,10,20001); Y=sol.sol(T_)
Nv=fn(Y[0],Y[1]); Fv=fF(Y[0],Y[1]); print("N range",Nv.min(),Nv.max(),"|f/N| max",np.max(np.abs(Fv/Nv)))
# energy drift
E=0.5*np.array([float(IB.subs(th,v)) for v in Y[0][::200]])*Y[1][::200]**2+1.5*(1-np.cos(Y[0][::200]))
print("energy drift",E.max()-E.min(), E.mean())
# small osc numeric period
sol=solve_ivp(lambda t,y:[y[1],fth(y[0],y[1])],[0,40],[0.01,0],rtol=1e-12,atol=1e-14,dense_output=True)
tt=np.linspace(0,40,400001); yy=sol.sol(tt)[0]
zc=[tt[i] for i in range(len(tt)-1) if yy[i]<0<=yy[i+1]]
Tn=np.mean(np.diff(zc)); print("num small period",Tn,"dev",Tn-2*np.pi/w3)
# (e) at outwardness 0.8 on the way down
thx=np.arctan2(0.6,0.8); IBx=float(IB.subs(th,thx)); zing=1.5*(0.8-0.6)/IBx; thdx=-np.sqrt(2*zing)
Pg=-1.5*np.sin(thx)*thdx; dIB=float(sp.diff(IB,th).subs(th,thx))*thdx
print("IBx",IBx,"zing",zing,"thd",thdx,"Pg",Pg,"Pg/IB",Pg/IBx,"dIB/dt",dIB,"actual dzing/dt",(Pg-zing*dIB)/IBx, "NE thd*thdd",thdx*fth(thx,thdx))
print("I_B range",float(IB.subs(th,0)),float(IB.subs(th,sp.pi)),float(IB.subs(th,th0)))

print("===== P4 =====")
Ia=4+2*np.sqrt(2); D=40.; Lc=0.10; C=Ia/(D*Lc); kap=5/6*np.sqrt(D*Lc)
w0=np.sqrt(D/Ia); nu=w0/6
print("Ia",Ia,"C",C,"kap",kap,"w0",w0,"1/sqrt(LC)",1/np.sqrt(Lc*C),"nu",nu)
E=0.080
q0=np.sqrt(2*C*E); V0=q0/C; a0=q0*np.sqrt(Lc/Ia)
print("q0",q0,"V0",V0,"a0",a0,np.sqrt(2*E/D),"deg",np.degrees(a0))
W=sp.symbols('W',positive=True); A_,Q_=sp.symbols('A Q')
Iss=4+2*sp.sqrt(2); Ds=40; Ls=sp.Rational(1,10); Cs=Iss/(Ds*Ls); ks=sp.Rational(5,6)*sp.sqrt(Ds*Ls); w0s=sp.sqrt(Ds/Iss)
Mx=sp.Matrix([[Ds-Iss*W**2,-ks*W],[ks*W,Ls*W**2-1/Cs]])
# eq1: A(D-Ia W^2) - k W Q = 0 ; eq2: -L W^2 Q = -Q/C + k W A -> kW A + (L W^2 - 1/C) Q... careful
# eq2: -L W^2 Q + Q/C - k W A = 0
Mx=sp.Matrix([[Ds-Iss*W**2,-ks*W],[-ks*W,1/Cs-Ls*W**2]])
roots=sp.solve(sp.simplify(Mx.det()),W)
print("roots",[sp.nsimplify(sp.simplify(r/w0s)) for r in roots])
for r in roots:
    QA=sp.simplify((Ds-Iss*r**2)/(ks*r)); print(" w/w0",sp.simplify(r/w0s),"Q/A",sp.nsimplify(sp.simplify(QA/sp.sqrt(Iss/Ls))),float(QA))
tau=sp.symbols('tau'); a0s,q0s,nus=sp.symbols('a0 q0 nu',positive=True)
av=a0s*(-sp.Rational(9,13)*sp.sin(4*nus*tau)+sp.Rational(4,13)*sp.sin(9*nus*tau))
qv=q0s*(sp.Rational(9,13)*sp.cos(4*nus*tau)+sp.Rational(4,13)*sp.cos(9*nus*tau))
sub={a0s:q0s*sp.sqrt(Ls/Iss),nus:w0s/6}
r1=sp.simplify((Iss*sp.diff(av,tau,2)-ks*sp.diff(qv,tau)+Ds*av).subs(sub))
r2=sp.simplify((Ls*sp.diff(qv,tau,2)+qv/Cs+ks*sp.diff(av,tau)).subs(sub))
print("residuals",r1,r2)
print("init",[sp.simplify(e.subs(tau,0)) for e in [av,sp.diff(av,tau),qv,sp.diff(qv,tau)]])
Th=sp.pi/nus/1  # T/2 = pi/nu
vals=[sp.simplify(e.subs(tau,sp.pi/nus)) for e in [av,sp.diff(av,tau),qv,sp.diff(qv,tau)]]
print("at T/2",vals)
Tr=2*np.pi/nu; print("T",Tr,"T/2",Tr/2,"T0",2*np.pi/w0)
def rhs4(t,y):
    a,ad,q,i=y
    return [ad,(kap*i-D*a)/Ia,i,(-q/C-kap*ad)/Lc]
sol=solve_ivp(rhs4,[0,Tr],[0,0,q0,0],rtol=1e-12,atol=1e-15,dense_output=True)
tt=np.linspace(0,Tr,20001); Y=sol.sol(tt)
fa=sp.lambdify(tau,av.subs({a0s:a0,nus:nu})); fad=sp.lambdify(tau,sp.diff(av,tau).subs({a0s:a0,nus:nu}))
fq=sp.lambdify(tau,qv.subs({q0s:q0,nus:nu})); fi=sp.lambdify(tau,sp.diff(qv,tau).subs({q0s:q0,nus:nu}))
print("max dev a",np.max(np.abs(Y[0]-fa(tt))),"ad",np.max(np.abs(Y[1]-fad(tt))),"q",np.max(np.abs(Y[2]-fq(tt))),"i",np.max(np.abs(Y[3]-fi(tt))))
print("state at T",sol.sol(Tr),"start",[0,0,q0,0])
print("state at T/2",sol.sol(Tr/2),"closed",fa(Tr/2),fad(Tr/2),fq(Tr/2),fi(Tr/2))
print("max|a|",np.max(np.abs(Y[0])),"deg",np.degrees(np.max(np.abs(Y[0]))),"max|ad|",np.max(np.abs(Y[1])),"max|i|",np.max(np.abs(Y[3])))
Ek=lambda y:(0.5*Ia*y[1]**2,0.5*D*y[0]**2,y[2]**2/(2*C),0.5*Lc*y[3]**2)
e=Ek(sol.sol(Tr/2)); print("energies T/2",e,sum(e),144/169*E,25/169*E)
EE=sum(Ek(Y)); print("energy drift",EE.max()-EE.min())
# does any earlier time return all four? scan
d=np.sqrt((Y[0]/a0)**2+(Y[1]/(a0*w0))**2+((Y[2]-q0)/q0)**2+(Y[3]/(q0*w0))**2)
idx=[i for i in range(1,len(tt)-1) if d[i]<d[i-1] and d[i]<d[i+1]]
print("closest returns (t,dist)",sorted([(round(tt[i],3),round(d[i],4)) for i in idx],key=lambda z:z[1])[:5])
c=3.0e8; Ep,Em=0.080,0.020
w=(Ep-Em)/(Ep+Em)*c; gw=1/np.sqrt(1-(w/c)**2)
print("w",w,"gamma",gw,"rest inc",(Ep+Em)/gw,"KE inc",(gw-1)*(Ep+Em)/gw,"dp",(Ep-Em)/c)
v=sp.symbols('v'); vs=sp.solve(sp.Eq((1-v)*80,(1+v)*20),v)[0]; print("v/c",vs)
gH=1/np.sqrt(1-0.36); print("E' each",gH*0.4*80,gH*1.6*20)
print("S time",gH*Tr,"dist",w*gH*Tr)
