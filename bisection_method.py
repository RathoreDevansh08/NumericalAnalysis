import numpy as np
import matplotlib.pyplot as plt

def func(x):
	return np.power(x,3)+4*np.power(x,2)-10
	
def bisection(a,b):
	error=1
	while(error>0.0001):
		s=(a+b)/2
		#print(s)
		fs=func(s)
		if(fs*(func(a))>0):
			a=s
		elif(fs*(func(b))>0):
			b=s
		else:
			return s
		error=abs(b-a)
	return s

c=bisection(1,2)
print(c)
print(func(c))
