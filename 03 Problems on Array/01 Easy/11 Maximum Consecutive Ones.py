'''
Given a binary array nums, return the maximum number of consecutive 1s in the array.
A binary array is an array that contains only 0s and 1s.
'''
nums = [1, 1, 0, 0, 1, 1, 1, 0]
count = 0
max_count=0
for i in range(len(nums)):
  if(nums[i]==1):
    count+=1
    max_count=max(count,max_count)
  else:
    count=0

print(max_count)