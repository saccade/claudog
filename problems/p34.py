import sympy as sp, numpy as np
from scipy.integrate import solve_ivp
# Problem 2 period fix
Rv,bv=0.30,0.05
Om2=np.sqrt(5*10/(7*(Rv-bv)))
def f2(t,y): return [y[1],-5*10/(7*(Rv-bv))*np.sin(y[0])]
ev2=lambda t,y:y[1]; ev2.direction=1
s=solve_ivp(f2,[0,5],[0.01,0],events=ev2,rtol=1e-12,atol=1e-14)
print('P2 num period',2*s.t_events[0][0],'dev',2*s.t_events[0][0]-2*np.pi/Om2)
# ---------- Problem 3 ----------
t=sp.symbols('t'); th=sp.Function('theta')(t)
M,m,R,a,g=sp.symbols('M m R a g',positive=True)
xO=R*th; yO=R
rm=sp.Matrix([xO-a*sp.sin(th),yO-a*sp.cos(th)])
vO=sp.Matrix([xO.diff(t),0])
T=M*vO.dot(vO)/2+M*R**2/4*th.diff(t)**2+m*rm.diff(t).dot(rm.diff(t))/2
U=m*g*rm[1]+M*g*yO
T=sp.simplify(T); print('T',sp.factor(sp.simplify(T/th.diff(t)**2*2)))
Lag=T-U
eom=sp.simplify(sp.diff(Lag.diff(th.diff(t)),t)-Lag.diff(th))
print('EOM',sp.expand(eom))
num={M:2,m:1,R:sp.Rational(3,10),a:sp.Rational(15,100),g:10}
IP=sp.expand(2*T/th.diff(t)**2).subs(num); print('IP',IP)
IO=(M*R**2/2+m*a**2).subs(num); IG=IO-3*sp.Rational(5,100)**2; print('IO',IO,'IG',IG)
IP0=IP.subs(th,0); print('IP0',IP0)
W=float(sp.sqrt(m*g*a/IP0).subs(num)); WO=float(sp.sqrt((m*g*a).subs(num)/IO))
print('Omega roll',W,'T',2*np.pi/W,'axle',WO,2*np.pi/WO,'ratio',WO/W, np.sqrt(float(IP0/IO)))
c0=sp.Rational(3,5)
Ubot=(m*g*a*(1-c0)).subs(num); print('U0',Ubot)
wb=sp.sqrt(2*Ubot/IP0); print('omega bottom',wb,float(wb))
vG=sp.Rational(25,100)*wb; print('vG',float(vG))
KG=sp.Rational(3,2)*vG**2; Krot=IG*wb**2/2; print('KG',float(KG),'Krot',float(Krot),float(KG/Ubot),float(Krot/Ubot))
# numeric
eomn=sp.lambdify((th,th.diff(t)),sp.solve(eom.subs(num),th.diff(t,2))[0].subs({}) ,'numpy')
thd2=sp.solve(eom.subs(num),th.diff(t,2))[0]
s1,s2=sp.symbols('s1 s2')
fac=sp.lambdify((s1,s2),thd2.subs(th.diff(t),s2).subs(th,s1),'numpy')
print('thdd expr',sp.simplify(thd2.subs(th.diff(t),s2).subs(th,s1)))
def f3(t,y): return [y[1],fac(y[0],y[1])]
th0=float(sp.atan2(4,3))
ev=lambda t,y:y[0]; ev.terminal=True
s=solve_ivp(f3,[0,5],[th0,0],events=ev,rtol=1e-12,atol=1e-13,dense_output=True)
yb=s.y_events[0][0]; print('num bottom t',s.t_events[0][0],'thetadot',yb[1],'dev',yb[1]+float(wb))
# CM velocity numeric at bottom
d=0.05
vGx=0.3*yb[1]-d*np.cos(yb[0])*yb[1]; vGy=d*np.sin(yb[0])*yb[1]
print('vG num',np.hypot(vGx,vGy),'dev',np.hypot(vGx,vGy)-float(vG))
# energy along run, and normal force, friction ratio
tt=np.linspace(0,s.t[-1],2000); Y=s.sol(tt)
IPn=lambda x:0.3825-0.09*np.cos(x)
E=0.5*IPn(Y[0])*Y[1]**2+1.5*(1-np.cos(Y[0])); print('energy drift',E.max()-E.min())
thdd=np.array([fac(*y) for y in Y.T])
xG_dd=0.3*thdd - d*(np.cos(Y[0])*thdd-np.sin(Y[0])*Y[1]**2)
yG_dd=d*(np.sin(Y[0])*thdd+np.cos(Y[0])*Y[1]**2)
N=3*(10+yG_dd); F=3*xG_dd
print('N min',N.min(),'|F/N| max',np.abs(F/N).max())
# full period at 53 deg and small amplitude
ev2=lambda t,y:y[1]; ev2.direction=1
s=solve_ivp(f3,[0,10],[0.01,0],events=ev2,rtol=1e-12,atol=1e-14)
print('small amp period num',2*s.t_events[0][0],'dev',2*s.t_events[0][0]-2*np.pi/W)
s=solve_ivp(f3,[0,10],[th0,0],events=ev2,rtol=1e-12,atol=1e-14)
print('53deg period num',2*s.t_events[0][0])
# (e) check d/dt(K)=Pg while d/dt(.5 thd^2) != Pg/IP
y=np.array([th0*0.5,1.3]); dd=fac(*y)
Pg=-1.5*np.sin(y[0])*y[1]
print('dK/dt',IPn(y[0])*y[1]*dd+0.5*0.09*np.sin(y[0])*y[1]**3,'Pg',Pg,'thd*thdd',y[1]*dd,'Pg/IP',Pg/IPn(y[0]))
