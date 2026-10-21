import sympy as sp
a,q,A,Q,w,t=sp.symbols('a q A Q w t',positive=True)
Ia,D,L,C,k=sp.symbols('I_a D L C kappa',positive=True)
# numbers
r2=sp.sqrt(2)
Iav=2*(2+r2); Dv=40; Lv=sp.Rational(1,10)
Cv=Iav/(Dv*Lv); kv=sp.Rational(5,6)*sp.sqrt(Dv*Lv)
print('I_a',sp.N(Iav),'C',sp.N(Cv),'kappa',sp.N(kv))
w0sq=sp.simplify(Dv/Iav); print('w0^2',sp.N(w0sq),'w0',sp.N(sp.sqrt(w0sq)))
# characteristic
x=sp.symbols('x')
eq=sp.expand((Iav*(w0sq-x**2))*(Lv*(w0sq-x**2))-kv**2*x**2)
sol=sp.solve(eq,x); print([sp.N(s) for s in sol])
wl,wh=sp.N(sp.sqrt(w0sq)*sp.Rational(2,3)),sp.N(sp.sqrt(w0sq)*sp.Rational(3,2))
print('w low/high',wl,wh,'product',wl*wh,'periods',2*sp.pi/wl,2*sp.pi/wh, 'T0',2*sp.pi/sp.sqrt(w0sq))
for xx in [sp.Rational(2,3),sp.Rational(3,2)]:
    ww=sp.sqrt(w0sq)*xx
    QA=Iav*(w0sq-ww**2)/(kv*ww)
    QA2=kv*ww/(Lv*(w0sq-ww**2))
    print('Q/A',sp.N(QA),sp.N(QA2),'sqrt(Ia/L)',sp.N(sp.sqrt(Iav/Lv)))
    # energy split at a=A (cos=1): motion spring 1/2 D A^2 ; coil 1/2 L w^2 Q^2
    print(' spring',sp.N(Dv/2),'coil',sp.N(Lv*ww**2*QA**2/2),'kinetic at bottom',sp.N(Iav*ww**2/2),'cap at i=0',sp.N(QA**2/(2*Cv)))
# numeric integration check
import numpy as np
from scipy.integrate import solve_ivp
Iaf,Df,Lf,Cf,kf=map(float,(Iav,Dv,Lv,Cv,kv))
def f(t,y):
    a,ad,q,qd=y
    return [ad,(-Df*a+kf*qd)/Iaf,qd,(-kf*ad-q/Cf)/Lf]
for xx,sg in [(2/3,1),(3/2,-1)]:
    ww=float(sp.sqrt(w0sq))*xx; QA=sg*np.sqrt(Iaf/Lf)
    y0=[1,0,0,QA*ww]
    s=solve_ivp(f,[0,6],y0,rtol=1e-10,atol=1e-12,dense_output=True)
    tt=np.linspace(0,6,7); 
    err=max(abs(s.sol(t)[0]-np.cos(ww*t))+abs(s.sol(t)[2]-QA*np.sin(ww*t)) for t in tt)
    print('mode err',err)
# arbitrary start: a=A0, rest, q=0, no current -> mix
y0=[1,0,0,0]
s=solve_ivp(f,[0,20],y0,rtol=1e-10,atol=1e-12,dense_output=True)
# decomposition a(t)=c1 cos(wl t)+c2 cos(wh t); at t=0: q'(0)=0 => c1*Q1*wl+c2*Q2*wh=0, c1+c2=1
wlf,whf=float(wl),float(wh); Q1=np.sqrt(Iaf/Lf); Q2=-Q1
c1=sp.symbols('c1'); sol=sp.solve([c1+sp.Symbol('c2')-1, c1*Q1*wlf+sp.Symbol('c2')*Q2*whf],[c1,sp.Symbol('c2')]); print(sol)
