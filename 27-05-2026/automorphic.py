def Automorphic_number(number):
    square=pow(number,2)
    mod=pow(10,len(str(number)))

    if square%mod==number:
        print("It's an automorphic number")
    else:
        print("It's not an automorphic number")
    

n=int(input("Enter a number: "))
Automorphic_number(n)