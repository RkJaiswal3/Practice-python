#program to check max of 3 numbers
def max_of_three(x, y, z):
    if (x >= y) and (x >= z):
        return x
    elif (y >= x) and (y >= z):
        return y
    else:
        return z
max_value = max_of_three(3, 6, -5)
print("The maximum value is:", max_value)