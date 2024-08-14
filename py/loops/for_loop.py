# # For Loops in Python
# # Python For loop is used for sequential traversal i.e. 
# # it is used for iterating over an iterable like String, Tuple, List, Set, or Dictionary. 

# For Loops Syntax
# for var in iterable:
#     # statements

# Python program to illustrate
# Iterating over a list
l = ["geeks", "for", "geeks"]

for i in l:
	print(i)

#Iterating over tuple
t = ((1, 2), (3, 4), (5, 6))
for a in t:
	print(a)
	# print(b)

# Iterating over dictionary
print("Dictionary Iteration")

d = dict()

d['xyz'] = 123
d['abc'] = 345
for i in d:
	print("% s % d" % (i, d[i]))

# Iterating over a String
print("String Iteration")

s = "Geeks"
for i in s:
	print(i)

# python For Loop with a step size
# This code uses a for loop in conjunction with the range() function 
# to generate a sequence of numbers starting from 0, up to (but not including) 10, and with a step size of 2. 

# For each number in the sequence, the loop prints its value using the print() function. 
# The output will show the numbers 0, 2, 4, 6, and 8.
for i in range(0, 10, 2):
	print(i)


# nested for
for i in range(1, 4):
	for j in range(1, 4):
		print(i, j)


# Python For Loop with Zip()
# This code uses the zip() function to iterate over two lists (fruits and colors) in parallel. 
# The for loop assigns the corresponding elements of both lists to the variables fruit and color in each iteration. 
fruits = ["apple", "banana", "cherry"]
colors = ["red", "yellow", "green"]
for fruit, color in zip(fruits, colors):
	print(fruit, "is", color)


#for loop with statement
for letter in 'geeksforgeeks':

	# break the loop as soon it sees 'e'
	# or 's'
	if letter == 'e' or letter == 's':
		break

print('Current Letter :', letter)


# Python program to demonstrate
# for-else loop

for i in range(1, 4):
	print(i)
else: # Executed because no break in for
	print("No Break\n")
