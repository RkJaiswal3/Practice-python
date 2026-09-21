class A:
  def __init__(self, name, age, addr):
    self.name = name
    self.age = age
    self.addr = addr


  def getDetails(self, sound):
    print("Details of the person : ",self.name, self.age, self.addr, sound)


obj1 = A("Rohit", 12, "KTM")
obj1.getDetails("own own")


