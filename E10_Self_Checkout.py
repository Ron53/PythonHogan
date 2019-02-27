# Hogan Exercises
# Chapter 3, Exercise 10
# Self-Checkout
#
# OBJECTIVES
#	Arrays
#	Currency
#
# AUTHOR
#	Ron White
#
# CREATED
#	2019-02-26
#
# INPUTS
#	Item name string
#	Item price
#	Item quantity
#
# OUTPUTS
#	Item name, price, quantity, total cost
#	Total items cost
#	Calculate tax
#	Cost with tax
#
# LIBRARIES
#	Math
#
#
# MODIFICATION HISTORY
#	2019-02-26  Created
#
#

import math

item = []
price = []
qty = []
cost = []

sales_tax = 0.055

input_flag = True
counter = 0
item.append( input( f"What is item {counter}?  " ) )


while( input_flag ):
	input_no = input( f"How much does {item [ counter ]} cost?  " )
	input_price = int( input_no )
	if input_price <= 0:
		print( f"I think you need a better price, using integers. \n")
	else:
		price.append( input_price )
		input_no = input( f"How many items do you have?  " )
		input_qty = int( input_no )
		if input_qty <= 0:
			print( f"You should have at least 1 item.  \n")
		else:
			qty.append( input_qty )
			cost.append( price[ counter ] * qty[ counter ] )
			print( f"{item[ counter ]}; ${price[ counter ] / 100}; qty {qty[ counter]}; cost { cost[ counter ] } \n\n" )
			counter = counter + 1
			input_item = input( f"What is item {counter}?  " )
			if len( input_item ) > 0 :
				item.append( input_item )
			else:
				input_flag = False


#print( f"\n\n\nNo of items = {counter}, { len( item) }, { len( cost ) }, { len( qty) } " )
#print( counter )
#print( item )
#print( price )
#print( qty )
#print( cost )

cntr_2 = 0
total_cost = 0
print( f"\n\n" )

while( cntr_2 < counter ):
	total_cost = total_cost + cost[ cntr_2 ]
	print( f"{ item[ cntr_2 ] } - { qty[ cntr_2 ] } at ${ price[ cntr_2 ]/100 } is ${ cost[ cntr_2 ] /100 }, your balance is ${ total_cost / 100 } " )
	cntr_2 = cntr_2 + 1

tax = round( sales_tax * total_cost / 100 , 2 )
print( f"\n  Your subtotal is ${ total_cost / 100 }\n  Sales tax is ${ tax }\n\n  Your total is ${ (total_cost / 100) + tax }\n\nTHANK YOU FOR SHOPPING WITH US TODAY! \n\n\n\n\n")






print("\n \n OK")
