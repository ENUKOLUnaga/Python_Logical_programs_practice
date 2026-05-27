"""
Check Whether or Not the Two Numbers  are Friendly Pairs in Python
Given two integer numbers as the input, the objective is to check whether or not the two numbers are Friendly pairs of each other. Therefore, we’ll write a Program to Check Whether or Not the Two Numbers are Friendly Pairs in Python.

Example
Input : 6 28
Output : Yes, they are a friendly pair
"""

def printDivisors(n,factors):
    i=1
    while i<=pow(n,0.5):
        if n%i==0:
            if(n/i==i):
                factors.append(i)
            else:
                factors.append(i)
                factors.append(int(n/i))
        i=i+1
    return sum(factors)-n
num1,num2=map(int,input().split())
if int(printDivisors(num1,[])/num1)==int(printDivisors(num2,[])/num2):
    print("Friendly pair")
else:
    print("Not a friendly pair")