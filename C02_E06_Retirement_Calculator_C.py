# Hogan Exercises
# Chapter 2, Exercise 6
# Retirement Calculator with initial balance
#
# AUTHOR
#	Ron White
#
# CREATED
#	2019-02-19
#
# LIBRARIES
#	datetime - for current date and time attributes
#
# INPUTS
#	Name string
#	Age integer
#	Retirement age
#	Balance in Retirement Plan
#	Retirement Plan annual growth rate
#
# OUTPUTS
#	Text with name
#	Text with years to retirement
#	Text with retirement year

#
#

import datetime
now = datetime.datetime.now()


lim = 0

a = input("What is your name?  ")
print("Welcome,",a,"to Ron's Magnificent Retirement Calculator")
print()


b = 0
while(b <= lim):
	b = int(input("How many years old are you today?  "))
	if b <= lim:
		print("Come on! I know you've been born already! Try again...")
		b = 0
print("Very good, you are",b,"years old today.")
print()


c = 0
while(c <= b):
	c = int(input("At what age do you want to retire?  "))
	if c <= b:
		print("OK, let's try an age in the future now.")
		c = 0
print()
print("You want to retire at age ",c)
print("Age",c,"is",c-b,"years away.")
print("You are looking to retire in the year",now.year+c-b)
print()


init_bal = int(input("How much do you already have in a retirement account?  "))
rate = int(input("What annual return are you getting on your retirement account?  "))


flag = 0
rate = rate / 100
dep = 10000
if init_bal < dep:
	init_bal = dep


while flag == 0:

	bal = init_bal
	for i in range(1, c-b):
		bal = bal * (1 + rate)
		bal = bal + dep

#	print("Deposit =",dep)
#	print("Balance =",bal)
#	print()

	if bal >= 1050000:
		if dep > 4:
			dep = dep / 2
		else:
			flag = 1
	elif bal <= 950000:
		dep = dep + dep / 2
	else:
		flag = 1

print("Depositing",dep,"every year into an account increasing",rate*100,"% annually will give you about $1 million at retirement.")

print("OK")
