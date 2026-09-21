# nested if-else

val = float(input("Enter the number: "))

if(val > 0):
  print("The number is positive")
  if(val > 16):
    print("And the num is more than 16")
  else:
    print("The num is less than 16")
elif(val < 0):
  print("The number is negative")
else:
  print("The number is zero")