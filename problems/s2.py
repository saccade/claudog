from sympy import *
th=symbols('th')
c,s=cos(th),sin(th)
ratio=(2*c+Rational(12,5))/(Rational(98,5)-6*s)
import numpy as np
f=lambdify(th,ratio); xs=np.linspace(0,np.pi/2,100001); v=f(xs); i=v.argmax()
print('spool max f/N',v[i],np.degrees(xs[i]),np.cos(xs[i]))
print(simplify(ratio.subs({th:atan2(3,4)})))
# rocking wheel: v_cm^2 vs theta from release cos=0.6
R,h,g,b=0.3,0.05,9.8,0.15
I=lambda t:0.3825-0.09*np.cos(t)
ts=np.linspace(-np.arccos(0.6),np.arccos(0.6),20001)
td2=2*g*b*(np.cos(ts)-0.6)/I(ts)
d2=R**2+h**2-2*R*h*np.cos(ts)
vc2=d2*td2
print('vcm max at deg',np.degrees(ts[vc2.argmax()]),'td max at',np.degrees(ts[td2.argmax()]))
# k^2 identity
print(0.035+0.0625, 0.2925/3)
# contact-torque correction: Mt*(rcm-rP) x aP vs (1/2)I' thdot^2
t,Mt,m,a,RR,hh,w=symbols('t M_t m a R h w')
print(simplify(Mt*(-hh*sin(t))*RR*w**2 + Rational(1,2)*diff(-2*m*a*RR*cos(t),t)*w**2).subs(hh,m*a/Mt))
