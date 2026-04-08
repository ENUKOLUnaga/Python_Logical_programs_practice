def str_space_remove(str):
    s=''
    for i in range(len(str)):
        if str[i]!=' ':
            s+=str[i]
    return s

str=input("Enter a string: ")
print(f"{str} without spaces : {str_space_remove(str)}")
