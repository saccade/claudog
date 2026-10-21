import numpy as np
w0=np.sqrt(40/(4+2*np.sqrt(2))); nu=w0/6; T=2*np.pi/nu
a0=np.sqrt(0.004); q0=0.5226251859505506
t=np.linspace(0.01*T,0.99*T,2000001); x=nu*t
a=a0/13*(4*np.sin(9*x)-9*np.sin(4*x)); ad=a0*nu/13*36*(np.cos(9*x)-np.cos(4*x))
q=q0/13*(9*np.cos(4*x)+4*np.cos(9*x)); i=-q0*nu/13*36*(np.sin(4*x)+np.sin(9*x))
d=np.sqrt((a/a0)**2+(ad/(a0*nu*9))**2+((q-q0)/q0)**2+(i/(q0*nu*9))**2)
print(d.min(), t[d.argmin()]/T)
print('max i',np.abs(i).max())
