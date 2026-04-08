def bracket_remov(str):
    eq=''
    for i in str:
        if ord(i)==40 or ord(i)==41 or ord(i)==91 or ord(i)==93 or ord(i)==123 or ord(i)==125:
            pass
        else:
            eq=eq+i
    return eq

str=input("Enter a string: ")
print(f"{str} after removing brackets: {bracket_remov(str)}")
