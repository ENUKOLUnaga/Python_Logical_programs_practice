def LCM(n1,n2):
    for i in range(max(n1,n2),1+(n1*n2),max(n1,n2)):
        if i % n1==i % n2==0:
            lcm=i
            break
    print(f"lcm of {n1} and {n2} is {lcm}")

n1,n2=map(int,input().split())
LCM(n1,n2)