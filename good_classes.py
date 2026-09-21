class A:
  # constructors
  def __init__(self, name, age, gender, addr):
    self.name = name
    self.age  = age
    self.gender = gender
    self.addr = addr


#access the methods inside the class
  def details_person(self):
    print("Details of the person :" , self.addr)

obj1 = A("Rohit", 23, "Male", "KTM")
obj2 = A("Ram", 23, "Male", "KTM")

# print("My name is "+obj1.name+"."+"I am "+str(obj1.age)+"."+"I lived in "+obj1.addr+".")
# print("My name is "+obj2.name+"."+"I am "+str(obj2.age)+"."+"I lived in "+obj2.addr+".")

obj1.details_person()

    