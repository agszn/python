# Continue Statement in Python
# Continue is also a loop control statement just like the break statement. 
# continue statement is opposite to that of the break statement, instead of terminating the loop, 
# it forces to execute the next iteration of the loop. 

# As the name suggests the continue statement forces the loop to continue or 
# execute the next iteration. When the continue statement is executed in the loop, 
# the code inside the loop following the continue statement will be skipped and the next iteration of the loop will begin.

# Syntax of Continue Statement
# The continue statement in Python has the following syntax:

# for / while loop:
#     # statement(s)
#     if condition:
#         continue
#     # statement(s)

# Python program to
# demonstrate continue
# statement

# loop from 1 to 10
for i in range(1, 11):

	# If i is equals to 6,
	# continue to next iteration
	# without printing
	if i == 6:
		continue
	else:
		# otherwise print the value
		# of i
		print(i, end = " ")
