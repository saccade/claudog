import sympy as sp
g=10
# 1 pendulum (Codex room 1): m=1, l=1, th0=0.1
th0=sp.Rational(1,10)
heft=g*(1-sp.cos(th0)); print('heft',float(heft))
print('max sweep',float(th0*sp.sqrt(g)), 'period',float(2*sp.pi/sp.sqrt(g)))
# 2 constant power wheel I=0.5, w0=4, P=3, 4 s
I=sp.Rational(1,2);w0=4;P=3;t=sp.symbols('t')
w=sp.sqrt(w0**2+2*P*t/I)
print('w(4)',w.subs(t,4),'theta',float(sp.integrate(w,(t,0,4))),'turns',float(sp.integrate(w,(t,0,4))/(2*sp.pi)))
print('chi0',P/w0,'chi4',float(P/w.subs(t,4)),'alpha0',P/w0/I,'alpha4',float(P/8/I))
# governor l=0.5, w=5
l=sp.Rational(1,2);print('cos',g/(l*25),'angle deg',float(sp.acos(sp.Rational(4,5))*180/sp.pi))
# matching marble
b=sp.Rational(1,20);l1=1;Rb=sp.Rational(5,7)*l1;print('R-b',float(Rb),'R',float(Rb+b))
Tm=2*sp.pi*sp.sqrt(7*Rb/(5*g));print('marble T',float(Tm),'pend T',float(2*sp.pi/sp.sqrt(g)))
# ribbon
print('ribbon w', 2.0/0.6, 8*5/12)
# ladder g=10
L=3;c0=sp.Rational(4,5);cl=sp.Rational(16,10)/3
w2=3*g*(c0-cl)/L;print('ladder leave w^2',w2,float(w2),'vcm',float(sp.sqrt(w2)*L/2),'sqrt6',float(sp.sqrt(6)))
# leaves at 2/3 height? derive: wall normal N = m*ax_cm; check cos=2/3 c0
print('leave at y=',float(sp.Rational(2,3)*2.4))
# spool
M=2;R=sp.Rational(1,5);r=sp.Rational(3,25);Ia=sp.Rational(1,25);F=6;th=sp.symbols('th')
a=F*(R*sp.cos(th)-r)/(R*(M+Ia/R**2))
for d in (0,60,90):
    ad=sp.nsimplify(a.subs(th,d*sp.pi/180));N=M*g-F*sp.sin(d*sp.pi/180);f=M*ad-F*sp.cos(d*sp.pi/180)
    f=sp.N(M*ad*0+ (M*ad-F*sp.cos(d*sp.pi/180)) ,6)
    print(d,'a',float(ad),'N',float(N),'f',float(f),'mu',float(abs(f)/N))
print('rest cos',r/R)
