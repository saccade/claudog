import numpy as np
from scipy.integrate import solve_ivp
Ia=4+2*np.sqrt(2); D=40.; Lc=0.10; C=Ia/(D*Lc); kap=5/3
w0=np.sqrt(D/Ia); nu=w0/6; q0=np.sqrt(2*C*0.08); Tr=2*np.pi/nu
f=lambda t,y:[y[1],(kap*y[3]-D*y[0])/Ia,y[3],(-y[2]/C-kap*y[1])/Lc]
s=solve_ivp(f,[0,Tr],[0,0,q0,0],rtol=1e-12,atol=1e-15)
print(s.y[:,-1]-np.array([0,0,q0,0]))
a0=q0*np.sqrt(Lc/Ia); print("adot T/2 closed",-72/13*a0*nu, "q",5/13*q0, "V",5/13*q0/C)
# p3 small period check at smaller amplitude
