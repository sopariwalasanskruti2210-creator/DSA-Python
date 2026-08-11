'''
Given an array nums of size n and an integer k, 
find the length of the longest sub-array that sums to k. If no such sub-array exists, return 0.
'''
nums = [10, 5, 2, 7, 1, 9]
k=15
left = 0
right = 0
n=len(nums)
max_len=0
sum=nums[0]
while right<n:
  while left<=right and sum>k:
    sum-=nums[left]
    left+=1

  if sum==k:
    max_len=max(max_len,right-left+1)

  right+=1
  if right<n:
    sum+=nums[right]

print(max_len)