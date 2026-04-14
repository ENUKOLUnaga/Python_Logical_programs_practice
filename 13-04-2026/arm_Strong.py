
def armstrong(num):
    number=num
    length=len(str(num))
    digit, sum = 0, 0
    for i in range(length):
        digit = int(num%10)
        num = num/10
        sum += pow(digit,length)
    if sum==number:
        print("Armstrong")
    else:
        print("Not Armstrong")
num=int(input("Enter a number"))
armstrong(num)