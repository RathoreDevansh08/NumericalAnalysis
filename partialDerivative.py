import numpy as np
from sympy import Symbol, Derivative

x= Symbol('x')
y= Symbol('y')

func= x**2 * y**3 + 12*y**4
pd= Derivative(func, x)

c=pd.doit()
print(c)
