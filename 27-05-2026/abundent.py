def abundant_number(n):
    sum=1
    for i in range(2,n):
        if n%i==0:
            sum=sum+i
    if sum>n:
        return "abundant number"
    else:
        return "Not a abundant number"

n=int(input("enter a number: "))
print(abundant_number(n))
