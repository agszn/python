# Matplotlib is an overall package for creating static, animated, and interactive visualizations in Python.


# Matplotlib is a Python library that helps in visualizing and analyzing the data and helps in better understanding of the 
# data with the help of graphical, pictorial visualizations that can be simulated using the matplotlib library. 
# Matplotlib is a comprehensive library for static, animated and interactive visualizations.

# installation command
# pip install matplotlib

# importing the required module
import matplotlib.pyplot as plt
	
# x axis values
x = [1,2,3]
# corresponding y axis values
y = [2,4,1]
	
# plotting the points
plt.plot(x, y)
	
# naming the x axis
plt.xlabel('x - axis')
# naming the y axis
plt.ylabel('y - axis')
	
# giving a title to my graph
plt.title('My first graph!')
	
# function to show the plot
plt.show()
