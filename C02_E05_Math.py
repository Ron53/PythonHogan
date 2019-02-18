# Hogan Exercises
# Chapter 2, Exercise 5
# Simple Math
#
# AUTHOR
#	Ron White
#
# CREATED
#	2019-02-18
#
# INPUTS
#	Two numbers
#
# OUTPUTS
#	Sum
#	Difference
#	Product
#	Quotient
#
#

lim = 0

a = 0
while(a <= lim):
	a = int(input("Enter your first integer  "))
	if a <= lim:
		print("Your number needs to be greater than",lim)
		a = 0

b = 0
while(b <= lim):
	b = int(input("Enter your second integer  "))
	if b <= lim:
		print("Your number needs to be greater than",lim)
		b = 0


print(a,"+",b,"=",a+b)
print(a,"-",b,"=",a-b)
print(a,"*",b,"=",a*b)
print(a,"/",b,"=",a/b)

