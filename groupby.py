from itertools import groupby

lst  = ['apple', 'app', 'ball', 'dog', 'cap']

sortedWords = groupby(sorted(lst), key=lambda x: x[0])

for key, group in sortedWords:
  # print(key ,"=>", list(group))
  print(f"{key} => {list(group)}") #using f string


person = int('23')
print(type(person))
print(f"The element is this {person}") 