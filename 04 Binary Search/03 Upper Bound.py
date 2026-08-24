"""
Upper Bound
Given a sorted array of nums and an integer x, write a program to find the upper bound of x.
The upper bound of x is defined as the smallest index i such that nums[i] > x.
If no such index is found, return the size of the array.
"""


def binarySearch(nums, target):
    low = 0
    high = len(nums) - 1
    ans = len(nums)

    # Upper Bound : where element is greater than target
    while low <= high:
        mid = (low + high) // 2
        if nums[mid] > target:
            ans = mid
            high = mid - 1
        else:
            low = mid + 1

    return ans


nums = [3, 4, 6, 7, 9, 12, 16, 17]
target = 8
res = binarySearch(nums, target)
print(res)
