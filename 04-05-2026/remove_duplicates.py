def remove_duplicates(str):
    seen=set()
    result=[]
    for ch in str:
        if ch not in seen:
            seen.add(ch)
            result.append(ch)
    return "".join(result)

str=input("enter a string: ")
result=remove_duplicates(str)
print("first non repeating character: ",result)
