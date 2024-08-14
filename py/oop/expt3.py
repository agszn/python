# Procedure-Oriented Programming
def addition(a, b):
    return a + b

def subtraction(a, b):
    return a - b

# Inheritance
class MathOperation:
    def __init__(self, a, b):
        self.a = a
        self.b = b

class AdvancedMathOperation(MathOperation):
    def multiply(self):
        return self.a * self.b

# Polymorphism
def perform_operation(operation, a, b):
    return operation(a, b)

# Abstraction
from abc import ABC, abstractmethod

class Calculator(ABC):
    @abstractmethod
    def calculate(self):
        pass

class Addition(Calculator):
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def calculate(self):
        return self.a + self.b

# Encapsulation
class BankAccount:
    def __init__(self, balance):
        self.__balance = balance  # Private attribute

    def get_balance(self):
        return self.__balance

# Objects, Classes, Constructor, Destructor
class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __del__(self):
        print(f"{self.name} product deleted.")

# Override
class Shape:
    def area(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius * self.radius

# Overload
class Math:
    def add(self, a, b):
        return a + b

    def add(self, a, b, c):
        return a + b + c

# Procedure-Oriented Programming
result_add = addition(5, 3)
result_sub = subtraction(5, 3)
print("Procedure-Oriented Programming:")
print("Addition:", result_add)
print("Subtraction:", result_sub)

# Inheritance
adv_math = AdvancedMathOperation(4, 2)
result_mul = adv_math.multiply()
print("\nInheritance:")
print("Multiplication:", result_mul)

# Polymorphism
polymorphic_result = perform_operation(addition, 8, 3)
print("\nPolymorphism:")
print("Polymorphic Addition:", polymorphic_result)

# Abstraction
calc = Addition(7, 2)
abstract_result = calc.calculate()
print("\nAbstraction:")
print("Abstract Addition:", abstract_result)

# Encapsulation
account = BankAccount(1000)
balance = account.get_balance()
print("\nEncapsulation:")
print("Account Balance:", balance)

# Objects, Classes, Constructor, Destructor
product1 = Product("Laptop", 800)
del product1

# Override
circle = Circle(5)
circle_area = circle.area()
print("\nOverride:")
print("Circle Area:", circle_area)

# Overload
math = Math()
result_overload = math.add(2, 3, 4)
print("\nOverload:")
print("Overloaded Addition:", result_overload)
