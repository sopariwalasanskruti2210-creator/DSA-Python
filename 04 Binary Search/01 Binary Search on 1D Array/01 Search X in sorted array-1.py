"""
Given a sorted array of integers nums with 0-based indexing, find the index of a specified target integer.
 If the target is found in the array, return its index. If the target is not found, return -1.
"""


# Using Loop
def binarySearch(nums, n, target):
    low = 0
    high = n - 1
    while low <= high:
        mid = (low + high) // 2
        if nums[mid] == target:
            return mid
        elif target > nums[mid]:
            low = mid + 1
        else:
            high = mid - 1
    return -1


nums = [3, 4, 6, 7, 9, 12, 16, 17]
target = 12
res = binarySearch(nums, len(nums), target)
print(res)
