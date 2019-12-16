import numpy as np

def eq1(x1,x2,x3):
	return 2*x1 + 3*x2 + 5*x3
def eq2(x1,x2,x3):
	return 3*x1 + 4*x2 + 1*x3
def eq1(x1,x2,x3):
	return 6*x1 + 7*x2 + 2*x3
	
def Jacobi(x1,x2,x3):
	x=(-3/2)*x2-(5/2)*x3+(23/2)
	y=(-3/4)*x1-(1/4)*x3+(14/4)
	z=(-6/2)*x1-(7/2)*(x2)+(26/2)
	return x,y,z
	
def iterate(x0,y0,z0):
	ex=1
	ey=1
	ez=1
	it=0
	while((ex>0.001 or ey>0.001 or ez>0.001) and it<500):
		x1,y1,z1=Jacobi(x0,y0,z0)
		ex=abs(x1-x0)
		ey=abs(y1-y0)
		ez=abs(z1-z0)
		x0,y0,z0=x1,y1,z1
		#print(x0,y0,z0)
		it+=1
		
	print(x0,y0,z0)

iterate(0,0,0)
