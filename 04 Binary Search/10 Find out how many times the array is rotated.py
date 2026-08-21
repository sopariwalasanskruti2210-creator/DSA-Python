'''
Given an integer array nums of size n, sorted in ascending order with distinct values. 
The array has been right rotated an unknown number of times, between 0 and n-1 (including). 
Determine the number of rotations performed on the array.
'''
def numofRotattion(nums):
    low = 0
    high = len(nums)-1

    while low<high:
        mid = (low+high)//2

        # Find minimum of array that index is the num of times array is rotated 
        if nums[mid]>nums[high]:
            low = mid+1
        else:
            high = mid

    return low

nums = [4, 5, 6, 7, 0, 1, 2, 3]
res = numofRotattion(nums)
print(res)