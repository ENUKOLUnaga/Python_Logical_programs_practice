def frequency_counter(str):
    dic={}
    for i in str:
        if i in dic:
            dic[i]+=1
        else:
            dic[i]=1
    return dic

str=input("Enter a string: ")
print(f"frequency count of a string{frequency_counter(str)}")
