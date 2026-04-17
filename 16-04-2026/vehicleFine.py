def vehicle_fine(n,last_digits,d,x):
    date_is_even=d%2==0
    total_fine=0

    for digit in last_digits:
        digit_is_even=digit%2==0
        if digit_is_even!=date_is_even:
            total_fine+=x

    return total_fine

n=int(input("Enter a number of vehicles: "))
last_digits=list(map(int,input().split()))
d,x=map(int,input().split())

print(f"Total Fine:{vehicle_fine(n,last_digits,d,x)}")
