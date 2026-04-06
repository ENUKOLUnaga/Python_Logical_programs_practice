def reverse(str):
    rev = ''
    for i in range(1,len(str)+1):
        rev+=str[-i]
    return rev

str=input("Enter a string: ")
print(f"{reverse(str)}")
