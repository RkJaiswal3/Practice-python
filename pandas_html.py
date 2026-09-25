# read_html()
# to_html()

import pandas as pd

html = pd.read_html("https://help.monitorerp.com/CN-MONITOR_G5/en-us/Content/Topics/GeneralRegisters/OtherTables/Countries/bCountries.htm", 
match="Address format")
print(type(html))
print(html)
print(type(html[0]))
html[0].to_html('demo.html')
# df = html[0]

# df.columns = df.iloc[0]
# df=df[1:]
# df.reset_index(drop=True, inplace=True)
# print(df.columns.tolist())

# data= df.iloc[:,0:2]
# print("New Data\n",data.fillna(0))

