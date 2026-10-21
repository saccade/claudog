from sympy import *
th,F,R,r,M,Ic=symbols('theta F R r M I_C',positive=True)
# P2 torque about contact, clockwise positive; tangent point r(sin,-cos) from centre, contact (0,-R)
px,py=r*sin(th),-r*cos(th)+R
tau_cw=-(px*F*sin(th)-py*F*cos(th))
print('P2 tau_cw',simplify(tau_cw))
ax=R*tau_cw/(Ic+M*R**2)
v={F:6,R:Rational(1,5),M:2,Ic:Rational(1,25)}
print('a_x',expand(ax.subs(v).subs(r,Rational(1,10))),' r=0.12:',expand(ax.subs(v).subs(r,Rational(12,100))), N(acos(Rational(3,5))*180/pi))
# P5 numbers
g=Rational(98,10); Mt=3; h=Rational(1,20); R5=Rational(3,10)
IO=Rational(9,80); Icm=IO-Mt*h**2; I=lambda t: Rational(153,400)-Rational(9,100)*cos(t)
print('Z_C',Icm/Mt,'Z0',I(0)/Mt,'zeta_bot',N(Rational(147,200)/I(0)),'swirl_bot',N(I(0)/Mt*sqrt(2*Rational(147,200)/I(0))))
print('split ratio',(Mt*(R5-h)**2)/Icm, N(Mt*(R5-h)**2/(Mt*(R5-h)**2+Icm)))
# large-swing period, 60 deg
gb=g*Rational(15,100); t0=pi/3
f=lambda t: sqrt(I(t)/(2*gb*(cos(t)-cos(t0))))
import mpmath as mp
T=4*mp.quad(lambda u: float(N(f(t0*mp.sin(u)).subs({})))*float(t0)*mp.cos(u),[0,mp.pi/2])
print('T60',T,'small',N(2*pi*sqrt(I(0)/gb)))
# P3 mean-speed comparison, P1(c) ratio
print(N(Rational(448,18)), N(sqrt(3)), N(2.458/1.419))
