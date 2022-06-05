def simple_interest(p,t,r):
	print('The principal is', p)
	print('The time period is', t)
	print('The rate of interest is',r)
	
	si = (p * t * r)/100
	
	print('The Simple Interest is', si)

p=float(input("enter the principal\n"))
t=float(input("enter the time period\n"))
r=float(input("enter the rate of interest\n"))
simple_interest(p,t,r)