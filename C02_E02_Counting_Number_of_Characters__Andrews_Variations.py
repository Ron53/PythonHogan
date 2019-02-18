# Chapter 2, Exercise 2 - Andrew's modifiations
# Counting the Number of Characters & other info
#
# INPUT
#	Prompts for user name
#	Prompts for birthdate using m/d/y format
#
# OUTPUT
#	Sentence giving the input string, and
#	the number of characters in the input string
#	Returns the user's birthday
#	Tells user when they can reach full retirement age
#
# IMPORTS
#	Tkinter - GUI library
#
#

import tkinter

top = tkinter.Tk()

# Wigits code

top.mainloop(


#	Ask for and input user's name
#		Basic edit for non-null string
#
	flag = 1
	while flag == 1:
		a = input("What is your name? ")
		if len(a) > 0:
			flag = 0
		else:
			print("Must input a non-null string")

	print("Hello",a," it is nice to meet you.")
	print("Your name -",a,"- has",len(a),"letters.")


#	Ask for and input user's birthday
#		Basic edit for non-null string
#		Edit for minimum useable string length
#
	flag = 1
	while flag == 1:
		b = input("What is your birthday? (Use m/d/y format) ")
		if len(b) == 0:
			print("Must input a non-null string")
		elif len(b) < 5:
			print("I need an actual date value. ",b,"is not sufficient.")
		else:
			flag = 0


#	Edit birthday for valid data
#
	flag = 1


#	Check for full Social Security age
#
	year