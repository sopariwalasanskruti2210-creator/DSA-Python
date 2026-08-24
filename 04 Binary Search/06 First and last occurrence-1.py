"""
Given an array of integers nums sorted in non-decreasing order,
find the starting and ending position of a given target value.
If the target is not found in the array, return [-1, -1].
"""


def firstOcurrence(nums, target):
    low = 0
    high = len(nums) - 1
    ans = len(nums)

    # When target is found, don't return immediately.
    # Store mid as a possible answer and search left
    # because another occurrence may exist at a smaller index.
    while low <= high:
        mid = (low + high) // 2

        if nums[mid] >= target:
            ans = mid
            high = mid - 1
        else:
            low = mid + 1

    return ans


def lastOccurrance(nums, target):
    low = 0
    high = len(nums) - 1
    ans = len(nums)

    # When elemnet greater than target is found, don't return immediately.
    # Store mid as a possible answer and search right
    # because another occurrence may exist at a higher index.
    while low <= high:
        mid = (low + high) // 2

        if nums[mid] > target:
            ans = mid
            high = mid - 1
        else:
            low = mid + 1

    return ans - 1


nums = [5, 7, 7, 8, 8, 10]
target = 8
fs = firstOcurrence(nums, target)
ls = lastOccurrance(nums, target)
if fs == len(nums) or nums[fs] != target:
    print("[-1.-1]")
else:
    print(f"[{fs},{ls}]")
