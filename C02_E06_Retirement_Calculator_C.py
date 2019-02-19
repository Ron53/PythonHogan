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
# MODIFICATION HISTORY
#	2019-02-18  Change variable names to something more meaningful [RW]
#	2019-02-18  Changed "flag" to boolean
#
#

import datetime
now = datetime.datetime.now()


lim = 0

user_name = input("What is your name?  ")
welcome =f"Welcome, {user_name}, to Ron's Magnificent Retirememnt Calculator!\n"
print(welcome)


user_age = 0
ask_age = f"How many years old are you today?  "
bad_age = f"Come on! I know you've been born already! Try again..."
give_age = f"Very good, you are {user_age} years old today.\n"
while(user_age   <= lim):
	user_age = int(input(ask_age))
	if user_age   <= lim:
		print(bad_age)
		user_age = 0
print(give_age)


ret_age  = 0
ask_ret_age = f"At what age do you want to retire?  "
bad_ret_age = f"OK, let's try an age in the future now.\n"

print("#1",ret_age, user_age)
while(ret_age  <= user_age):
	ret_age  = int(input(ask_ret_age))
	print("#2",ret_age, user_age)
	if ret_age  <= user_age  :
		print(bad_ret_age)
		ret_age  = 0

give_ret_age = f"You want to retire at age {ret_age}"
give_ret_yrs_away = f"Age {ret_age} is {ret_age -user_age} years away."
give_ret_year = f"You are looking to retire in the year {now.year+ret_age -user_age}\n"  
print(give_ret_age)
print(give_ret_yrs_away)
print(give_ret_year)


init_bal = int(input("How much do you already have in a retirement account?  "))
rate = int(input("What annual return are you getting on your retirement account? \n   (7 is a reasonable return to expect from the stock market)  "))


flag = True
rate = rate / 100
dep = 10000
if init_bal < dep:
	init_bal = dep


while flag:

	bal = init_bal
	for i in range(1, ret_age -user_age  ):
		bal = bal * (1 + rate)
		bal = bal + dep

#	print("Deposit =",dep)
#	print("Balance =",bal)
#	print()

	if bal >= 1050000:
		if dep > 4:
			dep = dep / 2
		else:
			flag = False
	elif bal <= 950000:
		dep = dep + dep / 2
	else:
		flag = False

message = f"\nDepositing ${dep} every year into an account increasing {rate*100: 0.2}% annually \n   will give you about $1 million at retirement."
print(message)

print("\n \n OK")
