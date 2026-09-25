import pandas as pd
import numpy as np

df = pd.DataFrame(data = np.arange(0, 20).reshape(5,4), index = ['A', 'B', 'C', 'D', 'E'], columns = ['W', 'X', 'Y', 'Z'])
print(df)

print(type(df))

#df.info() #gives the information about the data frame
print(df.describe()) #gives the statistical information about the data frame it only select integer and float values and give the statistical information about it.


print(df.loc['A']) #loc is used to access the row data by using index name
print(df.iloc[3:5,2:4].values) #iloc is used to access the row data by using index number
print(df.isnull().sum()) #isnull is used to check the null values in the data frame and sum() is used to count the null values in the data frame.