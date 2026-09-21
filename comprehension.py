#square using exponent sign
lst = [1,2,3,4,5,6]
sqrtNum = [i**2 for i in lst ]
print("Square numbers: ",sqrtNum)

#even numbers
evenNumbers = [i for i in range(0,24) if i%2==0]
print("Even numbers: ", evenNumbers)

#flatten list example using 2 for loop
lst1 = [[1,2],[3,4],[5,6]]

flatenList = [items for sublist in lst1 for items in sublist]
print(flatenList)


#Generating a list of the first letters of words in a list:
wordlist = ["rohit", "shyam"]
items = [i[0] for i in wordlist]
print(items)


#Coverting list string to integer
strings = ['1','2','3','4','5']

interValue = [int(n) for n in strings]
print("Integer values: ",interValue)

#fibonasis series

fib = [0,1,2,3,4,5,6,7,8,9,10]
series = [fib[i-1] + fib[i-2] for i in range(2,len(fib))]
print(series)

#generating the numbers of devisiors 

number = 46
devisior = [i for i in range(1, number+1) if number%i == 0]
print("Divisors: ", devisior)

