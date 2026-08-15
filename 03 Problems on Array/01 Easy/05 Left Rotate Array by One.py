'''
Given an integer array nums, rotate the array to the left by one.
Note: There is no need to return anything, just modify the given array.
'''
def rotateArr(nums):
  temp=nums[0]
  for ele in range(1,len(nums)):
    nums[ele-1]=nums[ele]
  nums[-1]=temp

  return nums

nums = [1,2,3,4,5,6]
rotateArr(nums)
print(nums)