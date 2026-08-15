'''
Given an integer array nums, move all the 0's to the end of the array. 
The relative order of the other elements must remain the same.
This must be done in place, without making a copy of the array.
'''
nums = [1,2,0,0,3,4,5]
left = 0
for right in range(len(nums)):
    if nums[right] != 0:
        nums[left], nums[right] = nums[right], nums[left]
        left += 1
print(nums)