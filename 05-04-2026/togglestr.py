def toggle_str(str):
    String1 = ''
    for i in str:
        if i.isupper():
            i = i.lower()
            String1 = String1 + i
        else:
            i = i.upper()
            String1 = String1 + i
    return String1

str=input("Enter a string: ")
print(f"toggle of {str} is : {toggle_str(str)}")
