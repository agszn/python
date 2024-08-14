# with statement in Python
# In Python, with statement is used in exception handling to make the code cleaner and much more readable. 
# It simplifies the management of common resources like file streams. 
#https://www.geeksforgeeks.org/with-statement-in-python/
# file handling

# 1) without using with statement
file = open('file_path', 'w')
file.write('hello world !')
file.close()

# 2) without using with statement
file = open('file_path', 'w')
try:
	file.write('hello world')
finally:
	file.close()

# using with statement
with open('file_path', 'w') as file:
	file.write('hello world !')


'''unlike the first two implementations, there is no need to call file.close() when using with statement. 
The with statement itself ensures proper acquisition and release of resources. 
An exception during the file.write() call in the first implementation can prevent the file from closing properly 
which may introduce several bugs in the code, i.e. 
many changes in files do not go into effect until the file is properly closed. '''