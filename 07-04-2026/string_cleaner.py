def str_cleaner(str):
    str1=''
    for i in range(len(str)):
        if ((str[i]>='A' and str[i]<='Z') or (str[i]>='a' and str[i]<='Z')):
            str1+=str[i]
    return str1

str=input("Enter a string: ")
print(f" {str} after cleaning : {str_cleaner(str)}")
