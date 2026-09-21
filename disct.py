# dictionary is a collection of key-value pairs. It is an unordered collection, meaning that the elements do not have a specific order. Dictionaries are mutable, which means that you can add or remove elements from a dictionary after it has been created. This is based on data structure called hash table. Dictionaries are useful when you want to store a collection of items and access them using keys.

type({}) #by default this will create an empty dictionary. To create an empty set, you need to use the set() constructor.but when i add curly braces with elements inside, it will create a dictionary. For example, {1: "one", 2: "two"} will create a dictionary with the keys 1 and 2 and their corresponding values "one" and "two".

# or 

type({1}) #this will give us set because it has only one element. To create a dictionary with one key-value pair, you need to use the syntax {key: value}. For example, {1: "one"} will create a dictionary with the key 1 and its corresponding value "one".

type({1: "one", 2: "two"}) #this will give us dictionary because it has two key-value pairs. To create a dictionary with multiple key-value pairs, you can use the syntax {key1: value1, key2: value2, ...}. For example, {1: "one", 2: "two"} will create a dictionary with the keys 1 and 2 and their corresponding values "one" and "two".

print(dict({1: "one", 2: "two"})) #this will give us dictionary because it has two key-value pairs. To create a dictionary with multiple key-value pairs, you can use the syntax {key1: value1, key2: value2, ...}. For example, {1: "one", 2: "two"} will create a dictionary with the keys 1 and 2 and their corresponding values "one" and "two".

print(dict(name="rohit", age=26)) #this will create a dictionary with the keys "name" and "age" and their corresponding values "rohit" and 26.


my_car = {"name": "rohit", "age": 26, "color": "red"}
print(my_car["name"])  # Output: rohit, this will print the value associated with the key "name" in the dictionary my_car

print(my_car.items())  # This will return a view object that displays a list of a dictionary's key-value tuple pairs. Output: dict_items([('name', 'rohit'), ('age', 26), ('color', 'red')])

print(my_car.keys())  # This will return a view object that displays a list of all the keys in the dictionary. Output: dict_keys(['name', 'age', 'color'])
print("Values:",my_car.values())

#iterate using for loop

for i in my_car.items():
    print(i)  # This will print each key-value pair in the dictionary my_car

#add in dictionary 
my_car["model"] = "SUV"  # This will add a new key-value pair to the dictionary my_car
print(my_car)  # Output: {'name': 'rohit', 'age': 26, 'color': 'red', 'model': 'SUV'}, this will print the updated dictionary my_car after adding the new key-value pair

#nested dictionary
car1_model = {"model": "SUV", "year": 2020}
car2_model = {"model": "sedan", "year": 2021}
car3_model = {"model": "benz", "year": 2021}

car_type = {"car1": car1_model, "car2": car2_model, "car3": car3_model}
print(car_type)