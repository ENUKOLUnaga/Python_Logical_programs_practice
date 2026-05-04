def is_rotated(str1,str2):
    if len(str1)!=len(str2):
        return False
    
    return str2 in (str1+str1)

str1=input("enter a string1: ")
str2=input("enter a string2: ")
result=is_rotated(str1,str2)
print(result)
