def countFreq(arr, n):
   # Mark all array elements as not visited
   visited = [False for i in range(n)]

   for i in range(n):
     # Skip this element if already
     if (visited[i] == True):
        continue

     # Count frequency
     count = 1
     for j in range(i + 1, n, 1):
        if (arr[i] == arr[j]):
          visited[j] = True
          count += 1

     print(arr[i], count)

a = list(map(int, input("Enter numbers separated by space: ").split()))
n = len(a)
countFreq(a, n)
