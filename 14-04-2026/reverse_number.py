#reverse a number
#input 253
#output 352
def reverse(num):
    res=0
    while num>0:
        res=res*10+(num%10)
        num=num//10
    return res
number=int(input("Enter a number: "))
print(reverse(number))

