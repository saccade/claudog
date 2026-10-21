import math
from scipy.integrate import solve_ivp
import numpy as np
# Problem 2 period at amplitude 0.01
w2=10/(1.4*0.25); T0=2*math.pi/math.sqrt(w2)
def f(t,y): return [y[1], -w2*math.sin(y[0])]
def period(fun,y0,guess):
    ev=lambda t,y: y[1]; ev.direction=1
    s=solve_ivp(fun,[0,2*guess],y0,events=ev,rtol=1e-12,atol=1e-14)
    return s.t_events[0][0]
print("p2 T0",T0,"T(0.01)",period(f,[0.01,0],T0))
# Problem 3
M,m,R,a,g=2.0,1.0,0.3,0.15,10
def IP(th): return 0.3825-0.09*math.cos(th)
def f3(t,y):
    th,w=y
    return [w, -(m*a*R*math.sin(th)*w*w + m*g*a*math.sin(th))/IP(th)]
th0=math.atan2(0.12,0.09)
ev=lambda t,y:y[0]; ev.terminal=True
s=solve_ivp(f3,[0,5],[th0,0],events=ev,rtol=1e-12,atol=1e-14)
print("p3 reach bottom",s.t_events[0][0], s.y_events[0][0])
ev2=lambda t,y:y[1]; ev2.direction=1
s=solve_ivp(f3,[0,10],[th0,0],events=ev2,rtol=1e-12,atol=1e-14)
print("p3 full period",s.t_events[0][:2])
# 3e X point cos=0.8
c,sn=0.8,0.6
U=1.5*(c-0.6); I=IP(math.acos(c)); z=U/I; wd=-math.sqrt(2*z)
Pg=1.5*sn*abs(wd); dI=0.09*sn*wd
print("X pt",I,z,wd,Pg,Pg/I,dI,(Pg-z*dI)/I)
th=math.radians(26.565); c,sn=math.cos(th),math.sin(th)
U=1.5*(c-0.6); I=IP(th); z=U/I; wd=-math.sqrt(2*z)
Pg=1.5*sn*abs(wd); dI=0.09*sn*wd
print("Y pt",I,wd,Pg,Pg/I,z*dI,(Pg-z*dI)/I)
# p4
Ia=4+2*math.sqrt(2); D=40; L=0.1; C=Ia/(D*L); w0=math.sqrt(D/Ia); nu=w0/6
q0=math.sqrt(2*C*0.08); rho=math.sqrt(Ia/L)
print("p4",C,w0,nu,2*math.pi/nu,q0,q0/C,rho,q0/rho, math.degrees(q0/rho))
a0=q0/rho
print("adot T/2",-72/13*a0*nu, 5/13*q0, 144/169*80, 25/169*80)
print("gamma T",1.25*2*math.pi/nu, 1.8e8*1.25*2*math.pi/nu, 3e8*1.25*2*math.pi/nu, 3e8*2*math.pi/nu)
