import math
# print(abs(-5)) # returns the absolute value of -5 which is 5
# print(abs(5)) # returns the absolute value of 5 which is 5

print("Ceiling Values: " + str(math.ceil(4.2))) # returns the smallest integer greater than or equal to 4.2 which is 5
print("Floor Values: " + str(math.floor(4.8))) # returns the largest integer less than or equal to 4.8 which is 4

print("Square Root of 16: " + str(math.sqrt(16))) # returns the square root of 16 which is 4.0

print("Exponential Values: " + str(math.exp(2))) # returns the exponential value of 2 which is 7.38905609893065
print("Fabs values : " + str(math.fabs(6))) # returns the absolute value of 6 which is 6.0
print("Fabs values : " + str(math.fabs(-5))) # returns the absolute value of -5 which is 5.0
print("Logarithmic Values: " + str(math.log(100))) # returns the natural logarithm of 100 which is 4.605170185988092
print("Base 10 : " + str(math.log10(100))) # returns the logarithm of 100 to base 10 which is 2.0
print("Max : "+str(max(1,2,3,4,5))) # returns the maximum value among 1,2,3,4,5 which is 5
print("Min : "+str(min(1,2,3,4,5))) # returns the minimum value among 1,2,3,4,5 which is 1
print("Power : " + str(math.pow(2, 3))) # returns 2 raised to the power of 3 which is 8.0
print("Sqrt : " + str(math.sqrt(16))) # returns the square root of 16 which is 4.0

#Trigonometric Functions
print("Sine of 0: " + str(math.sin(0))) # returns the sine of 0 which is 0.0
print("Cosine of 0: " + str(math.cos(0))) # returns the cosine of 0 which is 1.0
print("Tangent of 0: " + str(math.tan(0))) # returns the tangent of 0 which is 0.0
print("Degrees to Radians: " + str(math.radians(180))) # converts 180 degrees to radians which is 3.141592653589793

# hypotenuse of a right-angled triangle
print("Hypotenuse of a right-angled triangle with sides 3 and 4: " + str(math.hypot(3, 4))) # returns the hypotenuse of a right-angled triangle with sides 3 and 4 which is 5.0

#modf()
print("Modf of 3.5 : " + str(math.modf(3.5))) # returns the fractional and integer parts of 3.5 which is (0.5, 3.0) 