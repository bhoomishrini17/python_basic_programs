# Python program to find Area of a circle
import math
num=int(input("enter the radius of a circle\n"))
def findArea(r):
	return math.pi * (r*r);
print("Area is %.6f" % findArea(num));
