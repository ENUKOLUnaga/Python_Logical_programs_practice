#Finding duplicate values
nums = list(map(int, input("Enter numbers: ").split()))
duplicates = []
for i in range(len(nums)):
    for j in range(i + 1, len(nums)):
        if nums[i] == nums[j] and nums[i] not in duplicates:
            duplicates.append(nums[i])
print("Duplicate elements:", duplicates)