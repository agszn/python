# OOP	
# Object oriented.	
# Program is divided into objects.	
# Bottom-up approach.	
# Inheritance property is used.	
# Encapsulation is used to hide the data.	
# use for solving big problems.
# e.g. C++, Java.

# POP
# Structure oriented.
# Program is divided into functions.
# Top-down approach.
# Inheritance is not allowed.
# No data hiding.
# Not suitable for solving big problems.
# C, Pascal.


# OOPs Concepts in Python
# Class
# Objects
# Polymorphism
# Encapsulation
# Inheritance
# Data Abstraction

# Python Class 
# A class is a collection of objects. 
# A class contains the blueprints or the prototype from which the objects are being created.
# It is a logical entity that contains some attributes and methods.

# Python3 program to
# demonstrate defining
# a class

class Dog:
	pass

# Python Objects
# The object is an entity that has a state and behavior associated with it. 
# It may be any real-world object like a mouse, keyboard, chair, table, pen, etc. 
# Integers, strings, floating-point numbers, even arrays, and dictionaries, are all objects. 
# More specifically, any single integer or any single string is an object. 
# The number 12 is an object, the string “Hello, world” is an object, a list is an object that can hold other objects, and so on.
obj = Dog()


class Dog:

	# class attribute
	attr1 = "mammal"

	# Instance attribute
	def __init__(self, name):
		self.name = name
		
	def speak(self):
		print("My name is {}".format(self.name))

# Driver code
# Object instantiation
Rodger = Dog("Rodger")
Tommy = Dog("Tommy")

# Accessing class methods
Rodger.speak()
Tommy.speak()
