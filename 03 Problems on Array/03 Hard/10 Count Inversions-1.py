"""
Given an integer array nums. Return the number of inversions in the array.
Two elements a[i] and a[j] form an inversion if a[i] > a[j] and i < j.
It indicates how close an array is to being sorted.
A sorted array has an inversion count of 0.
An array sorted in descending order has maximum inversion.
"""

nums = [2, 3, 7, 1, 3, 5]
count = 0
for i in range(len(nums)):
    for j in range(len(nums)):
        if nums[i] > nums[j] and i < j:
            count += 1
print(count)
