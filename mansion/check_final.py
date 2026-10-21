#!/usr/bin/env python3
# Written by Claude (Anthropic), 2026-10-21. Re-checks the cube threshold, the ribbon endpoints and the spool/ladder anchors used in the reading draft.
from math import sqrt
g=10
s=0.30; lift=sqrt(2)*s/2-s/2
v=sqrt(2*g*lift*8/3)
print('cube: lift %.4f threshold %.3f m/s, kept fraction %.4f'%(lift,v,(2/3)*(3/4)**2*(1)) )
m=0.5;r1=0.6;v1=2.0;r2=0.3
v2=v1*r1/r2
print('ribbon: v2 %.2f w2 %.2f T1 %.2f T2 %.2f W %.2f'%(v2,v2/r2,m*v1**2/r1,m*v2**2/r2,0.5*m*(v2**2-v1**2)))
print('spool: grips',[round((2*c+2.4)/(20-6*sn),3) for c,sn in [(1,0),(0.5,3**.5/2),(0,1)]], 'rest cos',0.6)
print('slope limits',3*m*0+36-28.8,36+28.8)
y=2.4; yh=2/3*y; xf=sqrt(9-yh**2); print('ladder: leave at %.2f m, foot %.3f m, travel %.3f, w2 %.4f, centre %.3f'%(yh,xf,xf-1.8,(3*g*(0.8-yh/3*1)/3) if False else 3*g*(y/3-yh/3)/3, sqrt(3*g*(y/3-yh/3)/3)*1.5))
