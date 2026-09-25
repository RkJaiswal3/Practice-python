#read_json()
#convert to_json()
#json_normalization()

import pandas as pd
from io import StringIO
data = '''[{"name": "rohit", "age": 29}, {"name": "sachin", "age": 30}]'''
print(type(data))
print(pd.read_json(StringIO(data)))




