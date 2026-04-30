import pickle

"""data={"name":"Nagendra",
      "age":22}

#with open("data.pkl","wb") as file:
#    pickle.dump(data,file)

with open("data.pkl","rb") as file:
    print(pickle.load(file))
"""

data=[1,2,3]

byte_data=pickle.dumps(data)
print(byte_data)

original=pickle.loads(byte_data)
print(original)