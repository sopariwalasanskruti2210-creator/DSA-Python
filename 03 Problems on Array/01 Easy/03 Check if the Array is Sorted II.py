'''
Given an array nums of n integers, 
return true if the array nums is sorted in non-decreasing order or else false.
'''
def isSorted(nums):
    for i in range(len(nums)):
        for j in range(len(nums)-1):
            if(nums[j]>=nums[j+1]):
                return False
    return True

nums = [1,2,3,4,5]
res = isSorted(nums)
print(res)