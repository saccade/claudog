import numpy as np, sympy as sp
from scipy.integrate import solve_ivp
g=10.
def period(f,A,tmax):
    ev=lambda t,y:y[0]; ev.direction=1
    s=solve_ivp(lambda t,y:[y[1],f(y[0],y[1])],[0,tmax],[A,0],rtol=1e-13,atol=1e-16,events=ev)
    z=s.t_events[0]; return np.mean(np.diff(z)), len(z)
L=0.25
for A in [0.01,0.001]:
    Tb,n=period(lambda p,pd:-200/7*np.sin(p),A,30); Tbd,_=period(lambda p,pd:-g/L*np.sin(p),A,30)
    print("P2 A",A,"ball",Tb,Tb-2*np.pi/np.sqrt(200/7),"bead",Tbd,Tbd-2*np.pi/np.sqrt(40), "expected rel A^2/16",A**2/16)
# P3 via Lagrange (checked equal to Newton-Euler)
IB=lambda t:0.3825-0.09*np.cos(t); dIB=lambda t:0.09*np.sin(t)
f=lambda t,td:(-1.5*np.sin(t)-0.5*dIB(t)*td**2)/IB(t)
for A in [0.01,0.001]:
    T,n=period(f,A,60); print("P3 A",A,T,T-2*np.pi/np.sqrt(1.5/0.2925))
