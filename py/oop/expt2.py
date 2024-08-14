# Abstraction, Encapsulation, Class, Constructor, Destructor
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        pass

    def __del__(self):
        print(f"{self.name} has been destroyed")

# Inheritance
class Dog(Animal):
    def speak(self):
        return f"{self.name} says Woof!"

# Polymorphism, Override
class Cat(Animal):
    def speak(self):
        return f"{self.name} says Meow!"

# Overload
class Calculator:
    def add(self, a, b):
        return a + b

    def add(self, a, b, c):
        return a + b + c

# Procedure-Oriented Programming (Function)
def add_numbers(x, y):
    return x + y

# Create objects and demonstrate the concepts
if __name__ == "__main__":
    # Objects
    dog = Dog("Buddy")
    cat = Cat("Whiskers")

    # Polymorphism
    animals = [dog, cat]
    for animal in animals:
        print(animal.speak())

    # Overload
    calc = Calculator()
    print("Sum (2 args):", calc.add(5, 3))
    print("Sum (3 args):", calc.add(5, 3, 2))

    # Procedure-Oriented Programming
    result = add_numbers(10, 20)
    print("Sum (Procedure-Oriented):", result)

    # Destructor
    del dog
    del cat
