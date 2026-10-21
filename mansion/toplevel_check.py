"""Checks every number in the clean-slate top-level problem set (Claude, 2026-10-21)."""
from math import sqrt, pi, cos, acos, degrees, log
g=10.0
out=[]
def p(k,v): out.append((k,v)); print(f"{k:40s} {v:.4g}")
# 1 knife
m,l,th=1.0,1.0,0.10
U=m*g*l*th**2/2; p('1a PE (J)',U); p('1b vmax (m/s)',sqrt(2*U/m)); p('1c T (s)',2*pi*sqrt(l/g))
# 2 engine + flywheel
Qh,W=15.0,3.0; p('2a Qc (J)',Qh-W); p('2a eff',W/Qh); p('2a P (W)',W*1.0)
I,w0,P,t=0.50,4.0,3.0,4.0
K0=I*w0**2/2; K1=K0+P*t; w1=sqrt(2*K1/I); p('2b w1 (rad/s)',w1); p('2b torque0 (N m)',P/w0); p('2b torque1 (N m)',P/w1)
# 3 governor + spool
lg,wg=0.50,5.0; c=g/(lg*wg**2); p('3a cos',c); p('3a angle (deg)',degrees(acos(c))); p('3a rise (m)',lg*(1-c)); p('3a PE each (J)',1.0*g*lg*(1-c)); p('3a w_min (rad/s)',sqrt(g/lg))
ms,R,r,Is,F=2.0,0.20,0.12,0.040,6.0
a=F*(1-r/R)/(ms+Is/R**2); p('3b a (m/s^2)',a); p('3b balance angle (deg)',degrees(acos(r/R)))
# 4 ladder
M,L,x0,y0,yf=8.0,3.0,1.8,2.4,1.6
p('4a top speed (m/s)',(x0/y0)*0.40)
dh=(y0-yf)/2; E=M*g*dh; p('4b PE released (J)',E); p('4c trans (J)',E*3/4); p('4c rot (J)',E/4); p('4c vcm (m/s)',sqrt(2*E*3/4/M))
# 5 cue
mb,Rb,J=1.0,0.050,2.0; Ib=0.4*mb*Rb**2
v=J/mb; H=Rb+Ib/(mb*Rb); p('5a v (m/s)',v); p('5b H (m)',H); p('5c w (rad/s)',v/Rb); p('5c Kt (J)',mb*v*v/2); p('5c Kr (J)',Ib*(v/Rb)**2/2)
# 6 basin
aa=5/7; p('6a T ball (s)',2*pi*sqrt(1.4*aa/g)); p('6b T bead (s)',2*pi*sqrt(aa/g))
# 7 hoop
Rh,wh=0.25,8.0; V=Rh*wh; p('7a V (m/s)',V); p('7b top (m/s)',2*V); p('7c side (m/s)',sqrt(2)*V)
# 8 ribbon
mp,r1,r2,v1=0.50,0.60,0.30,2.0; v2=v1*r1/r2
p('8a v2 (m/s)',v2); p('8a w2 (rad/s)',v2/r2); p('8b T1 (N)',mp*v1**2/r1); p('8b T2 (N)',mp*v2**2/r2); p('8c W (J)',mp*(v2**2-v1**2)/2)
# 9 double pendulum
wa=sqrt((2-sqrt(2))*g/1.0); wb=sqrt((2+sqrt(2))*g/1.0)
p('9a wa (rad/s)',wa); p('9a wb (rad/s)',wb); p('9a Ta (s)',2*pi/wa); p('9a Tb (s)',2*pi/wb); p('9b ratio',wb/wa); p('9b 1+sqrt2',1+sqrt(2))
# 10 RC, LC, coupling
Rr,Cr,V0=20.0,0.10,6.0
p('10a I0 (A)',V0/Rr); p('10a tau_RC (s)',Rr*Cr); p('10a t to 4 V (s)',Rr*Cr*log(3)); p('10a Q at 4 V (C)',Cr*4.0); p('10a U at 4 V (J)',Cr*16/2)
eta=2*(2+sqrt(2)); D=40.0; Lc=0.10; C=eta/(D*Lc)
w0c=1/sqrt(Lc*C); p('10b C (F)',C); p('10b w0 (rad/s)',w0c)
p('10d w_low',2/3*w0c); p('10d w_high',1.5*w0c); p('10d product',(2/3*w0c)*(1.5*w0c)); p('10d w0^2',w0c**2)
# 11 line
Lp,Cp=0.50e-6,0.20e-9; u=1/sqrt(Lp*Cp); Z=sqrt(Lp/Cp); p('11a u (m/s)',u); p('11a Z (ohm)',Z)
p('11b E per m (nJ)',0.5*Cp*12**2*1e9); p('11b each wave P (W)',36/Z)
fp,fm=5.0e6,4.0e6; p('11c slow (m/s)',u*(fp-fm)/(fp+fm)); p('11c fast (m/s)',u*(fp+fm)/(fp-fm)); p('11c fast/c',u*(fp+fm)/(fp-fm)/3e8)
# 12 two lights
c0=3.0e8; E1,E2=80e-3,20e-3; Et=E1+E2; pc=E1-E2
p('12a Etot (mJ)',Et*1e3); p('12a p (kg m/s)',pc/c0); p('12b Mc2 (mJ)',sqrt(Et**2-pc**2)*1e3); vv=pc/Et; gam=1/sqrt(1-vv**2)
p('12c v/c',vv); p('12c gamma',gam); p('12d dt0 for 10 s (s)',10/gam)
# 13 chair
E0=0.080; q0=sqrt(2*C*E0); nu=w0c/6; T=2*pi/nu
p('13a q0 (C)',q0); p('13a V0 (V)',q0/C); p('13b T (s)',T); p('13c q(T/2)/q0',9/13*cos(4*nu*T/2)+4/13*cos(9*nu*T/2)); p('13c can share',(5/13)**2); p('13c can (mJ)',(5/13)**2*E0*1e3); p('13c rest (mJ)',(1-(5/13)**2)*E0*1e3)
p('13d T in S (s)',gam*T); p('13d distance (m)',vv*c0*gam*T)
