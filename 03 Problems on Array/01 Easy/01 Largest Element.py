'''
Given an array of integers nums, return the value of the largest element in the array
'''
nums= [1,5,42,11,56]
largest = nums[0]
for i in range(len(nums)):
    if nums[i]>largest:
        largest = nums[i]

print(largest)