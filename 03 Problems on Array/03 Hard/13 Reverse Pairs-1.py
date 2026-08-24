"""
Given an integer array nums. Return the number of reverse pairs in the array.
An index pair (i, j) is called a reverse pair if:
0 <= i < j < nums.length
nums[i] > 2 * nums[j]
"""

nums = [5, 4, 4, 3, 3]
count = 0
for i in range(len(nums)):
    for j in range(i, len(nums)):
        if i < j and nums[i] > 2 * nums[j]:
            count += 1
print(count)
