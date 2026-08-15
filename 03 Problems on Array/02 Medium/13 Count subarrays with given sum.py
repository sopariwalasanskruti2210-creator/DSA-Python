'''
Given an array of integers nums and an integer k, return the total number of subarrays whose sum equals to k.
'''
nums = [1,2,3]
k = 3
prefix = {}
current_sum = 0
count = 0
for i in range(len(nums)):
  current_sum+=nums[i]

  if current_sum==k:
    count+=1

  pre = current_sum-k
  if pre in prefix:
    count+=1

  prefix[current_sum]=i
  print(current_sum,prefix)

print(count)