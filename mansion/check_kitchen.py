#!/usr/bin/env python3
# Written by Claude (Anthropic), 2026-10-20. Independent check of Codex's kitchen spool and library ladder.
# Spool: exact rationals. Ladder: exact departure values plus a numerical ODE of the sliding ladder.
from fractions import Fraction as Fr
import math
from scipy.integrate import solve_ivp
import numpy as np

# ---------- kitchen: first spool, F = 6 push, m = 2, R = 0.20, r = 0.12, eta_axle = 0.040, g = 10
m, R, r, ea, F, g = Fr(2), Fr(1,5), Fr(3,25), Fr(1,25), Fr(6), Fr(10)
ec = ea + m*R*R
print('eta_contact', ec, float(ec), ' eta_contact/R^2', ec/R**2)
def spool(cos, sin):
    lever = R*cos - r                    # clockwise positive, about the contact line
    a = F*lever/ec*R                     # rolling: a = R alpha
    f = m*a - F*cos                      # horizontal balance, rightward positive
    N = m*g - F*sin
    return a, f, N
import math as M
for name, th in (('flat',0),('sixty',60),('up',90)):
    c, s = (Fr(1),Fr(0)) if th==0 else ((Fr(1,2), None) if th==60 else (Fr(0),Fr(1)))
    if th==60: c=Fr(1,2); s=M.sqrt(3)/2
    a,f,N = spool(c, s)
    print(name,'a',float(a),'f',float(f),'N',float(N),'grip',float(-f/N) if f<0 else float(f/N))
print('still at cos =', float(r/R), ' sin =', M.sqrt(1-(0.6)**2))
# worst grip over all angles
ths = np.linspace(0, M.pi/2, 20001)
need = (2*np.cos(ths)+2.4)/(20-6*np.sin(ths))
print('max grip needed over 0..90 deg', need.max(), 'at deg', np.degrees(ths[need.argmax()]))
print('2cos+1.5sin max', max(2*np.cos(ths)+1.5*np.sin(ths)))
# energy before the trip: slack 0.10 m at 0.20 zoom
a = 0.20; d = 0.10
t = M.sqrt(2*d/a); v = a*t
punch = 0.5*2*v*v; hook = 0.5*0.04*(v/0.2)**2
print('t',t,'v',v,'punch',punch,'hook',hook,'total',punch+hook,'cord end 1 cm x 6 push =',6*0.01)
# cord end drawn: net along cord at 60 deg from rolling 0.5 rad leftward (clockwise negative)
phi = -d/0.2; th = M.radians(60)
print('cord drawn', phi*(0.2*M.cos(th)-0.12))
print('sear 0.02 push on 3 lump:', 0.02/3, 'fraction', 0.02/3/0.2)

# ---------- second winding: top-wound, r = R/3, board
rr = R/3
def f_needed(Fv, sinp):               # 9 f + F = 3 m g sin
    return (3*m*g*sinp - Fv)/9
sinp, cosp, mu = Fr(3,5), Fr(4,5), Fr(1,5)
Flow = 3*m*g*sinp - 9*mu*m*g*cosp; Fhigh = 3*m*g*sinp + 9*mu*m*g*cosp
print('limits', float(Flow), float(Fhigh))
# verify 9f+F relation from the two balances for random F
import random
for _ in range(3):
    Fv = Fr(random.randint(1,100)); 
    a_ = (Fv*(R+rr)/R - m*g*sinp)/(ec/R**2)       # eta_c a/R^2 + mg sin = F (R+r)/R
    f_ = m*a_ - Fv + m*g*sinp
    assert 9*f_ + Fv == 3*m*g*sinp, (f_, Fv)
print('second winding relation ok')

# ---------- library ladder
M_, L, x0, y0 = 8, 3.0, 1.8, 2.4
print('statics: floor', M_*10, 'crank about foot', M_*10*0.9, 'wall', M_*10*0.9/y0)
# moving trial
dx = 0.4; dy = -x0*dx/y0
print('top speed', dy, 'centre', dx/2, dy/2, M.hypot(dx/2,dy/2), 'sweep', dx/y0, -dy/x0)
# sliding ladder, wall contact: theta from floor, state (theta, w), top on wall, foot on floor, no friction
g_ = 10.0
th0 = M.asin(y0/L)
def rhs(t, s):
    th, w = s                      # w = -theta_dot (counterclockwise sweep)
    al = 1.5*g_*M.cos(th)/L        # 2 L alpha = 3 g cos
    return [-w, al]
def wall_force(th, w):
    al = 1.5*g_*M.cos(th)/L
    agx = 0.5*L*(al*M.sin(th) - w*w*M.cos(th))
    return M_*agx
def ev(t, s): return wall_force(*s)
ev.terminal = True; ev.direction = -1
sol = solve_ivp(rhs, [0, 3], [th0, 1e-12], events=ev, rtol=1e-11, atol=1e-13, max_step=1e-3)
th, w = sol.y[0,-1], sol.y[1,-1]
print('start wall force', wall_force(th0, 0.0), 'closed form', 0.75*M_*g_*M.cos(th0)*M.sin(th0))
print('departure: top height', L*M.sin(th), 'w^2', w*w, '8/3 =', 8/3, 'w', w)
print('centre speed', L*w/2, 'root 6', M.sqrt(6), 'punch', 0.5*M_*(L*w/2)**2, 'hook', 0.5*(M_*L*L/12)*w*w)
print('foot', L*M.cos(th), 'travelled', L*M.cos(th)-x0, 'heft lost', M_*g_*(y0-L*M.sin(th))/2)
