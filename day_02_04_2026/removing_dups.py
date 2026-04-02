def removeDuplicates(arr, n):
    if n == 0 or n == 1:
        return n

    temp = list(range(n))

    # Start traversing elements
    j = 0;
    for i in range(0, n-1):
        if arr[i] != arr[i+1]:
            temp[j] = arr[i]
            j += 1

    temp[j] = arr[n-1]
    j += 1
    for i in range(0, j):
        arr[i] = temp[i]

    return j

a = list(map(int, input("Enter numbers separated by space: ").split()))

n = len(a)

n = removeDuplicates(a, n)

# Print updated array
for i in range(n):
    print(a[i], end = " ")
