def odd_elements(arr):
    return [x for x in arr if x % 2 != 0]

n=int(input("enter the size of array:"))
arr=list(map(int,input("enter the array:").split()))
print(odd_elements(arr))