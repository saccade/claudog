import sympy as sp, numpy as np
from scipy.integrate import solve_ivp
g=10
# P1 skidding ball
m=1.0;R=0.050;v0=2.1;mu=0.20
h_over=sp.Rational(4,5)
w0=2*v0/R; vf=9*v0/7; wf=vf/R
KE0=0.5*m*v0**2+0.5*(0.4*m*R**2)*w0**2
KEf=0.5*m*vf**2*1.4
print('P1 w0',w0,'vf',vf,'wf',wf,'KE0',KE0,'KEf',KEf,'loss',KE0-KEf,(KE0-KEf)/KE0,'tskid',(vf-v0)/(mu*g),'dist', v0*(vf-v0)/(mu*g)+0.5*mu*g*((vf-v0)/(mu*g))**2)
# sweet spot: v=v0 -> (R+h)/R=7/5 => h/R=2/5
# P2 marble
b=0.05;Rc=0.30
w2=np.sqrt(5/7*g/(Rc-b));print('P2 T',2*np.pi/w2,'bead T',2*np.pi/np.sqrt(g/(Rc-b)),'ratio',np.sqrt(7/5))
# P3 wheel
M=2.0;mm=1.0;Rw=0.30;a=0.15
Mt=M+mm
th=sp.symbols('theta')
# CM relative to O: mass at angle theta from straight down (clockwise): position x=a sin th, y=-a cos th
# CM: (m/Mt) a (sin th, -cos th)
I_O=M*Rw**2/2+mm*a**2
print('I_O',I_O, 'Icm_stable', I_O-Mt*(mm/Mt*a)**2)
# contact point P = (x_O, -R) ; O = (R th, 0)  x_O=R*th
# KE = 1/2 I_P(th) thdot^2, I_P = I_cm + Mt*|CM-P|^2
rcm=(mm/Mt)*a
Icm=I_O-Mt*rcm**2
xcm=Rw*th+rcm*sp.sin(th); ycm=-rcm*sp.cos(th)
dx=xcm-Rw*th; dy=ycm+Rw
IP=Icm+Mt*(dx**2+dy**2)
IPs=sp.simplify(IP)
print('IP(th)=',IPs)
U=Mt*g*(ycm+rcm)  # above min (ycm min=-rcm)
th0=sp.atan2(sp.Rational(12,100),sp.Rational(9,100))  # mass 0.12 left? angle from stable
# clockwise from stable orientation: mass left of O -> counterclockwise? treat sign by symmetry; magnitude th0
th0=float(sp.atan(12/9))
print('th0 deg',np.degrees(th0))
Uf=sp.lambdify(th,U);IPf=sp.lambdify(th,IPs)
print('U0',Uf(th0),'IP0',IPf(th0),'IP stable',IPf(0))
# small oscillation: omega^2 = Mt g rcm / IP(0)
w3=np.sqrt(Mt*g*rcm/IPf(0));print('omega small',w3,'T',2*np.pi/w3)
wfix=np.sqrt(mm*g*a/I_O);print('fixed axle omega',wfix,'T',2*np.pi/wfix)
# bottom speed: 1/2 IP(0) w^2 = U0
wb=np.sqrt(2*Uf(th0)/IPf(0));print('w bottom',wb,'vcm',wb*Rw if False else None)
# CM speed at bottom: CM at distance from contact: dy at 0 = R - rcm ; vcm = w*(R-rcm)
print('vcm',wb*(Rw-rcm), 'vO',wb*Rw)
K=Uf(th0)
Ktrans=0.5*Mt*(wb*(Rw-rcm))**2; Krot=0.5*Icm*wb**2
print('K total',K,'trans',Ktrans,'rot',Krot,Ktrans/K)
