from abc import ABC, abstractmethod

class MyAbstractClass(ABC):
    @abstractmethod
    def my_abstract_method(self):
        pass

class MyDerivedClass(MyAbstractClass):
    def my_abstract_method(self):
        return "This is the implementation of the abstract method."

# You cannot create an instance of the abstract base class:
# abstract_instance = MyAbstractClass()  # This will raise a TypeError

# You can create an instance of the derived class:
derived_instance = MyDerivedClass()
result = derived_instance.my_abstract_method()
print(result)  # This will print "This is the implementation of the abstract method."
