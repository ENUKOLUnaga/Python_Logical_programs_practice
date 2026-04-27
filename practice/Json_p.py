import json
data={
    "name":"Nagendra",
    "age": 21
}

json_str=json.dumps(data)
print(json_str)

data1=json.loads(json_str)
print(data1["name"])