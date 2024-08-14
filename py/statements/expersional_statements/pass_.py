# Pass Statement in Python
# As the name suggests pass statement simply does nothing. 
# The pass statement in Python is used when a statement is required syntactically but you do not want any command or 
# code to execute. It is like a null operation, as nothing will happen if it is executed. 
# Pass statements can also be used for writing empty loops. Pass is also used for empty control statements, 
# functions, and classes.

# Syntax of Pass Statement
# The pass statement in Python has the following syntax:

# function/ condition / loop:
#    pass

# Python program to demonstrate
# pass statement

s = "geeks"

# Empty loop
for i in s:
	# No error will be raised
	pass

# Empty function
def fun():
	pass

# No error will be raised
fun()

# Pass statement
for i in s:
	if i == 'k':
		print('Pass executed')
		pass
	print(i)
