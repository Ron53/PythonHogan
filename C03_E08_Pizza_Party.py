# Hogan Exercises
# Chapter 3, Exercise 8
# Pizza!
#
# AUTHOR
#	Ron White
#
# CREATED
#	2019-02-20
#
# INPUTS
#	No people
#	No pizzas
#	How many slices per pizz
#
# OUTPUTS
#	No of slices per person
#	No of slices left over
#
# MODIFICATION HISTORY
#	2019-02-20  Created
#
#


lim = 1

people = 0
ans_people = 0
ask_people = f"How many people?  "
bad_people = f"Come on, there are more than that! Let's try again.\n"

#print(f"people {people}; ans_people {ans_people} \n")

while(ans_people <= lim):
	ans_people = int(input(ask_people))
#	print(f"people {people}, ans_people {ans_people}")
	if people == 1:
		if ans_people == 1:
			print("OK, pizza for one it is.\n")
			ans_people = 100
		elif ans_people > lim:
			people = ans_people
			print(f"Good! {people} people sounds like a good time.\n")
		else:
			people = ans_people
			print(bad_people)
	elif ans_people <= lim:
		people = ans_people
		print(bad_people)
		ans_people = 0
	else:
		people = ans_people
		print(f"Good! {people} people sounds like a good time.\n")


lim = 0
pizzas = 0
ask_pizzas = f"How many pizzas?  "
bad_pizzas = f"Not very hungary, are we? Try again... \n"
while(pizzas <= lim):
	pizzas = int(input(ask_pizzas))
	if pizzas <= lim:
		print(bad_pizzas)
		pizzas = 0
print(f"OK, {pizzas} pizzas it is.\n")


slices = 0
ask_slices = f"How many slices?  "
bad_slices = f"A whole pizza with no slices? Try again... \n"
while(slices <= lim):
	slices = int(input(ask_slices))
	if slices <= lim:
		print(bad_slices)
		slices = 0
print(f"OK, {pizzas} pizzas, each with {slices} slices.\n")

print(f"{people} people; {pizzas} pizzas; {slices} slices\n\n")

if pizzas < 2:
	pizza_order = f"That's 1 pizza"
else:
	pizza_order = f"That's {pizzas} pizzas"

if slices < 2:
	slices_order = f"with 1 slice - well, a whole pizza,"
else:
	slices_order = f"with {slices} slices per pizza,"

if people < 2:
	people_order = f"for just you."
else:
	people_order = f"for {people} people." 

print(pizza_order, slices_order, people_order)

each = int(pizzas * slices / people)
left = (pizzas * slices) % people

if each == 1:
	slices_each = f"That's 1 slice for everyone,"
else:
	slices_each = f"That's {each} slices for everyone,"

if left == 1:
	left_over = f"with 1 slice left over.\n"
else:
	left_over = f"with {left} slices left over.\n"

print(slices_each, left_over)



print("\n \n OK")
