#recursive solution
num=int(input("enter the number to find its factorial\n"))
def factorial(num):
    if(num<0):
        return 0
    if(num==1 or num==0):
        return 1
    else:
        return num*factorial(num-1)
print("factorial of ",num, " is ",factorial(num))

#iterative method
num=int(input("enter the number to find its factorial\n"))
i=num
if(num<0):
    print("factorial of a ",num, " is 0")
if(num==1 or num==0):
    print("factorial of a ",num, " is 1")
else:
    fact=1
    while(i>1):
        fact=fact*i
        i=i-1
print("factorial of ",num," is ",fact)
