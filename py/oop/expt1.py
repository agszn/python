# Abstraction: Create a class 'Animal' as a blueprint for all animals
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        pass  # Abstract method, to be overridden by subclasses

# Inheritance: Create subclasses for different types of animals
class Dog(Animal):
    def speak(self):
        return f"{self.name} says Woof!"

class Cat(Animal):
    def speak(self):
        return f"{self.name} says Meow!"

# Encapsulation: Create objects of the classes and access their attributes
my_dog = Dog("Buddy")
my_cat = Cat("Whiskers")

# Polymorphism: Call the 'speak' method on different objects
print(my_dog.speak())  # Outputs: Buddy says Woof!
print(my_cat.speak())  # Outputs: Whiskers says Meow!

# Procedure-Oriented Programming: Create functions to perform actions
def feed(animal):
    return f"Feeding {animal.name}"

def pet(animal):
    return f"Petting {animal.name}"

# Objects: Use the functions on the objects
print(feed(my_dog))  # Outputs: Feeding Buddy
print(pet(my_cat))  # Outputs: Petting Whiskers

# Destructor: We don't need explicit destructors in Python; the objects are automatically destroyed when they go out of scope.

# Override: The 'speak' method in each subclass overrides the 'speak' method in the parent class.

# Overload: In Python, method overloading isn't explicitly supported, but you can achieve it through optional parameters or different method names.
