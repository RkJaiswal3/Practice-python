# Set in python is a collection of unique elements. It is an unordered collection, meaning that the elements do not have a specific order. Sets are mutable, which means that you can add or remove elements from a set after it has been created.This is based on data structure called hash table. Sets are useful when you want to store a collection of unique items and perform operations like union, intersection, and difference.

from distro import name


type({}) #by default this will create an empty dictionary. To create an empty set, you need to use the set() constructor.but when i add curly braces with elements inside, it will create a set. For example, {1, 2, 3} will create a set with the elements 1, 2, and 3.

val = set({1, 2, 3, 4, 5, 6, 7, 8, 9})
print(val)  # Output: {1, 2, 3, 4, 5, 6, 7, 8, 9}, this will print the set with the specified elements

new = set({1, 2, 3, 4, 4, 5, 6, 7, 8, 9})
print(new)  # Output: {1, 2, 3, 4, 5, 6, 7, 8, 9}, this will create a set from the set literal, removing duplicates

newVal = {"rohit", "ram", "shyam"}
# print(newVal[1])  # This will raise an error because sets are unordered and do not support indexing
#but you can iterate over the set using a for loop or convert it to a list to access elements by index.

for i in newVal:
  print(i)


my_set = {1, 2, 3, 4, 5}
new_set = {4, 5, 6, 7, 8}
# Union of two sets
print("Union:", my_set.union(new_set))  # Output: {1, 2, 3, 4, 5, 6, 7, 8}, this will return a new set containing all unique elements from both sets
# Intersection of two sets
print("Intersection:", my_set.intersection(new_set))  # Output: {4, 5}, this will return a new set containing only the elements that are present in both sets
# Difference of two sets
print("Difference:", my_set.difference(new_set))  # Output: {1, 2, 3}, this will return a new set containing the elements that are present in my_set but not in new_set

my_set.add(6)  # This will add the element 6 to the set
print(my_set)  # Output: {1, 2, 3, 4, 5, 6}, this will print the updated set after adding the new element

num = set({1,5,3,21,67,2,3,4,5,6,7,8,9})

print(num)  # Output: {1, 2, 3, 4, 5, 6, 7, 8, 9, 21, 67}, this will create a set from the provided list and remove duplicates
num.add(14)
print(num)  # This will add the element 14 to the set 



# for example 
lst = list([1, 2, 3, 4, 5, 6, 7, 8, 9])
lst1 = list([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15])
set1 = set(lst)
set2 = set(lst1)
print("Intersection:", set1.intersection(set2))  # Output: {1, 2, 3, 4, 5, 6, 7, 8, 9}, this will return a new set containing only the elements that are present in both sets


set1N = {"rohit", "ram", "shyam"}
set2N = {"shyam", "ram", "hari"}
print("Intersection update:", set2N.intersection_update(set1N))  # Output: None, this will update set1N to contain only the elements that are present in both sets
print("Updated set2N:", set2N)  # Output: {'ram', 'shyam'}, this will print the updated set1N
