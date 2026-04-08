def vowel_counter(str):
    count=0
    str.lower()
    for i in str:
        if i=='a' or i=='e' or i=='i' or i=='o' or i=='u':
            count+=1

    return count

str=input("Enter a string: ")
print(f"count of vowels in {str} is : {vowel_counter(str)}")
