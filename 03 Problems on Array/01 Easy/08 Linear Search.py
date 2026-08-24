"""
Given an array of integers nums and an integer target, find the smallest
index (0 based indexing) where the target appears in the array.
If the target is not found in the array, return -1
"""

nums = [2, 3, 4, 5, 3]
target = 3

for i in range(len(nums)):

    # If target is found return else check for element
    if nums[i] == target:
        ans = i
        break

    # If target is not found in any case return -1
    else:
        ans = -1
print(ans)
