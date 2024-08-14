# Python While Loop is used to execute a block of statements repeatedly until a given condition is satisfied. 
# And when the condition becomes false, the line immediately after the loop in the program is executed.

# Syntax: 

# while expression:
#     statement(s)

# While loop falls under the category of indefinite iteration. 
# Indefinite iteration means that the number of times the loop is executed isn’t specified explicitly in advance. 

# Statements represent all the statements indented by the same number of character spaces after a programming 
# construct are considered to be part of a single block of code. Python uses indentation as its method of grouping statements. 

# When a while loop is executed, expr is first evaluated in a Boolean context and if it is true, the loop body is executed.
# Then the expr is checked again, if it is still true then the body is executed again and this continues until the expression 
# becomes false.

# Python program to illustrate
# while loop
count = 0
while (count < 3):
	count = count + 1
	print("Hello Geek")

# checks if list still
# contains any element
a = [1, 2, 3, 4]

while a:
	print(a.pop())

# Python program to illustrate
# Single statement while block
count = 0
while (count < 5): count += 1; print("Hello Geek")

#continue while
# Prints all letters except 'e' and 's'
i = 0
a = 'geeksforgeeks'

while i < len(a):
	if a[i] == 'e' or a[i] == 's':
		i += 1
		continue
		
	print('Current Letter :', a[i])
	i += 1

#break while
# break the loop as soon it sees 'e'
# or 's'
i = 0
a = 'geeksforgeeks'

while i < len(a):
	if a[i] == 'e' or a[i] == 's':
		i += 1
		break
		
	print('Current Letter :', a[i])
	i += 1

#pass while
# An empty loop
a = 'geeksforgeeks'
i = 0

while i < len(a):
	i += 1
	pass

print('Value of i :', i)

# Python program to demonstrate
# while-else loop

i = 0
while i < 4:
	i += 1
	print(i)
else: # Executed because no break in for
	print("No Break\n")

i = 0
while i < 4:
	i += 1
	print(i)
	break
else: # Not executed as there is a break
	print("No Break")

# Sentinel Controlled Statement
# In this, we don’t use any counter variable because we don’t know how many times the loop will execute. 
# Here user decides that how many times he wants to execute the loop. For this, we use a sentinel value. 
# A sentinel value is a value that is used to terminate a loop whenever a user enters it, generally, the sentinel value is -1.

# Example: Python while loop with user input
a = int(input('Enter a number (-1 to quit): '))

while a != -1:
	a = int(input('Enter a number (-1 to quit): '))

# While loop on Boolean values:
# One common use of boolean values in while loops is to create an infinite loop 
# that can only be exited based on some condition within the loop. For example:
# Initialize a counter
count = 0

# Loop infinitely
while True:
	# Increment the counter
	count += 1
	print(f"Count is {count}")

	# Check if the counter has reached a certain value
	if count == 10:
		# If so, exit the loop
		break

# This will be executed after the loop exits
print("The loop has ended.")
