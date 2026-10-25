"""Checks for three MIT 8.022 (Fall 2004) Assignment 6 problems, worked with the turn. Claude.

Problem 5: field at the center of a regular n-gon of current, R from center to each side.
Problem 6: vector potential of an infinite solenoid.
Problem 8: two moving line charges; electric and magnetic force per length.
"""

import sympy as s

turn = 2*s.pi
mu, eps, I, R, r, n_wind, c = s.symbols('mu_0 epsilon_0 I R r n c', positive=True)
n = s.symbols('n', integer=True, positive=True)

# 5. Each side: a straight wire R away whose ends lean flip/n off the perpendicular.
#    The usual finite-wire field: mu I / (4 pi R) * (sin a + sin b).
side = mu*I/(4*s.pi*R) * 2*s.sin(s.pi/n)
center = n*side
# Way through: the corners' directions mark an inscribed n-gon on a unit circle,
# and the field is mu I / (2 turn R) times that polygon's perimeter.
perimeter = 2*n*s.sin(turn/(2*n))
assert s.simplify(center - mu*I*perimeter/(2*turn*R)) == 0
assert s.simplify(center.subs(n, 4) - s.sqrt(2)*mu*I/(s.pi*R)) == 0       # the square
x = s.symbols('x', positive=True)                                        # n as a real number, for the limits
assert s.limit(perimeter.subs(n, x), x, s.oo) == turn                    # Archimedes
assert s.simplify(s.limit(center.subs(n, x), x, s.oo) - mu*I/(2*R)) == 0 # the circle
print('5: square / circle =', s.N((center.subs(n, 4)/(mu*I/(2*R))), 3))

# 6. Infinite solenoid: B = mu n I inside. A runs around; its circulation is the linkage.
B = mu*n_wind*I
A_in = (B*turn*r**2/2) / (turn*r)            # a turn of triangle slivers, spread over a turn of circumference
A_out = (B*turn*R**2/2) / (turn*r)
assert s.simplify(A_in - B*r/2) == 0 and s.simplify(A_out - B*R**2/(2*r)) == 0
# check against curl: B_z = (1/r) d(r A)/dr
assert s.simplify(s.diff(r*A_in, r)/r - B) == 0 and s.simplify(s.diff(r*A_out, r)/r) == 0
print('6: A inside =', A_in, '; outside =', A_out)

# 8. Two lines of charge lam0 (rest), d apart, moving at v. Rest force per length:
lam0, d, v = s.symbols('lambda_0 d v', positive=True)
rest = lam0**2/(eps*turn*d)                   # the field spreads over a turn of circumference
gamma = 1/s.sqrt(1 - v**2/c**2)
electric = (gamma*lam0)**2/(eps*turn*d)       # lab: charge bunched by the stretch
current = gamma*lam0*v
magnetic = current*mu*current/(turn*d)        # current of the other's field, pulling together
total = (electric - magnetic.subs(mu, 1/(eps*c**2))).simplify()
assert s.simplify(total - rest) == 0
# Bondi's shift s: stretch = (s + 1/s)/2, and gamma v/c = half the gap = (s - 1/s)/2
sh = s.symbols('s', positive=True)
stretch, half_gap = (sh + 1/sh)/2, (sh - 1/sh)/2
assert s.simplify(stretch**2 - half_gap**2) == 1
print('8: at shift 2: electric', stretch.subs(sh, 2)**2, 'of rest; magnetic', half_gap.subs(sh, 2)**2, '; total 1')
