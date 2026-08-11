'''
Given an array nums of size n and an integer k, 
find the length of the longest sub-array that sums to k. If no such sub-array exists, return 0.
'''
nums=[2,3,-2,4,1]
current_sum=0
prefix={}
maxLen=0
k=5
for i in range(len(nums)):
  current_sum+=nums[i]

  if current_sum==k:
    maxLen=max(maxLen,i+1)

  pre=current_sum-k
  if pre in prefix:
    length=i-prefix[pre]
    maxLen=max(maxLen,length)

  if current_sum not in prefix:
    prefix[current_sum]=i
print(maxLen)
print(prefix)