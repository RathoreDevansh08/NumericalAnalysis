from sympy.core.symbol import symbols
from sympy.solvers.solveset import nonlinsolve

x, y, z = symbols('x, y, z', real=True)

c=nonlinsolve([x*y - 1, 4*x**2 + y**2 - 5], [x, y])

print(c)
