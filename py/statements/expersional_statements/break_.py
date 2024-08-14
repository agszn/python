# Break Statement in Python
# The break statement in Python is used to terminate the loop or statement in which it is present. 
# After that, the control will pass to the statements that are present after the break statement, if available. 
# If the break statement is present in the nested loop, then it terminates only those loops which contain the break statement.


# Syntax of Break Statement
# The break statement in Python has the following syntax:

# for / while loop:
#     # statement(s)
#     if condition:
#         break
#     # statement(s)
# # loop end

# Python program to demonstrate
# break statement

s = 'python_programming'
# Using for loop
for letter in s:

	print(letter)
	# break the loop as soon it sees 'e'
	# or 's'
	if letter == 'h' or letter == 'o':
		break

print("Out of for loop")
print()

i = 0

# Using while loop
while True:
	print(s[i])

	# break the loop as soon it sees 'e'
	# or 's'
	if s[i] == 'e' or s[i] == 's':
		break
	i += 1

print("Out of while loop")

#nested for loop break statements
# Python program to demonstrate
# break statement with nested
# for loop

# first for loop
for i in range(1, 5):
	
	# second for loop
	for j in range(2, 6):
		
		# break the loop if
		# j is divisible by i
		if j%i == 0:
			break
			
		print(i, " ", j)
