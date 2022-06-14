#using pow function

def compound_interest(principle, rate, time):
	Amount = principle * (pow((1 + rate / 100), time))
	CI = Amount - principle
	print("Compound interest is", CI)

p=float(input("enter principal\n"))
r=float(input("enter rate of interest\n"))
t=float(input("enter time period\n"))
compound_interest(p,r,t)


#using **
def compound_interest(principle, rate, time):
	Amount = principle * (1+(rate/100))**time
	CI = Amount - principle
	print("Compound interest is", CI)

p=float(input("enter principal\n"))
r=float(input("enter rate of interest\n"))
t=float(input("enter time period\n"))
compound_interest(p,r,t)
