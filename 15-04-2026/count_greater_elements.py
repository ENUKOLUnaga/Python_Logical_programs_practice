def count_greater(lis):
    temp=1
    max_far=lis[0]
    for i in range(1,len(lis)):
        if lis[i]>max_far:
            temp+=1
            max_far=lis[i]

    return temp


lis=list(map(int,input().split()))
print(count_greater(lis))
