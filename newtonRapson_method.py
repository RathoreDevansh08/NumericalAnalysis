import numpy as np

def func(x):
	return np.power(x,3)+4*np.power(x,2)-10

def diff(x):
	return 3*np.power(x,2)+8*(x)

def NewtonRapson(x):
	error=1
	itr=0
	while(error>0.001 and itr<1000):
		if(diff(x)!=0):
			x1=x-func(x)/diff(x)
		elif(abs(func(x)-0)<0.0001):
			break
		else:
			print("Differentiation in intermediate step=0")
			print("No further iteration possible")
			break
		itr+=1
		error=abs(x1-x)
		x=x1
	return x

c=NewtonRapson(5)
print(c)
print(func(c))
			
			
