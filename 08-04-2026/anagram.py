def anagram(str1,str2):
    str1=sorted(str1.lower())
    str2=sorted(str2.lower())

    if str1==str2:
        return "Anagram"
    else:
        return "Not an Anagram"
    
str1=input("Enter a string1: ")
str2=input("Enter a string2: ")
print(f"{anagram(str1,str2)}")

