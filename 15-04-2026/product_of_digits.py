def prod_of_digits(num):
    product=1
    while num>0:
        digit=num%10
        product*=digit
        num//=10
    return product

num=int(input("enter a number: "))
print(f"product of digits for {num} is : ",prod_of_digits(num))
