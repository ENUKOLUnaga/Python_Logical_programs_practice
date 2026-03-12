def plusOne(digits):
    num=0
    for d in digits:
        num=num*10+d
    num+=1
    result=list(map(int,str(num)))
    return result