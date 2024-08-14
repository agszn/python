#Import in python is similar to #include header_file in C/C++. 
#Python modules can get access to code from another module by importing the file/function using import. 
#The import statement is the most common way of invoking the import machinery, but it is not the only way.

#import module_name

#When the import is used, it searches for the module initially in the local scope by calling __import__() function. 
#The value returned by the function is then reflected in the output of the initial code. 

import math
pie = math.pi
print("The value of pi is : ",pie)

from math import pi

# Note that in the above example,
# we used math.pi. Here we have used
# pi directly.
print(pi)

from math import *
print(pi)
print(factorial(6))

import mathematics
print(mathematics.pi)
