import sympy as sp, numpy as np
from scipy.integrate import solve_ivp
# ---------- Problem 1 ----------
m,R,v0,mu,g,h=sp.symbols('m R v0 mu g h',positive=True)
I=sp.Rational(2,5)*m*R**2
J=m*v0
w0=J*h/I
# angular momentum about ground point
Lg=J*(R+h)
vf=sp.solve(sp.Eq(m*R*sp.Symbol('vf')+I*sp.Symbol('vf')/R,Lg),sp.Symbol('vf'))[0]
print('vf',sp.simplify(vf))
hs=sp.solve(sp.Eq(vf,sp.Rational(9,7)*v0),h)[0]; print('h/R',hs/R)
num={m:1,R:sp.Rational(5,100),v0:sp.Rational(21,10),mu:sp.Rational(2,10),g:10}
W0=w0.subs(h,hs).subs(num); print('omega0',W0, 'v0/R*2',(2*v0/R).subs(num))
VF=(sp.Rational(9,7)*v0).subs(num); print('vf',VF,'omegaf',VF/num[R])
a=mu*g; al=-mu*m*g*R/I
ts=(VF-num[v0])/a.subs(num); print('t',ts, 'omega check',(W0+al.subs(num)*ts))
d=num[v0]*ts+a.subs(num)*ts**2/2; print('dist',d)
K0=(m*v0**2/2+I*w0**2/2).subs(h,hs).subs(num); Kf=(sp.Rational(7,10)*m*vf**2).subs(h,hs).subs(num)
print('K0',K0,float(K0),'Kf',Kf,float(Kf),'lost',K0-Kf,'frac',sp.nsimplify((K0-Kf)/K0),float((K0-Kf)/K0))
print('roll at once h',sp.solve(sp.Eq(w0*R,v0),h))
# numeric skid
def f(t,y):
    x,v,th,om=y
    slip=v-om*float(num[R])
    F=-np.sign(slip)*0.2*1*10
    return [v,F/1,om,-F*0.05/(0.4*1*0.05**2)]
ev=lambda t,y: y[1]-y[3]*0.05
ev.terminal=True
s=solve_ivp(f,[0,1],[0,2.1,0,84.0],events=ev,rtol=1e-12,atol=1e-12,max_step=1e-3)
te=s.t_events[0][0]; ye=s.y_events[0][0]
print('num t',te,'x',ye[0],'v',ye[1],'omega',ye[3])
print('dev t',te-0.3,'dx',ye[0]-0.72,'dv',ye[1]-2.7,'domega',ye[3]-54)
K=lambda y:0.5*y[1]**2+0.5*0.4*0.05**2*y[3]**2
print('num energy',K([0,2.1,0,84]),K(ye),'dev',K(ye)-5.103)
# ---------- Problem 2 ----------
Rc,b,psi,t=sp.symbols('R_c b psi t',positive=True)
ps=sp.Function('psi')(t); phi=sp.Function('phi')(t)
# centre position (x right,y up), axis at origin
rc=sp.Matrix([(Rc-b)*sp.sin(ps),-(Rc-b)*sp.cos(ps),0])
vc=rc.diff(t)
Om=sp.Matrix([0,0,phi.diff(t)])  # ball angular velocity, ccw positive
rcp=sp.Matrix([b*sp.sin(ps),-b*sp.cos(ps),0])  # centre->contact
vp=vc+Om.cross(rcp)
sol=sp.solve(sp.simplify(vp[0]*sp.cos(ps)+vp[1]*sp.sin(ps)),phi.diff(t))
print('spin',sp.simplify(sol[0]))
print('vp after', sp.simplify(vp.subs(phi.diff(t),sol[0])))
mm=sp.Symbol('m',positive=True); gg=sp.Symbol('g',positive=True)
KE=sp.simplify(mm*vc.dot(vc)/2+sp.Rational(2,5)*mm*b**2*sol[0]**2/2)
print('KE',sp.factor(KE))
Rv,bv=0.30,0.05
Om2=np.sqrt(5*10/(7*(Rv-bv))); print('Omega',Om2,'T',2*np.pi/Om2,'Tbead',2*np.pi*np.sqrt((Rv-bv)/10),'ratio',np.sqrt(1.4))
# numeric nonlinear small oscillation
def f2(t,y): return [y[1],-5*10/(7*(Rv-bv))*np.sin(y[0])]
ev2=lambda t,y:y[1]; ev2.direction=1
s=solve_ivp(f2,[0,5],[0.01,0],events=ev2,rtol=1e-12,atol=1e-14)
print('num period (amp .01 rad)',s.t_events[0][0], 'dev',s.t_events[0][0]-2*np.pi/Om2)
