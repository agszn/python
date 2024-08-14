'''Python Operators
Operators are used to perform operations on variables and values.

In the example below, we use the + operator to add together two values:

Python divides the operators in the following groups:

Arithmetic operators
Assignment operators
Comparison operators
Logical operators
Identity operators
Membership operators
Bitwise operators

== and =
'''
# Python Arithmetic Operators
# Arithmetic operators are used with numeric values to perform common mathematical operations:

# +	Addition	x + y	
# -	Subtraction	x - y	
# *	Multiplication	x * y	
# /	Division	x / y	
# %	Modulus	x % y	
# **	Exponentiation	x ** y	
# //	Floor division	x // y	

x = 5
y = 3

print(x + y)

# Python Assignment Operators
# Assignment operators are used to assign values to variables:

# =	x = 5	x = 5	
# +=	x += 3	x = x + 3	
# -=	x -= 3	x = x - 3	
# *=	x *= 3	x = x * 3	
# /=	x /= 3	x = x / 3	
# %=	x %= 3	x = x % 3	
# **=	x **= 3	x = x ** 3	
# &=	x &= 3	x = x & 3	
# |=	x |= 3	x = x | 3	
# ^=	x ^= 3	x = x ^ 3	


# Python Comparison Operators
# Comparison operators are used to compare two values:

# ==	Equal	x == y	
# !=	Not equal	x != y	
# >	Greater than	x > y	
# <	Less than	x < y	
# >=	Greater than or equal to	x >= y	
# <=	Less than or equal to	x <= y	

x = 5
y = 3

print(x == y)

# returns False because 5 is not equal to 3

# Python Logical Operators
# Logical operators are used to combine conditional statements:

# and 	Returns True if both statements are true	x < 5 and  x < 10	
# or	Returns True if one of the statements is true	x < 5 or x < 4	
# not	Reverse the result, returns False if the result is true	not(x < 5 and x < 10)
x = 5

print(not(x > 3 and x < 10))

# returns False because not is used to reverse the result
#############
# Python Identity Operators
# Identity operators are used to compare the objects, not if they are equal, but if they are actually the same object, with the same memory location:

# is 	Returns True if both variables are the same object	x is y	
# is not	Returns True if both variables are not the same object	x is not y