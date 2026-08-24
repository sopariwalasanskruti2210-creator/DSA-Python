"""
Given an array nums of n integers,
return true if the array nums is sorted in non-decreasing order or else false.
"""


def isSorted(nums):

    for i in range(len(nums)):

        # To check if array is sorted we use bubble sort if there is no swap happens
        # in an iteration that means array is already sorted
        # For example nums = [1,2,3,4,5]  so in first iteration no swap happens so we can conclude that array is sorted
        # If we give nums = [1,3,2,4,5] so here in first iteration 3>2 so swap(3,2) = (2,3) so swap happens therefore array is unsorted.
        for j in range(len(nums) - 1):
            if nums[j] >= nums[j + 1]:
                return False
    return True


nums = [1, 2, 3, 4, 5]
res = isSorted(nums)
print(res)
