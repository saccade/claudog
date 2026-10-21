import sympy as sp
R_=sp.Rational
print("== room 1")
x,y,xd=R_(18,10),R_(24,10),R_(4,10); L=3
yd=-x*xd/y; print("top speed",yd)
foot=sp.Matrix([x,0]); top=sp.Matrix([0,y]); vf=sp.Matrix([xd,0]); vt=sp.Matrix([0,yd])
rel=vt-vf; lev=top-foot
print("rel",rel.T,"|rel|",rel.norm(),"dot",rel.dot(lev/L))
wz=(lev[0]*rel[1]-lev[1]*rel[0])/L**2; print("omega_z (+ccw)",wz)
c=(foot+top)/2; vc=(vf+vt)/2; print("centre",c.T,"vc",vc.T,"pace",vc.norm(),"dot",c.dot(vc),"|c|",c.norm())
IC=sp.Matrix([x,y]); rot=lambda r: wz*sp.Matrix([-r[1],r[0]])
for n,p,v in [("foot",foot,vf),("top",top,vt),("centre",c,vc)]:
    r=p-IC; print(n,"lever",r.norm(),"pred",rot(r).T,"actual",v.T)
print("== room 2")
m,Lr,J=R_(6,10),R_(12,10),R_(18,10)
v=J/m; I=m*Lr**2/12; r=sp.Matrix([0,Lr/2]); Jv=sp.Matrix([J,0])
tz=r[0]*Jv[1]-r[1]*Jv[0]; w=tz/I; print("v",v,"I",I,"Lz",tz,"omega_z",w)
Z=Lr**2/12; print("Z",Z,"v(L/2)/Z",v*(Lr/2)/Z)
d=sp.symbols('d'); vp=sp.Matrix([v,0])+w*sp.Matrix([-(-d),0]); dd=sp.solve(vp[0],d)[0]
print("still pt d south",dd,"from north end",Lr/2+dd,"frac",(Lr/2+dd)/Lr)
print("rel vel at d south (x):",(w*sp.Matrix([d,0]))[0])
ZP=Z+dd**2; print("ZP",ZP,"ZP/d",ZP/dd)
print("== room 3")
g,th,Ls=sp.symbols('g theta L',positive=True)
ZP3=Ls**2/12+Ls**2/4; print("Z",ZP3,ZP3.subs(Ls,3))
s=sp.symbols('s',positive=True); w2=sp.solve(sp.Eq(ZP3*sp.Symbol('W')/2,g*Ls/2*(R_(4,5)-s)),sp.Symbol('W'))[0]
print("omega^2",sp.simplify(w2))
f=s**2*(R_(4,5)-s); print("max at",sp.solve(sp.diff(f,s),s))
s0=sp.symbols('s0',positive=True); print("general",sp.solve(sp.diff(s**2*(s0-s),s),s))
# full dynamics check with theta(t): wall force, floor force
t=sp.symbols('t'); TH=sp.Function('T')(t)
xc=Ls/2*sp.cos(TH); yc=Ls/2*sp.sin(TH)
# use omega^2 general: thetadot = -sqrt(3g(s0 - sin)/L)
thd=-sp.sqrt(3*g*(s0-sp.sin(th))/Ls); thdd=sp.diff(thd**2/2,th)
ax=sp.diff(sp.diff(xc,t),t).subs(sp.Derivative(TH,(t,2)),thdd).subs(sp.Derivative(TH,t),thd).subs(TH,th)
ay=sp.diff(sp.diff(yc,t),t).subs(sp.Derivative(TH,(t,2)),thdd).subs(sp.Derivative(TH,t),thd).subs(TH,th)
ax=sp.simplify(ax); ay=sp.simplify(ay); print("Nwall/m",sp.factor(ax)); print("Nfloor/m",sp.simplify(g+ay))
Nf=sp.lambdify((th,),(g+ay).subs({g:9.8,Ls:3,s0:0.8}))
import math
print("Nfloor/m at s=0.8, s=8/15:",Nf(math.asin(0.8)),Nf(math.asin(8/15)))
sv=R_(8,15); W2=(3*g*(R_(4,5)-sv)/Ls).subs({g:R_(98,10),Ls:3})
print("omega^2",W2,float(W2),"omega",float(sp.sqrt(W2)),"vc",float(R_(3,2)*sp.sqrt(W2)),"vx",float(R_(3,2)*sp.sqrt(W2)*sv))
print("hookP",float(3*W2/2),"punch",float(R_(9,4)*W2/2),"hookC",float(R_(3,4)*W2/2),"heft",float(R_(98,10)*(R_(6,5)-R_(3,2)*sv)),"top h",3*sv)
print("== room 4")
vx,w,Rb,v1,w1=sp.symbols('v_x omega R v1 w1')
Zb=2*Rb**2/5
# sign check: L_z about contact, centre at (0,R), omega>0 = topspin = clockwise => omega_z=-omega
Lz=(0*0-Rb*vx)+Zb*(-w); print("Lz/m about contact",sp.expand(Lz))
sol=sp.solve([sp.Eq(vx*Rb+Zb*w,v1*Rb+Zb*w1),sp.Eq(vx**2+Zb*w**2,v1**2+Zb*w1**2)],[v1,w1],dict=True)
for so in sol: print(sp.simplify(so[v1]),"|",sp.simplify(so[w1]))
vp_=(3*vx+4*Rb*w)/7; wp_=(10*vx-3*Rb*w)/(7*Rb)
print("slip",sp.simplify(vp_-Rb*wp_+(vx-Rb*w)))
M=sp.Matrix([[R_(3,7),4*Rb/7],[10/(7*Rb),-R_(3,7)]]); print("M^2",sp.simplify(M*M)); print("eig",M.eigenvects())
n={vx:R_(21,10),w:0,Rb:R_(25,1000)}; a=vp_.subs(n); b=wp_.subs(n); print("v'",a,"w'",b)
print("v''",((3*a+4*n[Rb]*b)/7),"w''",(10*a-3*n[Rb]*b)/(7*n[Rb]))
print("swirl",n[vx]*n[Rb],a*n[Rb]+Zb.subs(n)*b)
print("zip0",float(n[vx]**2/2),"zip1",a**2/2,float(a**2/2),"Zzing",float(Zb.subs(n)*b**2/2))
print("rolling double root:",[ (sp.simplify(so[v1].subs(w,vx/Rb)),sp.simplify(so[w1].subs(w,vx/Rb))) for so in sol])
print("== room 5")
b_,Rc,ph,phd,phdd,gg=sp.symbols('b R_c phi phidot phiddot g')
n_=sp.Matrix([sp.sin(ph),-sp.cos(ph)]); t_=sp.Matrix([sp.cos(ph),sp.sin(ph)])
W=-(Rc-b_)*phd/b_; A=-(Rc-b_)*phdd/b_
rc=(Rc-b_)*n_; vc=(Rc-b_)*phd*t_; ac=(Rc-b_)*(phdd*t_-phd**2*n_)
rP=b_*n_; vP=vc+W*sp.Matrix([-rP[1],rP[0]])
aP=ac+A*sp.Matrix([-rP[1],rP[0]])-W**2*rP
print("vP",sp.simplify(vP.T),"aP",sp.simplify(aP.T))
print("aP x (centre-P):",sp.simplify(aP[0]*(-rP)[1]-aP[1]*(-rP)[0]),"aP.(centre-P)",sp.simplify(aP.dot(-rP)))
r=-rP; tau=r[0]*(-gg)-r[1]*0; print("tau/m about P",sp.simplify(tau))
ZP5=sp.Rational(7,5)*b_**2; sol5=sp.solve(sp.Eq(tau,ZP5*A),phdd)[0]; print("phiddot",sp.simplify(sol5))
T=2*sp.pi*sp.sqrt(7*(Rc-b_)/(5*gg)); nn={Rc:R_(3,10),b_:R_(5,100),gg:R_(98,10)}
print("T",float(T.subs(nn)),"bead",float((2*sp.pi*sp.sqrt((Rc-b_)/gg)).subs(nn)),"sqrt7/5",float(sp.sqrt(R_(7,5))))
KE=sp.simplify(ZP5*W**2/2); print("KE/m",sp.factor(KE))
