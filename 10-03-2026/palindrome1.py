def isPalindrome(x):
        n=x
        r=0
        while x>0:
            r=r*10+(x%10)
            x=x//10
        if r==n:
            return True
        else:
            return False
number=int(input("Enter a number: "))
res=isPalindrome(number)
print(res)
