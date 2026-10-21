from sympy import *
g=Rational(98,10); th,t,w,wd=symbols('theta t omega omegadot',real=True)
# P1
I1=2*Rational(1,4)+1*Rational(1,4); k1=(2-1)*Rational(1,2)*g
print('P1',I1,k1,N(2*pi*sqrt(I1/k1)),N(2*pi*sqrt(I1/(3*g/2))),'U',k1*(1-cos(th)))
# P2 general derivation
a,f,F,M,R,r,Ic,T=symbols('a f F M R r I_C T')
sol=solve([Eq(M*a,F*cos(T)+f),Eq(Ic*(-a/R),F*r+f*R)],[a,f])
print('P2',simplify(sol[a]),simplify(sol[f]))
vals={F:6,M:2,R:Rational(2,10),r:Rational(1,10),Ic:Rational(4,100)}
for d in [0,60,90]:
    s={**vals,T:d*pi/180}; print(d,N(sol[a].subs(s)),N(sol[f].subs(s)),N(2*g-6*sin(d*pi/180)))
# P3
P,I,w0=3,Rational(1,2),4
om=sqrt(w0**2+2*P*t/I); print('P3',om.subs(t,4),N(integrate(om,(t,0,4))),[N(P/om.subs(t,x)) for x in (0,4)],[N(P/om.subs(t,x)/I) for x in (0,4)])
# P4
m,v0,r0,rf=Rational(1,2),2,Rational(6,10),Rational(3,10); x=symbols('x',positive=True)
vf=v0*r0/rf; print('P4',vf,N(vf/rf),N(v0/r0),N(m*v0**2/r0),N(m*vf**2/rf),N(m*(vf**2-v0**2)/2),N(integrate(m*(v0*r0)**2/x**3,(x,rf,r0))))
# P5
M5,R5,m5,a5=2,Rational(3,10),1,Rational(15,100); Mt=M5+m5; d=m5*a5/Mt
IO=M5*R5**2/2+m5*a5**2; Icm=IO-Mt*d**2
IP=IO+Mt*R5**2-2*Mt*R5*d*cos(th); U=Mt*g*d*(1-cos(th))
print('P5',d,IO,Icm,expand(IP),U)
print(N(2*pi*sqrt(IP.subs(th,0)/(Mt*g*d))),N(2*pi*sqrt(IO/(Mt*g*d))))
E=U.subs(th,pi/3); wb=sqrt(2*E/IP.subs(th,0)); vc=wb*(R5-d)
print(N(E),N(wb),N(vc),N(Mt*vc**2/2),N(Icm*wb**2/2))
# Lagrange check
q=Function('q')(t); L=IP.subs(th,q)*diff(q,t)**2/2-U.subs(th,q)
eq=diff(diff(L,diff(q,t)),t)-diff(L,q)
qdd=solve(eq,diff(q,t,2))[0]
Pg=-diff(U.subs(th,q),t)
print(simplify(diff(q,t)*qdd - (Pg-diff(IP.subs(th,q),q)*diff(q,t)**3/2)/IP.subs(th,q)))
