import numpy as np
import matplotlib.pyplot as plt


def func(x):
	return np.sin(x)
	
def diff(x):
	return np.cos(x)

def taylor(x,x0,epsilon):
	f=func(x0)+(x-x0)*(diff(x0))+((x-x0)**2)*(-0.5)*(func(x));
	return f
	
print(taylor(4,3.14,0.86))
print(np.sin(4))	
print(np.sin(3.14))
