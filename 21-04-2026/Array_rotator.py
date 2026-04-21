def rotator(n,k,arr):
    k=k%n
    return arr[-k:]+arr[:-k]
n=int(input("enter the size of array:"))
k=int(input("enter the number of rotations:"))  
arr=list(map(int,input("enter the array:").split()))
print(rotator(n,k,arr))