def printOrder(arr,n) :
    # sorting the array
    arr.sort()
    i = 0
    while i < n/2: 
        print(arr[i]) 
        i=i+1 
        
a = list(map(int, input("Enter numbers separated by space: ").split()))

n=len(a)
printOrder(a,n)

