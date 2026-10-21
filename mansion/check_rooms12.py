#!/usr/bin/env python3
# Written by Claude (Anthropic), 2026-10-20. Numbers for rooms 1 and 2 of the assembled Mansion draft.
import math
g=10.0
# room 1: knife, m = 1.0 kg, L = 1.0 m, released from rest at 0.10 rad
m,L,th=1.0,1.0,0.10
h=L*(1-math.cos(th)); print('h',h,'~ L th^2/2',L*th*th/2)
K=m*g*h; v=math.sqrt(2*g*h); w=v/L
print('K',K,'v',v,'sweep at bottom',w,'check',math.sqrt(g/L)*th)
T=2*math.pi*math.sqrt(L/g); print('T',T,'ring',math.sqrt(g/L))
print('beta',m*L,'I',m*L*L,'g beta / I',g*m*L/(m*L*L),'twice mass:',g*2*m*L/(2*m*L*L),'K2',2*K)
# exact period for 0.10 rad (amplitude correction)
print('exact T ~',T*(1+th*th/16))
# room 2: engine test
I,w1,P,t=0.50,4.0,3.0,4.0
K1=0.5*I*w1**2; K2=K1+P*t; w2=math.sqrt(2*K2/I)
print('K1',K1,'K2',K2,'w2',w2)
theta=I*(w2**3-w1**3)/(3*P); print('angle',theta,'turns',theta/(2*math.pi))
print('torque start',P/w1,'end',P/w2,'pickup',P/w1/I,P/w2/I)
# check: integrate numerically
dt=1e-5; ww=w1; ang=0.0; tt=0.0
while tt<t:
    al=P/(I*ww); ww+=al*dt; ang+=ww*dt; tt+=dt
print('numeric w',ww,'angle',ang)
# governor: l = 0.5 m, w = 5
l,wg=0.5,5.0
c=g/(wg**2*l); print('cos',c,'lean deg',math.degrees(math.acos(c)),'below pivot',l*c,'out',l*math.sqrt(1-c*c))
print('lift above hanging',l*(1-c),'heft change per 1 kg weight',1*g*l*(1-c),'critical sweep',math.sqrt(g/l))
# hook at sweep 5: each weight KE = 1/2 m (out*w)^2
out=l*math.sqrt(1-c*c); print('KE each',0.5*1*(out*wg)**2)
