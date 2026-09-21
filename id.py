# here id used to point the memory location of the variable. It is used to get the identity of an object. The id() function returns a unique integer for the specified object, which represents its memory address in CPython implementation.

# a = "sita"
# b = "sita"
# print(id(a))
# print(id(b))
# print(id(a) == id(b)) #check the values are same or not

# print(a is b) # check the memory location of a and b are same or not


# onece again 
a = [1,2,3]
b = [1,2,3]
print(id(a))
print(id(b))
print(id(a) == id(b)) #check the values are same or not
print(a is b) # check the memory location of a and b are same or notx