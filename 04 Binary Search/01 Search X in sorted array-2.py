'''
Given a sorted array of integers nums with 0-based indexing, find the index of a specified target integer.
 If the target is found in the array, return its index. If the target is not found, return -1.
'''

# Using Recursive Call
def binarySearch(nums,low,high):
    if low>high:
            return -1

    mid = (low+high)//2
    if nums[mid]==target:
        return mid
    elif target>nums[mid]:
        return binarySearch(nums,mid+1,high)
    else:
        return binarySearch(nums,low,mid-1)
    

nums = [3,4,6,7,9,12,16,17]
target = 6
res = binarySearch(nums,0,len(nums)-1)
print(res)