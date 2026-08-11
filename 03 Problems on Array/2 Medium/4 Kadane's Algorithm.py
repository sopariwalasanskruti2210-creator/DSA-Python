'''
Given an integer array nums, find the subarray with the largest sum and return the sum of the 
elements present in that subarray.
A subarray is a contiguous non-empty sequence of elements within an array.
'''
nums = [-2,1,-3,4,-1,2,1,-5,4]
sum = 0
max_sum = float("-inf")
i=0
while i<len(nums):

  sum+=nums[i]

  if sum>max_sum:
    max_sum=sum
    end=i

  if sum<0:
    sum=0
    start=i+1

  i+=1

print(max_sum)
ans = []
for i in range(start,end+1):
  ans.append(nums[i])

print(ans)