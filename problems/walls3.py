from sympy import *
t,R,u,A=symbols('t R u A',positive=True)
X=Function('X')(t); q=X/R
P=Matrix([X,R])+R*Matrix([-sin(q),-cos(q)])
v=P.diff(t); a=P.diff(t,2)
sub=lambda E: simplify(E.subs(Derivative(X,(t,2)),A).subs(Derivative(X,t),u).subs(X,0))
print('contact vel',sub(v),'contact accel',sub(a),'(centre is at +y, distance R)')
