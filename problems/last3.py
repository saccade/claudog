import sympy as sp, numpy as np
L=0.5e-6; C=0.2e-9
u=1/np.sqrt(L*C); Z=np.sqrt(L/C); print('u',u,'Z',Z)
x,t,Vp,Vm=sp.symbols('x t Vp Vm')
# energy / power identity
Vv=Vp+Vm; I=(Vp-Vm)/sp.Float(Z)
e=sp.simplify(((sp.Float(C)*Vv**2+sp.Float(L)*I**2)/2)-sp.Float(C)*(Vp**2+Vm**2)); print('energy diff',sp.N(e,5))
P=sp.expand(Vv*I); print('power', P, '(Vp^2-Vm^2)/Z =', (Vp**2-Vm**2)/Z)
print('energy at 6,6:',C*(36+36),'J/m ; each wave', C*36, 'power each',36/Z)
# product check
fp,fm=5e6,4e6; wp,wm=2*np.pi*fp,2*np.pi*fm; kp,km=wp/u,wm/u
print('w',wp,wm,'k',kp,km,'lambda',2*np.pi/kp,2*np.pi/km)
xs=np.linspace(0,300,7);ts=np.linspace(0,2e-6,5)
X,T=np.meshgrid(xs,ts)
lhs=6*np.cos(kp*X-wp*T)+6*np.cos(km*X+wm*T)
rhs=12*np.cos(.5*((kp+km)*X-(wp-wm)*T))*np.cos(.5*((kp-km)*X-(wp+wm)*T))
print('max diff',abs(lhs-rhs).max())
print('half coeffs',.5*(kp+km),.5*(wp-wm),.5*(kp-km),.5*(wp+wm))
v1=(wp-wm)/(kp+km); v2=(wp+wm)/(kp-km); print('v1',v1,'v2',v2,'v1v2',v1*v2,'u^2',u*u,'v2/c',v2/3e8)
print('90 m: stripe',90/v2,'front',90/u)
# PDE check on right wave
f=sp.cos(sp.Symbol('k')*(x-sp.Float(u)*t))
