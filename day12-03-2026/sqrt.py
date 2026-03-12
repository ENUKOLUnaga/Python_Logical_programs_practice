def mySqrt(self, x):
    n=x
    while n*n>x:
        n=(n+x//n)//2 
    return n