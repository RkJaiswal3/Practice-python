# Pickling is the process of converting python object into a byte stream and unpickling is the inverse operation. The pickle module is implements the binary protocal in seriliazing and deserializing way of pyton object.

import seaborn as sns
import pickle as pkd

data = sns.load_dataset('tips')
# print(data.head())

fileName = 'file.pkl'

#serialized process
# pickling process

# print(pkd.dump(data, open(fileName, mode="wb")))


# Unpickling process
df = pkd.load(open(fileName, 'rb'))


print(type(df))
print("Unpickeled",df)
print("The pickling process is completed successfully !")

#we can also make the byte stream file of json data too

dict_example = {"name": "rohit", "age": 32, "add": "KTM"}

print(pkd.dump(dict_example, open('dict.pkl', "wb")))
print("Pickled json object :")

#now unpickling 
print(pkd.load(open('dict.pkl', "rb")))