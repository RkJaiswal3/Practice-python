# Numpy is a general purpose array-processing package. It provides a high performance multidimenshional array object, and tools for working with these arrays.

import numpy as np

lst = [1,2,3,4,5,6]
new_array = np.array(lst)

print("Array:", new_array )

print("Type of Array:", type(new_array))

lst1 = [1,2,3,4,5]
lst2 = [1,2,3,4,5]
lst3 = [1,2,3,4,5]

multiArray=np.array([lst1, lst2, lst3])

print(multiArray)

print("Showing rows and column: ",multiArray.shape)

new_array[5]=7 #changing the values in index 5 by 7
print("Showing the element only skipping first one :", new_array[1:])#accessing the elements from an array
print('Showing by skipping last element: ',new_array[::-1]) #accessing the elements from an array by reversing the array
print('Showing every second element: ',new_array[::-2])

#now in the case of multidimenstional array 
print('Accessing first column: ',multiArray[:,1]) #access all the rows and the first column means index 1

#if i want to access the different way matrix values

print(multiArray[1:,2:4])

print(multiArray[:,[0, 4]]) #first and last column 
print(multiArray[:,[0, 4]].shape) #first and last column 

#EDA point of view
print("EDA: ", multiArray[multiArray<3])

print("Reshape of Array: ",multiArray.reshape(5,3))


#mechanishm to build array 
newArray1= np.arange(2,45,2)
print("New Array : ", newArray1)

print(np.zeros((2,4)))
print(np.ones((2,4)))

print(multiArray[1,4])
print(newArray1.size)
print(newArray1.reshape(2,11))

arr = np.arange(1, 13)

newArray3 = arr.reshape(2, 2, -1)

print("Array with arange use: ", newArray3)


#to generate random number

random1 = np.random.randint(2,10, 4).reshape(2,2)
print("Random num: ",random1)

randomArray = np.random.randn(5,6)
print("Random Array : ", randomArray)

randomArray1 = np.random.random_sample((5,6))  # to generate all the values between 0 to 1
print("Random Array 1: ", randomArray1)