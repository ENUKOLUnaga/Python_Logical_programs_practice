def largestInArray(a):
    max_element = a[0]

    for i in range(len(a)):
        if a[i] > max_element:
            max_element = a[i]
    return max_element

a = list(map(int, input("Enter numbers separated by space: ").split()))
print("Largest element in a Array:",largestInArray(a))
