# Hogan Exercises
# Chapter 3, Exercise 11
# Currency Conversion
#
# OBJECTIVES
#	Currency
#
# AUTHOR
#	Ron White
#
# CREATED
#	2019-02-27
#
# INPUTS
#	From currency string
#	To currency string
#	Exchange rate:  1 from currency = x to currency
#	From currency amount
#
# OUTPUTS
#	From currency, exchange rate, to currency
#	From amount, exchange rate, to amount
#
# LIBRARIES
#	Math
#
#
# MODIFICATION HISTORY
#	2019-02-27  Created
#
#

import math


input_flag = True

from_currency = input( f"What currency do you have?  " )
to_currency = input( f"What currency do you want?  " )

exch_input = input( f"What is the exchange rate? Eg.: 1 { from_currency } = how many { to_currency }?  ")
try:
	exch_rate = float( exch_input )

except ValueError:
	print( f"Sorry, you need a numeric exchange rate, instead of a string. \n" )


cash_input = input( f"How much do you want to exchange?  ")
try:
	cash_exchange = float( cash_input )

except ValueError:
	print( f"Sorry, you need a numeric amount to exchange, instead of a string. \n" )


new_cash = round( cash_exchange * exch_rate , 2 )

print( f"\n\nExchanging { cash_input } from { from_currency } to { to_currency } gives you { new_cash } \n\nTHANK YOU FOR SHOPPING WITH US TODAY! \n\n\n")






print("\n \n OK")
