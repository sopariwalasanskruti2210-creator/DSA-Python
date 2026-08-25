"""
Given an array nums sorted in non-decreasing order. Every number in the array except one appears twice.
Find the single number in the array.
"""


def singleElement(nums):
    n = len(nums)
    low = 1
    high = n - 2

    # Edge cases
    if len(nums) == 1:
        return nums[0]

    if nums[0] != nums[1]:
        return nums[0]

    if nums[n - 1] != nums[n - 2]:
        return nums[n - 1]

    while low <= high:
        mid = (low + high) // 2

        # Single Element Found
        if nums[mid] != nums[mid + 1] and nums[mid] != nums[mid - 1]:
            return nums[mid]

        # If not then check for both half as for left half the pair if mid is odd the pair is (odd,odd-1) for even
        # it is (even,even+1) same as for right it is reversed
        # (even,odd)->left half
        # (odd,even)->right half
        if (mid % 2 != 0 and nums[mid] == nums[mid - 1]) or (
            mid % 2 == 0 and nums[mid] == nums[mid + 1]
        ):
            low = mid + 1
        else:
            high = mid - 1

    return -1


nums = [1, 1, 2, 2, 3, 3, 4, 5, 5, 6, 6]
res = singleElement(nums)
print(res)
