import math
def second_smallest(arr):
    first=second=math.inf
    
    for i in range(0, len(arr)):
        if arr[i] < first:
            second = first
            first = arr[i]

        elif (arr[i] < second and arr[i] != first):
            second = arr[i];

    return second

a = list(map(int, input("Enter numbers separated by space: ").split()))
print("second smallest element in a Array:",second_smallest(a))
