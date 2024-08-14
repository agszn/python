#1: Find the length of the list and simply swap the first element with (n-1)th element.
# Examples: 

# Input : [12, 35, 9, 56, 24]
# Output : [24, 35, 9, 56, 12]

# Input : [1, 2, 3]
# Output : [3, 2, 1]

# Python program to swap first
# and last element of a list

# Swap function
def swapList(newList):
	size = len(newList)
	
	# Swapping
	temp = newList[0]
	newList[0] = newList[size - 1]
	newList[size - 1] = temp
	
	return newList
	
# Driver code
newList = [12, 35, 9, 56, 24]

print(swapList(newList))

#############################################################

#2: The last element of the list can be referred as list[-1]. Therefore, we can simply swap list[0] with list[-1].
# Python3 program to swap first
# and last element of a list

# Swap function
def swapList(newList):
	
	newList[0], newList[-1] = newList[-1], newList[0]

	return newList
	
# Driver code
newList = [12, 35, 9, 56, 24]
print(swapList(newList))


##############################################################


#3: Given a list in Python and a number x, count the number of occurrences of x in the given list.

# Examples: 

# Input: lst = [15, 6, 7, 10, 12, 20, 10, 28, 10], x = 10
# Output: 3 
# Explanation: 10 appears three times in given list.

# Input: lst = [8, 6, 8, 10, 8, 20, 10, 8, 8], x = 16
# Output: 0
# Explanation: 16 appears zero times in given list.

# Python code to count the number of occurrences
def countX(lst, x):
	count = 0
	for ele in lst:
		if (ele == x):
			count = count + 1
	return count


# Driver Code
lst = [8, 6, 8, 10, 8, 20, 10, 8, 8]
x = 8
print('{} has occurred {} times'.format(x, countX(lst, x)))

#############################################################
#4: Python program to print even numbers in a list
# Example: 

# Input: list1 = [2, 7, 5, 64, 14]
# Output: [2, 64, 14]
# Input: list2 = [12, 14, 95, 3]
# Output: [12, 14]

# Python program to print Even Numbers in a List

# list of numbers
list1 = [10, 21, 4, 45, 66, 93]

# iterating each number in list
for num in list1:

	# checking condition
	if num % 2 == 0:
		print(num, end=" ")

#############################################################
# The task is to perform the operation of removing all the occurrences of a given item/element present in a list. 

# Examples:

# Input : 1 1 2 3 4 5 1 2 1 
# Output : 2 3 4 5 2 
# Explanation : The input list is [1, 1, 2, 3, 4, 5, 1, 2] and the item to be removed is 1. After removing the item, the output list is [2, 3, 4, 5, 2] 

# Input : 5 6 7 8 9 10 7 
# Output : 5 6 8 9 10

def fun1():
	x=[i for i in test_list if i!=ele]
	print(x)

#using pop
def fun2(listvalue,itemvalue):
	for i in test_list:
		if i==listvalue:
			listvalue[i].pop()

#using append
def fun3(listvalue,itemvalue):
	for i in test_list:
		if i==listvalue:
			listvalue[i].pop()
	
final = []
test_list = [1, 3, 4, 6, 5, 1]
ele=1

fun2(test_list,ele)

