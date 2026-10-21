#!/usr/bin/env python3
# Written by Claude (Anthropic), 2026-10-20. Numbers for rooms 5-8 (billiards, conservatory, ballroom) of the assembled draft, in SI.
import math
g=10.0
# room 5: skid
m=1.0;R=0.05;h=0.04;v0=2.1;I=0.4*m*R*R
w0=m*v0*h/I; Lt=m*v0*(R+h); wr=Lt/(1.4*m*R*R); vr=R*wr
E0=0.5*m*v0**2+0.5*I*w0**2; E1=0.5*m*vr**2+0.5*I*wr**2
print('I',I,'w0',w0,'swirl',Lt,'profile',1.4*R*R,'w',wr,'v',vr,'E0',E0,'E1',E1,'burn',E0-E1)
a=0.2*g; t=(vr-v0)/a; print('t',t,'dist',(v0+vr)/2*t)
# slip distance check: bottom point speed v-wR from -2.1 to 0
print('burn via friction',m*0.2*g*(abs(v0-R*w0)/2*t))
M=5/7;u=4.2;print('striker oompf',M*u,'E',0.5*M*u*u)
# elastic: M u = M u' + m v0 ; compute u'
u2=(M*u-m*v0)/M; print('striker after',u2,M*u2,0.5*M*u2**2, 'contact',v0+h*w0,'sep',v0+h*w0-u2)
# rod
mr,L,J=0.6,1.2,1.8;vc=J/mr;wc=J*(L/2)/(mr*L*L/12);print('rod',vc,wc,vc/wc)
# cube
s=0.3;print('cube thr',math.sqrt(g*s*(1/math.sqrt(2)-0.5)/(3/16)),'rise',s*(1/math.sqrt(2)-0.5))
# superball
v,Rw=2.1,0.0
for i in range(2):
    v,Rw=(3*v+4*Rw)/7,(10*v-3*Rw)/7
    print('bounce',i+1,v,Rw,Rw/0.025)
# room 6
print('D',2.7*2*math.pi/math.sqrt(10),'T',2*math.pi/math.sqrt(10),'bead T',2*math.pi/math.sqrt(g/(5/7)))
a=5/7;b=0.05;th=0.1;w=th*math.sqrt(10);print('lever sweep',w,'centre',a*w,'own',a/b*w,'heft',g*a*(1-math.cos(th)))
for name,(bs,Iy) in {'beam1':(0.5,0.75),'beam2':(1.5,0.75),'beam3':(0,1.0)}.items():
    print(name,'beta',bs,'I',Iy,'T',(2*math.pi/math.sqrt(g*bs/Iy)) if bs else None)
Iax=0.09+0.0225;Mt=3.0;d=0.05;Rr=0.3
Ic=lambda ph: Iax+Mt*Rr**2-2*Mt*d*Rr*math.cos(ph); print('Ic0',Ic(0),'coef',Iax+Mt*Rr**2,2*Mt*d*Rr)
heft=Mt*g*0.02;wb=math.sqrt(2*heft/Ic(0));vcm=0.25*wb;print('heft',heft,'w',wb,'vcm',vcm,'punch',0.5*Mt*vcm**2,'hook',heft-0.5*Mt*vcm**2,'ratio',0.5*Mt*vcm**2/(heft-0.5*Mt*vcm**2),25/14)
print('T roll',2*math.pi/math.sqrt(Mt*g*d/Ic(0)),'T axle',2*math.pi/math.sqrt(Mt*g*d/Iax))
print('kitchen zlow',3.0/0.5,(0.5*8**2-0.5*4**2)/4)
# room 7/8
V=2.0;Rh=0.25;print('hoop w',V/Rh,'top',2*V,'bottom',0)
print('track wb',0.5*2.0/0.05)
mp=0.5;r0=0.6;sw=mp*r0*V;print('roll',sw,'swirl',r0*V,'v1',r0*V/0.3,'sweep1',r0*V/0.3/0.3,'T0',mp*V**2/r0,'T1',mp*(r0*V/0.3)**2/0.3,'work',0.5*mp*((r0*V/0.3)**2-V**2),'zip',V**2/2,(r0*V/0.3)**2/2,'transmission',8*5/12,10/3*0.6)
