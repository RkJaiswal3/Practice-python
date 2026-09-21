i = 1
evenSum = 0
oddSum = 0
while(i < 10):
    if(i%2 == 0):
      evenSum = evenSum + i
    else:
      oddSum = oddSum + i
    i = i + 1
print("The sum of even numbers is: ", str(evenSum))
print("The sum of odd numbers is: ", str(oddSum))