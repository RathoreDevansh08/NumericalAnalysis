import numpy as np

def f(x,y):
	return x**2-y**2+7
def g(x,y):
	return x-x*y+9
def fx(x,y):
	return 2*x
def fy(x,y):
	return (-2)*y
def gx(x,y):
	return 1-y
def gy(x,y):
	return (-1)*x
	
def Solver(x0,y0):
	ex=1
	ey=1
	it=0
	while((ex>0.01 or ey>0.01) and it<100):
		nx=(-f(x0,y0)*gy(x0,y0)+g(x0,y0)*fy(x0,y0))
		dx=(fx(x0,y0)*gy(x0,y0)-gx(x0,y0)*fy(x0,y0))
		ny=(-g(x0,y0)*fx(x0,y0)+f(x0,y0)*gx(x0,y0))
		dy=(fx(x0,y0)*gy(x0,y0)-fy(x0,y0)*gx(x0,y0))
		x1=x0+(nx)/(dx)
		y1=y0+(ny)/(dy)
		ex=abs(x0-x1)
		ey=abs(y0-y1)
		x0,y0=x1,y1
	return x0,y0

x0,y0=Solver(4,5)
print(x0,y0)
