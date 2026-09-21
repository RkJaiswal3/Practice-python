#List is a collection of items in a particular order. It is one of the most commonly used data structures in Python. Lists are mutable, meaning you can change their content without changing their identity.

lst = [1,2,2,"rohit","ram",3,4,5]
print(lst)
print(lst[3])  # Output: ram

lst = list([1,2,2,3,4,5])  # This will create a list from the provided iterable
print(lst)

lst.append(6)  # This will add the element 6 to the end of the list
print(lst)  # Output: [1, 2, 2, 3, 4, 5, 6]

lst.insert(4, "new")  # This will insert the element "new" at index 4
print(lst)  # Output: [1, 2, 2, 3, 'new', 4, 5, 6]

print("Length of the list:", len(lst))  # Output: 8
 
print("pop after index 4:", lst.pop(4))  # This will remove and return the element at index 4

for i in lst:
    print(i+5)   # This will print each element in the list

 # This will add the list [7, 8, 9] as a single element to the end of the list
lst.append([7,8,9])
print(lst)  # Output: [1, 2, 2, 3, 4, 5, 6, [7, 8, 9]]

print('Nested list: ',lst[7][1]) # Output: 8, this accesses the element at index 7
print(lst[2:5])  # Output: [2, 3, 'new'], this slices the list from index 2 to 4. 'new' is not included in the slice.Because the end index is exclusive in Python slicing.Like N -1. If you want to include the end index, you can use N+1. For example, lst[2:6] will give you [2, 3, 'new', 4].

lst.extend([10,11,12])  # This will add the elements 10, 11, and 12 to the end of the list
print(lst)  # Output: [1, 2, 2, 3, 'new', 4, 5, 6, [7, 8, 9], 10, 11, 12]


print("Sum : ", sum(lst[0:3]))  # This will calculate the sum of the elements from index 0 to 2. Output: 5

print(lst.count(2))  # This will count the number of occurrences of the element 2 in the list. Output: 2

lst1 = [1,3,2,2,2,3,4,5,6,7,8,8]
print("Index of 2:", lst1.index(2, 0, 3))  # This will return the index of the first occurrence of the element 2 in the list between index 0 and 2. Output: 2
