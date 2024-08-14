# The other way of writing except statement, is shown below and in this way, 
# it only accepts exceptions that you’re meant to catch or you can check which error is occurring.

# code
def divide(x, y):
	try:
		# Floor Division : Gives only Fractional Part as Answer
		result = x // y
		print("Yeah ! Your answer is :", result)
	except Exception as e:
	# By this way we can know about the type of error occurring
		print("The error is: ",e)

		
divide(3, "GFG")
divide(3,0)

# Output:

# The error is:  unsupported operand type(s) for //: 'int' and 'str'
# The error is:  integer division or modulo by zero