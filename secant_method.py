import numpy as np

def func(x):
	return np.power(x,3)+4*np.power(x,2)-10

def diff(x, x2):
	return (func(x)-func(x2))/(x-x2)

def Secant(x):
	error=1
	itr=0
	x0=x+1
	while(error>0.001 and itr<1000):
		if(diff(x,x0)!=0):
			x1=x-func(x)/diff(x,x0)
		elif(abs(func(x)-0)<0.0001):
			print("derivative became zero")
			break
		else:
			print("Differentiation in intermediate step=0")
			print("No further iteration possible")
			break
		itr+=1
		error=abs(x1-x)
		x=x1
	return x

c=Secant(5)
print(c)
print(func(c))
