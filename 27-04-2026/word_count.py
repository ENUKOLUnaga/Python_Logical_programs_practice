from collections import Counter

def word_count(text):
    c=Counter(text.split())

    return c

text=input("Enter a message: ")
print(f"count of words {text} : {word_count(text)}")
