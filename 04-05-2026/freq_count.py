from collections import Counter
def first_non_repeating_character(str):
    count=Counter(str)

    for ch in str:
        if count[ch]==1:
            return ch

    return None

str=input("enter a string: ")
result=first_non_repeating_character(str)
print("first non repeating characte: ",first_non_repeating_character(str))
