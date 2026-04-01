def smallestInArray(a):
    min_element = a[0]

    for i in range(len(a)):
        if a[i] < min_element:
            min_element = a[i]
    return min_element

a = list(map(int, input("Enter numbers separated by space: ").split()))
print("Largest element in a Array:",smallestInArray(a))