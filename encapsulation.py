#access modifier encapsulation
class Person:
  def __init__(self, name, age):
    self.__name= name
    self.__age= age

  def display_info(self):
    print(f"The name is {self.__name} and age is {self.__age}")


per = Person("Rohit", 24)
per.display_info()