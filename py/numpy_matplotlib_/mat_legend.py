# What is a Legend?
# A legend is an area describing the elements of the graph. 
# In simple terms, it reflects the data displayed in the graph’s Y-axis. 
# It generally appears as the box containing a small sample of each color on the graph and a small description of 
# what this data means.

# Creating the Legend
# A Legend can be created using the legend() method. 
# The attribute Loc in the legend() is used to specify the location of the legend. 
# The default value of loc is loc=”best” (upper left). 
# The strings ‘upper left’, ‘upper right’, ‘lower left’, ‘lower right’ place the legend at the corresponding corner of the axes/figure.

import matplotlib.pyplot as plt

# data to display on plots
x = [3, 1, 3]
y = [3, 2, 1]
plt.plot(x, y)
plt.plot(y, x)

# Adding the legends
plt.legend(["blue", "orange"])
plt.show()
