import numpy as np, sympy as sp
from scipy.integrate import solve_ivp
r2=2**.5
Ia=2*(2+r2); D=40.; L=.1; C=Ia/(D*L); k=5/6*(D*L)**.5
E=0.080
q0=np.sqrt(2*C*E); V0=q0/C; a0=q0*np.sqrt(L/Ia); w0=np.sqrt(D/Ia); nu=w0/6
print('C',C,'q0',q0,'V0',V0,'a0',a0,'w0',w0,'nu',nu,'T',2*np.pi/nu,'T_S',1.25*2*np.pi/nu)
f=lambda t,y:[y[1],(-D*y[0]+k*y[3])/Ia,y[3],(-k*y[1]-y[2]/C)/L]
Tn=2*np.pi/nu
s=solve_ivp(f,[0,Tn],[0,0,q0,0],rtol=1e-11,atol=1e-13,dense_output=True,max_step=0.01)
fa=lambda t:a0*(-9/13*np.sin(4*nu*t)+4/13*np.sin(9*nu*t))
fq=lambda t:q0*(9/13*np.cos(4*nu*t)+4/13*np.cos(9*nu*t))
ts=np.linspace(0,Tn,400)
print('max err a',max(abs(s.sol(t)[0]-fa(t)) for t in ts),'max err q',max(abs(s.sol(t)[2]-fq(t)) for t in ts))
print('end state',s.sol(Tn))
# earlier recurrence?
Y=np.array([s.sol(t) for t in ts]); y0=np.array([0,0,q0,0])
sc=np.array([a0,a0*nu,q0,q0*nu])
dev=np.abs((Y-y0)/sc).max(axis=1); idx=[i for i in range(5,len(ts)-5) if dev[i]<0.02]; print('near-returns before T',idx)
yh=s.sol(Tn/2); print('T/2',yh,'pred adot',-72/13*a0*nu,'q',5/13*q0)
a,ad,q,i=yh
print('grav',.5*D*a*a,'motion',.5*Ia*ad*ad,'can',.5*q*q/C,'coil',.5*L*i*i,'sum',.5*D*a*a+.5*Ia*ad*ad+.5*q*q/C+.5*L*i*i)
print('fractions',144/169*E,25/169*E)
aa=np.array([fa(t) for t in np.linspace(0,Tn,20000)]); print('max|a|',abs(aa).max(),'theta2 max',r2*abs(aa).max(),'lower disp max',(1+r2)*abs(aa).max(), 'deg',np.degrees(r2*abs(aa).max()))
print('theta^2/6',(r2*abs(aa).max())**2/6)
print('bound a0',a0)
# part a
g=1.25;print('dM c2',100/g,'dK',100-100/g,'dM',0.080/9e16)
