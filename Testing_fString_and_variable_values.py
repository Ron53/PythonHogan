# Testing fString variable values and variable value updates
#

i = -100
message1 = f"The value of 'i' is {i}. This was defined outside the loop"
for i in range (0,5):
	message2 = f"The value of 'i' is {i}. This was defined inside the loop"

	print(message1)
	print(message2,"\n")

print("The loop has finished running")
print(message1)
print(message2)

