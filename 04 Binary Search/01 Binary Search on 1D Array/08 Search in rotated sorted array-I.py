"""
Given an integer array nums, sorted in ascending order (with distinct values) and a
target value k. The array is rotated at some pivot point that is unknown. Find the index at which k is present and if
k is not present return -1.
"""


def binarySearch(nums, k):
    low = 0
    high = len(nums) - 1
    ans = -1

    while low <= high:
        mid = (low + high) // 2

        if nums[mid] == k:
            ans = mid
            return ans

        # If one half is sorted, check whether target lies within
        # the range of that sorted half.
        # If yes -> search inside that half.
        # If no  -> eliminate it and search the other half.
        if nums[low] <= nums[mid]:
            if nums[low] <= k < nums[mid]:
                high = mid - 1
            else:
                low = mid + 1
        else:
            if nums[mid] < k <= nums[high]:
                low = mid + 1
            else:
                high = mid - 1

    return ans


nums = [4, 5, 6, 7, 0, 1, 2]
k = 0
res = binarySearch(nums, k)
print(res)
