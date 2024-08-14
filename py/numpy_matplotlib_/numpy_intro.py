# What is NumPy? 
# NumPy is a general-purpose array-processing package. 
# It provides a high-performance multidimensional array object and tools for working with these arrays. 

# Install Python NumPy
# pip install numpy

# Arrays in NumPy
# NumPy’s main object is the homogeneous multidimensional array.

# It is a table of elements (usually numbers), all of the same type, indexed by a tuple of positive integers.
# In NumPy, dimensions are called axes. The number of axes is rank.
# NumPy’s array class is called ndarray. It is also known by the alias array.

import numpy as np

# Creating array object
arr = np.array( [[ 1, 2, 3],
				[ 4, 2, 5]] )

# Printing type of arr object
print("Array is of type: ", type(arr))

# Printing array dimensions (axes)
print("No. of dimensions: ", arr.ndim)

# Printing shape of array
print("Shape of array: ", arr.shape)

# Printing size (total number of elements) of array
print("Size of array: ", arr.size)

# Printing type of elements in array
print("Array stores elements of type: ", arr.dtype)

