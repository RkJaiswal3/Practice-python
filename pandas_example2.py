import pandas as pd
import numpy as np

dataFrame = pd.DataFrame(data=[[1, np.nan, 3], [4, 5, 6]], index=['Row1', 'Row2'], columns=['Col1', 'Col2', 'Col3'])
print("DataFrame is : \n", dataFrame)
print("Null Values: ", dataFrame.isnull().sum())

