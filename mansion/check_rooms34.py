#!/usr/bin/env python3
# Written by Claude (Anthropic), 2026-10-20. Numbers for rooms 3 (spool) and 4 (ladder) of the assembled draft, in SI.
import math
from fractions import Fraction as Fr
g=10; m=2; R=Fr(1,5); r=Fr(3,25); Iax=Fr(1,25); F=6
Ic=Iax+m*R*R; print('I_contact',Ic,'effective mass',Ic/R**2)
for name,c,s in (('flat',1,0),('60',0.5,math.sqrt(3)/2),('up',0,1)):
    a=F*(c-0.6)/float(Ic/R**2); f=m*a-F*c; N=m*g-F*s
    print(name,'a',round(a,3),'f',round(f,3),'N',round(N,3),'grip',round(abs(f)/N,3))
print('still cos',0.6,'angle',math.degrees(math.acos(0.6)),'up part',F*0.8)
print('worst grip',max(abs(2*math.cos(t)*1+2.4)/(20-6*math.sin(t)) for t in [i*math.pi/2/1000 for i in range(1001)]))
print('max 2cos+1.5sin',math.hypot(2,1.5))
# twine
a=-0.2; t=math.sqrt(2*0.10/0.2); v=0.2*t; print('t',t,'v',v,'punch',0.5*m*v**2,'turn',0.5*float(Iax)*(v/float(R))**2,'cord work',6*0.01,'sear dA',0.02/3)
# slope
rr=float(R)/3; sp=0.6; cp=0.8; mu=0.2; N=m*g*cp
Flo=3*m*g*sp-9*mu*N; Fhi=3*m*g*sp+9*mu*N; print('slope limits',Flo,Fhi)
# ladder
L=3;M=8;x=1.8;y=2.4
print('floor',M*g,'torque',M*g*x/2,'wall',M*g*x/2/y)
print('calib: top',-x*0.4/y,'centre',0.2,-0.15,'speed',math.hypot(0.2,0.15),'omega',0.4/y)
s0=y/L; c0=x/L; print('wall at release',3*M*g*c0*(3*s0-2*s0)/4)
yd=2/3*y; w2=3*g*(s0-yd/L)/L; v=L*math.sqrt(w2)/2
print('y leave',yd,'w2',w2,'centre',v,'punch',M*L*L*w2/8,'hook',M*L*L*w2/24,'heft lost',M*g*(y-yd)/2,'foot',math.sqrt(L*L-yd**2),'out',math.sqrt(L*L-yd**2)-x)
