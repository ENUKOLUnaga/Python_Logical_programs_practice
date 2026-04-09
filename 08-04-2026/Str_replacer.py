def str_replace(string,str1,str2):
    replaced_string=string.replace(str1,str2)

    return replaced_string

string=input("Enter a string: ")
str1=input("Enter a sub string: ")
str2=input("Enter a string which you need to place: ")
print(f"after replacing string {str_replace(string,str1,str2)}")

