from sympy import *
import numpy as np
from scipy.integrate import solve_ivp
R=Rational(1,20); h=Rational(2,25); v0=Rational(21,10); Ip=Rational(2,5)*R**2
w0=v0*h/Ip; print('w0',w0,'R w0',R*w0)
v=Rational(9,7)*v0; print('v',v, 'w',v/R)
Eb=v0**2/2+Ip*w0**2/2; Ea=v**2/2+Ip*(v/R)**2/2; print(float(v0**2/2),float(Ip*w0**2/2),float(Eb),float(v**2/2),float(Ip*(v/R)**2/2),float(Ea),float(Eb-Ea))
print('skid t',(v-v0)/2,'d',v0*(v-v0)/2+(v-v0)**2/2/2*2/ (1) )
t=(v-v0)/2; print('dist',float(v0*t+Rational(1,2)*2*t**2))
# striker
M=Rational(5,7);V=Rational(21,5);J=symbols('J');Ja=v0
Vp=V-J/M; J_=Ja
print('Vp',V-Ja/M,'E_str',float(M*V**2/2),float(M*(V-Ja/M)**2/2),'contact',float(v0+h*w0),'sep',float(v0+h*w0-(V-Ja/M)))
# rod
m=Rational(3,5);L=Rational(6,5);J=Rational(9,5);print('rod v',J/m,'w',J*L/2/(m*L**2/12),'d',(J/m)/(J*L/2/(m*L**2/12)))
# cube
s=Rational(3,10);print('cube',Rational(3,8),float(sqrt(16*10*s*(sqrt(2)-1)/2/3*2/2)))
vt=symbols('vt',positive=True);print('vthr',float(solve(Rational(3,16)*vt**2-10*s*(sqrt(2)-1)/2,vt)[0]))
# superball
v1=(3*2.1)/7;Rw1=10*2.1/7;print(v1,Rw1,Rw1/0.025,(3*v1+4*Rw1)/7,(10*v1-3*Rw1)/7)
# marble
a=Rational(5,7);print('T',float(2*pi/sqrt(10)),'bead',float(2*pi/sqrt(14)),'cen',float(a*sqrt(10)*Rational(1,10)),'own',float(a/Rational(1,20)*sqrt(10)*Rational(1,10)),'heft',float(10*a*Rational(1,100)/2))
# beam
for (b,I) in [(Rational(1,2),Rational(3,4)),(Rational(3,2),Rational(3,4)),(0,1)]:
    print('beam',b,I, float(2*pi/sqrt(10*b/I)) if b else 'inf')
# garden wheel
eta=lambda p:0.3825-0.09*np.cos(p)
print('eta0',eta(0),'w',np.sqrt(2*0.6/eta(0)),'v',0.25*np.sqrt(2*0.6/eta(0)))
print('T roll',2*np.pi/np.sqrt(1.5/0.2925),'T fixed',2*np.pi/np.sqrt(1.5/0.1125))
# numerical: phi0 with lump 0.09 below axle -> cos=0.6
def f(t,y):
    p,w=y; e=eta(p); de=0.09*np.sin(p)
    # d/dt(1/2 e w^2)= -dU/dt ; U=-1.0*10*0.15*cos p  => dU/dp=10*.15*sin p
    return [w,(-1.5*np.sin(p)-0.5*de*w*w)/e]
sol=solve_ivp(f,[0,5],[np.arccos(0.6),0],rtol=1e-10,atol=1e-12,dense_output=True)
ts=np.linspace(0,5,200001);ps=sol.sol(ts)
print('bottom w',max(abs(ps[1])),'cm ratio punch/hook', 25/14)
print('wheel energy punch', 0.5*3*(0.25*2.025)**2)
# puck
print('puck',0.6*2,0.3*4,4/0.3,0.5*4/0.6,0.5*16/0.3,0.5*0.5*(64-4))
