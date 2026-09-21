from dataclasses import dataclass

@dataclass
class Person:
  name: str
  age: int
  addr: str = "KTM"

#the data classes decortar automatically generates the following methods for you :

# __init__():Initialilze the object and assigns the provided values to the attributes
# __repr__(): Provides a string representation of th object
# __eq__(): Implements equality comparison between two objects of the class based on their attributes

person1 = Person("Rohit", 24, "Pune") #overrite the address
print(f"My name is {person1.name}. My age is {person1.age}. I live in {person1.addr}")


