from sympy import *
g=Rational(98,10)
# P1
I1=2*Rational(1,4)+1*Rational(1,4); k1=(2-1)*g/2; k2=3*g/2
print('P1',I1,k1,N(2*pi*sqrt(I1/k1)),N(2*pi*sqrt(I1/k2)))
# P2
th=symbols('th'); M,R,Ia,r,F=2,Rational(1,5),Rational(1,25),Rational(12,100),6
# unknowns a (right), alpha (ccw), f, Nn
a,al,f,Nn=symbols('a al f Nn')
# cord tangent point: position p s.t. F direction d, torque about O = +rF
d=Matrix([cos(th),sin(th)]); p=r*Matrix([sin(th),-cos(th)])
tqO=p[0]*F*d[1]-p[1]*F*d[0]
eqs=[M*a-(F*cos(th)+f), Ia*al-(simplify(tqO)+(-0*f-(-R)*f)), a+R*al]
# friction f at (0,-R), force (f,0): torque = x*Fy - y*Fx = R f
sol=solve(eqs,[a,al,f]); print('P2',simplify(tqO),simplify(sol[a]),simplify(sol[f]))
for t in [0,60,90]:
    tt=rad(t); print(t,N(sol[a].subs(th,tt)),N(sol[f].subs(th,tt)),N(M*g-F*sin(tt)))
print(N(acos(r/R)*180/pi))
# P3
P,I,w0=3,Rational(1,2),4; t=symbols('t',positive=True)
w=sqrt(w0**2+2*P*t/I); print('P3',w.subs(t,4),N(integrate(w,(t,0,4))),Rational(P)/w0,P/w.subs(t,4))
# P4
m,ri,vi,rf=Rational(1,2),Rational(6,10),2,Rational(3,10); rr=symbols('rr',positive=True)
vf=vi*ri/rf; print('P4',vf,N(vf/rf),m*vi**2/ri,N(m*vf**2/rf),m*(vf**2-vi**2)/2,integrate(m*vi**2*ri**2/rr**3,(rr,rf,ri)))
# P5
M,m,R,a=2,1,Rational(3,10),Rational(15,100)
q=Function('q')(symbols('t')); tt=symbols('t')
xO=R*q; pm=Matrix([xO-a*sin(q),-a*cos(q)])
T=Rational(1,2)*M*diff(xO,tt)**2+Rational(1,2)*(M*R**2/2)*diff(q,tt)**2+Rational(1,2)*m*(pm.diff(tt).dot(pm.diff(tt)))
IP=simplify(2*T/diff(q,tt)**2); print('IP',IP)
U=m*g*a*(1-cos(q)); kk=m*g*a
I0=IP.subs(q,0); print('T roll',N(2*pi*sqrt(I0/kk)),'T axle',N(2*pi*sqrt((M*R**2/2+m*a**2)/kk)))
U0=U.subs(q,acos(Rational(3,5))); wb=sqrt(2*U0/I0); b=m*a/(M+m)
vc=(R-b)*wb; Kt=Rational(1,2)*(M+m)*vc**2
print(N(U0),N(wb),N(vc),N(Kt),N(U0-Kt), I0-(M+m)*(R-b)**2)
