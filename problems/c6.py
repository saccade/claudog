import numpy as np
from scipy.integrate import solve_ivp
m=0.5; r0=0.6; Tpull=60.0  # string drawn in at constant rate over 60 s
rate=0.3/Tpull
# body in plane, string length to hole r(t)=r0-rate*t enforced by constraint: use polar with r prescribed
# theta eq: d/dt(m r^2 thdot)=0 ; tension from radial eq: T = m(r thdot^2 - rddot)
def f(t,z):
    th,w=z; r=r0-rate*t; rd=-rate
    return [w,-2*rd*w/r]
s=solve_ivp(f,[0,Tpull],[0,2.0/0.6],rtol=1e-11,atol=1e-12,dense_output=True)
w=s.y[1,-1]; print('vf',0.3*w,'omega',w)
ts=np.linspace(0,Tpull,200001); ws=s.sol(ts)[1]; rs=r0-rate*ts
T=m*rs*ws**2
print('work',np.trapezoid(T*rate,ts))
