# if the data written in excel. And then it is ready by pandas library in python, It will be treated as a data structure which called data frame.


import pandas as pd
import numpy as np

#Dataframe creation

arr = np.arange(0,20).reshape((5,4))
print(arr)

dataFrame1 = pd.DataFrame(data=arr,index=["Row1", "Row2", "Row3", "Row4", "Row5"], columns=["Num1", "Num2", "Num3", "Num4"])

print("DataFrame : \n", dataFrame1)
print("DataFrame : \n", dataFrame1.head()) #Want to see top 5 records use head()
print("DataFrame : \n", dataFrame1.tail()) #Want to see last 5 record use tail()

print(dataFrame1.info()); #Show dataframe information 
print(dataFrame1.describe()); #Show dataframe information 

#indexing 
#DIrect by using column name
#Another is using rowindex[loc]
#rowindex columnindex number[.iloc]


print("Column Data: \n",dataFrame1[['Num1', 'Num2']]) #BY using column name 

#In series either one row or one column but in dataframe has multiple
print("Row Data:\n",dataFrame1.loc['Row1']) #using loc to access the row data
print(dataFrame1.iloc[2:4,2:]) #using iloc to access the row and column data


# syntax 
# DataFrame.iloc[row_selection, column_selection]

print(dataFrame1.iloc[:,[0,3]]) #using brackets to access the column data too.

# converting dataFrame1 into arrays
print("Arrays of dataframe : ", dataFrame1.values)

print(dataFrame1.isnull().sum())

print("Unique vallues: ",  dataFrame1['Num2'].value_counts()) #help to count occurrence how many times in a column
print("Unique:", dataFrame1['Num1'].unique())

print(dataFrame1[dataFrame1['Num1']>2])