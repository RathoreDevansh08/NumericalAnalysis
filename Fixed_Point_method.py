r=5

def g(x):
	return 3*x*x - 12*x + 27

def diff(x):
	return 6*x - 12

def Fixed_Point_method(x):
	it=0
	while(it<50):
		it=it+1
		x=r+g(x)-g(r)
		#print(x)
	return x

c=Fixed_Point_method(6)
print(c)
