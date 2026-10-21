from sympy import *
x,y,z,s,rho,R,r,th,ph,d,e=symbols('x y z s rho R r theta phi d e',positive=True)
# cube: axis through face centres (along z, through centre) and about an edge (x=-s/2,y=-s/2)
M=rho*s**3
Ic=integrate(integrate(integrate(rho*(x**2+y**2),(x,-s/2,s/2)),(y,-s/2,s/2)),(z,-s/2,s/2))
Ie=integrate(integrate(integrate(rho*((x+s/2)**2+(y+s/2)**2),(x,-s/2,s/2)),(y,-s/2,s/2)),(z,-s/2,s/2))
print('cube Ic/M',simplify(Ic/M),'Iedge/M',simplify(Ie/M))
# parallel axis, generic: sum m(x+d)^2+(y+e)^2 with sum m x = sum m y = 0
n=4; ms=symbols('m0:4'); xs=symbols('x0:4'); ys=symbols('y0:4')
Ishift=sum(ms[i]*((xs[i]+d)**2+(ys[i]+e)**2) for i in range(n))
I0=sum(ms[i]*(xs[i]**2+ys[i]**2) for i in range(n)); Mt=sum(ms)
rest=expand(Ishift-I0-Mt*(d**2+e**2)); print('parallel-axis remainder =',factor(rest),'(zero when centroid at origin)')
# sphere 2/5 check
Isph=integrate(integrate(integrate(rho*(r*sin(th))**2*r**2*sin(th),(r,0,R)),(th,0,pi)),(ph,0,2*pi))
print('sphere I/(M R^2)',simplify(Isph/(rho*Rational(4,3)*pi*R**3)/R**2))
# contact-point material acceleration for rolling: centre at X(t), angle q(t) with X'=R q'
t=symbols('t'); X=Function('X')(t); q=X/R
P=Matrix([X,R])+R*Matrix([-sin(q),-cos(q)])  # material point at bottom when q=0 ... general point
a=P.diff(t,2); print('contact accel at q=0:',simplify(a.subs(X,0)))
