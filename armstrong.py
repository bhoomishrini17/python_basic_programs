#Using forloop
num=input("enter a number\n")
k=len(num)
i=0
armstr=0
for i in range(k):
    armstr=int(num[i])**k+armstr
if armstr==int(num):
    print("true,the given number is an armstrong number")
else:
    print("false,the given number is not an armstrong number")

    
    
    
#using whileloop
num=input("enter a number\n")
s=int(num)
k=len(num)
sum1=0
while s!=0:
    r=s%10
    sum1=sum1+r**k
    s=s//10
if int(num)==sum1:
    print("The given number",num,"is armstrong number")
else:
    print("The given number",num,"is not armstrong number")
