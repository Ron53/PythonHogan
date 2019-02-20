# Hogan Exercises
# Chapter 3, Exercise 7
# Room Dimensions
#
# AUTHOR
#	Ron White
#
# CREATED
#	2019-02-19
#
# INPUTS
#	Room Name string
#	Length integer
#	Eidth integer
#
# OUTPUTS
#	Floor area in sq feet
#	Floor area in sq meters
#
# MODIFICATION HISTORY
#	2019-02-18  Created
#
#


sq_ft_to_sq_m_conv = .09290304
lim = 0

room = input("What room is are we figuring the area for?  ")
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
area_m = sq_ft_to_sq_m_conv * area_ft

output_area_ft = f"The area of {room} is {area_ft} sq feet."
output_area_m = f"The area of {room} is {area_m} sq meters./2n"
print(output_area_ft)
print(output_area_m)
print("\n \n OK")
