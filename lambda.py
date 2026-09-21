#Lambda function syntax 
# lambda arguments : expression 

h = lambda x, y : x+y
print(type(h))
print(h(5,6))


#find out he squares of the list using lambda

numbers = [1,2,3,4,5,6]

strings = list(map(lambda x:x**2, numbers))
print(strings)

#filter out even numbers from a list

nums = [1,2,3,4,5,6]

evenNumbers = list(filter(lambda x: x%2==0, nums))
print(evenNumbers)

#strings sorted

strings = ['apple', 'ball', 'dog', 'cat']
print(sorted(strings, key=lambda x: len(x))) #by len the strings having store in the list


#complex task
#sort a list of dictionaries based on a specific key 

dict1 = [
  {"name": "rohit", "age": 45, "addr":"KTM"},
  {"name": "shya", "age": 42, "addr":"KTM"},
  {"name": "hari", "age": 41, "addr":"KTM"},
  {"name": "gita", "age": 47, "addr":"KTM"},
  {"name": "kittu", "age": 35, "addr":"KTM"},
  {"name": "aaron", "age": 85, "addr":"KTM"},
  {"name": "me", "age": 90, "addr":"KTM"},

         ]
print(sorted(dict1, key=lambda x: x['age']))

#finding the max value in a dictionary 

dict2 = {'a': 34, 'b':90}

print(max(dict2, key=lambda x : dict2[x]))