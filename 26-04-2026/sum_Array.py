def SumOfArray(arr):
    Sum = 0

    for i in range(len(arr)):
        Sum = Sum + arr[i]
    return Sum

a = list(map(int, input("Enter numbers separated by space: ").split()))
print("Total Sum of Array:",SumOfArray(a))
