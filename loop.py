# values = [1,2,3,4,5]
# name = ['Alice', 'Bob', 'Charlie', 'David', 'Eve']

# sum = 0
# for m in values:
#   sum = sum + m
# print("The sum of the values is: ", sum)
 

# for i in name:
#   print(i + ' is a person.')


# sum of add and even numbers

values = [1,2,3,4,5]
evenSum = 0
oddSum = 0
for i in values:
  if(i%2 == 0):
    evenSum = evenSum + i
  else:
    oddSum = oddSum + i

print("The sum of even numbers is: ", str(evenSum))
print("The sum of odd numbers is: ", str(oddSum))



