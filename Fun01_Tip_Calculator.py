#  Tip Calculator
#
#  INPUT
#      Check
#      Tip Rate
#
#  OUTPUT
#      Tip
#      Total Paid

#  check for valid input
valid_input = 0
while valid_input < 1:
	check_amt = float(input("Enter check amount:  "))
	if( check_amt <= 0):
		print("Check amount must be greater than zero")
		valid_input = 0
	else:
		valid_input = 1

valid_input = 0
while valid_input < 1:
	tip_rate = float(input("Enter tip rate:  ")) / 100
	if(tip_rate < .10):
		print("Are you sure you want to be that cheap?")
	elif(tip_rate < .20):
		print("Must be pretty poor service")
		valid_input = 1
	elif(tip_rate > 1.5):
		print()
		print("But think of the children!")
		print()
		valid_input = 1
	elif(tip_rate > .4):
		print("Must be really good service!")
		valid_input = 1
	else:
		valid_input = 1



#print('Check:  ',check_amt)
#print('Tip Rate:  ',tip_rate,'%')
tip_amt = round(check_amt * tip_rate,2)
total_paid = check_amt + tip_amt

print('Tip:  ',tip_amt)
print('Total check:  ',total_paid)