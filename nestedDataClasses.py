from dataclasses import dataclass

@dataclass
class Person:
  name: str
  age : int

@dataclass
class Emp:
    id: int
    depart: str
    details: Person


pers = Person("rohit", 24)
emp = Emp(1, "IT", pers)

print(emp.details.age)


