
#maximum of two numbers 
num1=float(input("enter two numbers\n"))
num2=float(input())
if(num1>num2):
    print(str(num1)+" is bigger")
else:
    print(str(num2)+" is bigger")
    
#using max function
num1=float(input("enter two numbers\n"))
num2=float(input())
print(str(max(num1,num2))+" is bigger")

#using ternary operator
num1=float(input("enter two numbers\n"))
num2=float(input())
print(num1 if(num1>num2) else num2)
