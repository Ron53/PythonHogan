# Greatest Common Divisor (GCD) program
#
# The GCD finds the largest number that goes evenly into
# both of the input numbers
#
# INPUT
# 	Integer A
# 	Integer B
#
# OUTPUT
#	Integer C
#

a = 0
while(a < 2):
	a = int(input("Enter your first integer  "))
	if a < 2:
		print("Your number needs to be greater than 1")
		a = 0

b = 0
while(b < 2):
	b = int(input("Enter your second integer  "))
	if b < 2:
		print("Your number needs to be greater than 1")
		b = 0


# Check to see whether the smaller number is the GCD
if a < b:
	div = a
else:
	div = b

if 0 == a % div:
	if 0 == b % div:
		gcd = div
	else:
		gcd = 0
else:
	gcd = 0


# Begin divisor iteration
if 0 == div % 2:
	div = div - 1

while gcd == 0:
	if 0 == a % div:
		if 0 == b % div:
			gcd = div

	div = div - 1
#	if div == 1:
#		div = 2



# Print result - the GCD
print()
print("The Greatest Common Divisor of ",a," and ",b," is ",gcd)
print()
print(a," divided by ",gcd," is ",int(a / gcd))
print(b," divided by ",gcd," is ",int(b / gcd))




# setup check
#print("a= ",a)
#print("b= ",b)
#print("div: ",div)
#print("gcd: ",gcd)


