import pandas as pd
from io import StringIO

df = pd.read_excel('data.xlsx', usecols=('Customer Name', 'State','Country','Sales'))

print(df.tail())

df.to_csv('text.csv', index=False)

print(type(df)) #create dataframe of each file in python. It is treated first as a dataframe

data = ('col1, col2\n'
        '1, 2\n'
        'a, b\n')

# print(type(data))
# print(data)

# print(StringIO(data))
# print(pd.read_csv(StringIO(data)))