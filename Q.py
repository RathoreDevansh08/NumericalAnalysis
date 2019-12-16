import numpy as np

def Gauss_Seidel(x1,x2,x3,x4):
	v = (x2 -2*x3 + 6)/10
	x = (v +x3 -3*x4 +25)/11
	y = (-2*v + x +x4 -11)/10
	z = (-3*x + y + 15)/8
	return v,x,y,z
	
def Iterate(v0,x0,y0,z0):
	rError=1
	while(rError>0.001):
		v1,x1,y1,z1=Gauss_Seidel(v0,x0,y0,z0)
		ev=abs(v1)
		ex=abs(x1)
		ey=abs(y1)
		ez=abs(z1)
		e=max(ey,ev,ex,ez)
		if(e==ev):
			rError=abs(v1-v0)/ev
		elif(e==ex):
			rError=abs(x1-x0)/ex
		elif(e==ey):
			rError=abs(y1-y0)/ey
		else:
			rError=abs(z1-z0)/ez
		v0,x0,y0,z0=v1,x1,y1,z1
	return v0,x0,y0,z0
	
print(Iterate(0,0,0,0))
		
		
