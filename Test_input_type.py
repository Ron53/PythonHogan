number = input ("Enter number   ")
number_two = input("Enter another number   ")
print("Printing type of input value")
print ("type of number ", type(number))
print ("type of number_two ", type(number_two ))
print ()


try:
	val = int( number )
	print("Yes input string is an Integer.")
	print("Input number value is: ", val)
except ValueError:
	print("That's not an int!")
	try:
		val = float( number )
		print("Yes input string is a Float.")
		print("Input number value is: ", val)
	except ValueError:
		print("That's not an int or a float!")
		print("No.. input string is not an Integer. It's a string")
   

print()
print()

try:
	val = int( number_two )
	print("Yes input string 2 is an Integer.")
	print("Input number value is: ", val)
except ValueError:
	print("That's not an int!")
	try:
		val = float( number_two )
		print("Yes input string 2 is a Float.")
		print("Input number value is: ", val)
	except ValueError:
		print("That's not an int or a float!")
		print("No.. input string 2 is not an Integer. It's a string")
   


print( f"OK" )