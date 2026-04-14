def reverse(num):
    res=0
    while num>0:
        res=res*10+(num%10)
        num=num//10
    return res
def palindromeOrNot(num):
    result=reverse(num)
    if result==number:
        print("Palindrome")
    else:
        print("Not a palindrome")

number=int(input("Enter a number: "))
palindromeOrNot(number)

