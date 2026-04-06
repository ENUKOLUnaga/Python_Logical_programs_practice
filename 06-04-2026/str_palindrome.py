def palindrome(str):
    rev = str[::-1]

    if str == rev:
        return rev + " is Palindrome"
    else:
        return rev + " is not Palindrome"

str=input("Enter a string: ")
print(f"{palindrome(str)}")
