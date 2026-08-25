"""
Given a sorted array of nums and an integer x, write a program to find the lower bound of x.
The lower bound algorithm finds the first and smallest index in a sorted array where the value at that index is
greater than or equal to a given key i.e. x.
If no such index is found, return the size of the array.
"""


def binarySearch(nums, target):
    low = 0
    high = len(nums) - 1
    ans = len(nums)

    # Lower Bound : where element is greater than or equal to target
    while low <= high:
        mid = (low + high) // 2
        if nums[mid] >= target:
            ans = mid
            high = mid - 1
        else:
            low = mid + 1

    return ans


nums = [3, 4, 6, 7, 9, 12, 16, 17]
target = 15
res = binarySearch(nums, target)
print(res)
