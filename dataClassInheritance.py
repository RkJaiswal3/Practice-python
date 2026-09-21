from dataclasses import dataclass

@dataclass
class Person:
  name: str
  age: int

@dataclass
class Employee(Person):
  empId: str
  department: str


person = Person("Rohit", 12)

emp = Employee("Hari", 24, "123", "IT")

print(f"Name: {emp.name} ")