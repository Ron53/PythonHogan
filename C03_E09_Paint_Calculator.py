# Hogan Exercises
# Chapter 3, Exercise 9
# Paint Calculator
#
# AUTHOR
#	Ron White
#
# CREATED
#	2019-02-20
#
# INPUTS
#	Room Name string
#	Length integer
#	Width integer
#
# OUTPUTS
#	Ceiling area in sq feet
#	Gallons of paint needed
#
# MODIFICATION HISTORY
#	2019-02-20  Created
#
#


coverage = 350
lim = 0

room = input("\n\nWhat room is are we planning on painting?  ")
print(f"We are measuring the area of {room}\n")


room_length = 0
ask_length = f"How long is {room}?  "
bad_distance = f"Come on, the wall is longer than that! Let's try again.\n"
while(room_length <= lim):
	room_length = int(input(ask_length))
	if room_length <= lim:
		print(bad_distance)
		room_length = 0
print(f"The length of {room} is {room_length} feet\n")


room_width = 0
ask_width = f"How wide is {room}?  "
while(room_width <= lim):
	room_width = int(input(ask_width))
	if room_width <= lim:
		print(bad_distance)
		room_width = 0
print(f"The width of {room} is {room_width} feet\n")

area_ft = room_length * room_width
gallons_needed = area_ft / coverage


output_area_ft = f"The area of {room} ceiling is {area_ft} sq feet."
paint_needed = f"You need {gallons_needed} gallons of paint to cover the {room} ceiling.\n"
print(output_area_ft)
print(paint_needed)


print("\n \n OK")
