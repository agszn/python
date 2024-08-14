# Figure: This class is the top-level container for all the plots means it is the overall window or page on which everything 
#is drawn. A figure object can be considered as a box-like container that can hold one or more axes.
# Axes: This class is the most basic and flexible component for creating sub-plots. 
#You might confuse axes as the plural of axis but it is an individual plot or graph. 
#A given figure may contain many axes but given axes can only be in one figure.

# Figure class
# Figure class is the top-level container that contains one or more axes. 
#It is the overall window or page on which everything is drawn.

# Python program to show pyplot module
import matplotlib.pyplot as plt
from matplotlib.figure import Figure

# Creating a new figure with width = 5 inches
# and height = 4 inches
fig = plt.figure(figsize =(5, 4))

# Creating a new axes for the figure
ax = fig.add_axes([1, 1, 1, 1])

# Adding the data to be plotted
ax.plot([2, 3, 4, 5, 5, 6, 6],
		[5, 7, 1, 3, 4, 6 ,8])
plt.show()
