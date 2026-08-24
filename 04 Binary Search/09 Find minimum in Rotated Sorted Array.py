"""
Given an integer array nums of size N, sorted in ascending order with distinct values, and then rotated an unknown
of times (between 1 and N), find the minimum element in the array.
"""


def minimum(nums):
    low = 0
    high = len(nums) - 1

    while low <= high:
        mid = (low + high) // 2

        # If mid is greater than high, minimum must be on the right
        if nums[mid] > nums[high]:
            low = mid + 1

        # Otherwise, minimum is at mid or somewhere on the left
        else:
            high = mid - 1

    return nums[low]


nums = [3, 4, 5, 1, 2]
res = minimum(nums)
print(res)
