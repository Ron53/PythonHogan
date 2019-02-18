# Chapter 2, Exercise 2
# Counting the Number of Characters
#
# INPUT
#	Random string of characters by user
#
# OUTPUT
#	Sentence giving the input string, and
#	the number of characters in the input string
#
# IMPORTS
#	Tkinter - GUI library
#
#

import Tkinter

top = tkinter.Tk()

# Wigits code

top.mainloop(

	flag = 1
	while flag == 1:
		a = input("What is the input string? ")
		if len(a) > 0:
			flag = 0
		else:
			print("Must input a non-null string")

	print(a," has",len(a),"characters.")

)

