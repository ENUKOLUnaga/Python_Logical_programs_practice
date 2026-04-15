#sum of digits
#input 352
#output 10
def sumOfDigits(num):
    sum=0
    while num>0:
        sum=sum+(num%10)
        num=num//10
    return sum
number=int(input("Enter a number: "))
print(sumOfDigits(number))