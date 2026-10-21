import sympy as sp, numpy as np
from scipy.integrate import solve_ivp
Ia=4+2*sp.sqrt(2); D=40; L=sp.Rational(1,10); C=Ia/(D*L); k=sp.Rational(5,6)*sp.sqrt(D*L)
w0=sp.sqrt(D/Ia); print('Ia',float(Ia),'C',float(C),'kappa',k,'w0',float(w0),'w0^2',sp.nsimplify(sp.radsimp(w0**2)))
# (a)
Ep,Em=sp.Rational(80,1000),sp.Rational(20,1000)
beta=(Ep-Em)/(Ep+Em); gw=1/sp.sqrt(1-beta**2); print('w/c',beta,'gamma',gw)
dM=(Ep+Em)/gw; print('rest energy gain',dM,'KE gain',(gw-1)*dM)
# (b)
q0=sp.sqrt(2*C*dM); print('q0',float(q0),'V0',float(q0/C))
# (c)
w=sp.symbols('omega',positive=True); A,Q=sp.symbols('A Q')
e1=sp.Eq((D-Ia*w**2)*A,k*w*Q); e2=sp.Eq((1/C-L*w**2)*Q,k*w*A)
Mx=sp.Matrix([[D-Ia*w**2,-k*w],[-k*w,1/C-L*w**2]])
roots=sp.solve(sp.simplify(Mx.det()),w); print('roots/w0',[sp.simplify(r/w0) for r in roots])
for r in roots:
    print('Q/A',sp.simplify(sp.radsimp((k*r/(1/C-L*r**2)))),'sqrt(Ia/L)',float(sp.sqrt(Ia/L)))
nu=w0/6; a0=q0*sp.sqrt(L/Ia); print('a0',float(a0),'nu',float(nu),'T',float(2*sp.pi/nu))
tau=sp.symbols('tau')
af=a0/13*(4*sp.sin(9*nu*tau)-9*sp.sin(4*nu*tau))
qf=q0/13*(9*sp.cos(4*nu*tau)+4*sp.cos(9*nu*tau))
r1=sp.simplify(Ia*af.diff(tau,2)-k*qf.diff(tau)+D*af); r2=sp.simplify(L*qf.diff(tau,2)+qf/C+k*af.diff(tau))
print('residuals',sp.simplify(sp.radsimp(r1)),sp.simplify(sp.radsimp(r2)))
print('ICs',af.subs(tau,0),sp.simplify(af.diff(tau).subs(tau,0)),sp.simplify(qf.subs(tau,0)-q0),qf.diff(tau).subs(tau,0))
Th=2*sp.pi/nu
for lab,tv in [('T/2',Th/2),('T',Th)]:
    vals=[af.subs(tau,tv),af.diff(tau).subs(tau,tv),qf.subs(tau,tv),qf.diff(tau).subs(tau,tv)]
    vals=[sp.simplify(v) for v in vals]
    print(lab,vals,[float(v) for v in vals])
    Ek=Ia*vals[1]**2/2; Eg=D*vals[0]**2/2; Ec=vals[2]**2/(2*C); El=L*vals[3]**2/2
    print('  energies',[sp.nsimplify(sp.simplify(x)) for x in (Eg,Ek,Ec,El)],[float(x) for x in (Eg,Ek,Ec,El)])
# check no earlier recurrence: scan state distance
fa=sp.lambdify(tau,[af,af.diff(tau),qf,qf.diff(tau)],'numpy')
tt=np.linspace(1e-3,float(Th)*1.001,400001); S=np.array(fa(tt))
S0=np.array([0,0,float(q0),0])
scale=np.array([float(a0),float(a0*nu*9),float(q0),float(q0*nu*9)])
dist=np.sqrt((((S.T-S0)/scale)**2).sum(1))
print('min scaled dist before 0.99T',dist[tt<0.99*float(Th)].min())
print('max |a| rad',np.abs(S[0]).max(),'deg',np.degrees(np.abs(S[0]).max()),'max|adot|',np.abs(S[1]).max(),'max|i|',np.abs(S[3]).max())
# numeric run
Ian,Cn,kn,Ln,Dn=float(Ia),float(C),float(k),0.1,40.0
def f(t,y):
    a,ad,q,i=y
    return [ad,(kn*i-Dn*a)/Ian,i,(-q/Cn-kn*ad)/Ln]
Tn=float(Th)
s=solve_ivp(f,[0,Tn],[0,0,float(q0),0],rtol=1e-12,atol=1e-14,dense_output=True)
for lab,tv in [('T/2',Tn/2),('T',Tn)]:
    yn=s.sol(tv); ya=np.array(fa(tv))
    print('num',lab,yn,'dev',yn-ya)
tt=np.linspace(0,Tn,5001); Y=s.sol(tt); YA=np.array(fa(tt))
print('max dev over run per coord',np.abs(Y-YA).max(1))
E=Ian*Y[1]**2/2+Dn*Y[0]**2/2+Y[2]**2/(2*Cn)+Ln*Y[3]**2/2
print('energy',E.min(),E.max())
# (e)
v=sp.symbols('v',positive=True); c=sp.symbols('c',positive=True)
vs=sp.solve(sp.Eq(Ep*(c-v),Em*(c+v)),v); print('v',vs)
gm=sp.symbols('gamma',positive=True)
print('gamma',sp.solve(sp.Eq(Ep*Em*gm**2*(c-vs[0])*(c+vs[0])/c**2,Ep*Em),gm))
print('E primes',Ep*sp.Rational(5,4)*sp.Rational(2,5),Em*sp.Rational(5,4)*sp.Rational(8,5))
TS=1.25*Tn; print('T_S',TS,'dist',1.8e8*TS)
