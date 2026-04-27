"Find indices of two numbers that add up to target."

def two_sum(nums,target):
    d={}
    for i,num in enumerate(nums):
        diff=target-num
        if diff in d:
            return [d[diff],i]
        d[num]=i
lis=list(map(int, input().split()))
target=int(input())
print(two_sum(lis,target))