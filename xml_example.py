# here we learn to read_xml()
# to_xml()

import pandas as pd

doc = pd.read_xml('student.xml', xpath='./student')
print(type(doc))
# newDoc = doc.to_json('student.json')

# xpath attributes use to extract which row should be really seen
print(doc)