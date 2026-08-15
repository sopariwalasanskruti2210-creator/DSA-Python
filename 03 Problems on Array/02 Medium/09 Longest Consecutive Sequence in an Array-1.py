'''
Given an array nums of n integers.
Return the length of the longest sequence of consecutive integers. 
The integers in this sequence can appear in any order.
'''
nums = [100, 4, 200, 1, 3, 2]
nums.sort()
lastSmaller = nums[0]
count = 1
maxLen = 0
print(nums)
for i in range(1,len(nums)):
  if nums[i]==(lastSmaller+1):
    count+=1
    lastSmaller = nums[i]
    maxLen=max(maxLen,count)
  else:
    count = 1
    lastSmaller = nums[i]

print(maxLen)