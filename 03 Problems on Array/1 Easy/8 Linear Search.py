'''
Given an array of integers nums and an integer target, find the smallest 
index (0 based indexing) where the target appears in the array. 
If the target is not found in the array, return -1
'''
nums = [2, 3, 4, 5, 3]
target = 3
for i in range(len(nums)):
    if nums[i]==target:
        ans = i
        break
    else:
        ans = -1
print(ans)