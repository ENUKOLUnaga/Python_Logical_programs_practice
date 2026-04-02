def printOrder(arr,n) :
    # sorting the array
    arr.sort()
    
    # print in sorted order
    i = 0
    while i < n: 
        print(arr[i]) 
        i=i+1 
        
    
a = list(map(int, input("Enter numbers separated by space: ").split()))
n=len(a)
printOrder(a,n)
