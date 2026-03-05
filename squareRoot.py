#finding Square root of anumber 
num = int(input("Enter number: "))
i = 1
while i * i <= num:
    if i * i == num:
        print("Square root:", i)
        break
    i += 1