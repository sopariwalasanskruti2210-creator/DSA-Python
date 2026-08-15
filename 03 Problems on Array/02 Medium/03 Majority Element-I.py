'''
Given an integer array nums of size n, return the majority element of the array.
The majority element of an array is an element that appears more than n/2 times in the array. 
The array is guaranteed to have a majority element.
'''
count = {}
nums = [7, 0, 0, 1, 7, 7, 2, 7, 7]
n=len(nums)
for i in nums:
  if i not in count:
    count[nums[i]]=1
  else:
    count[nums[i]]+=1

ans = [key for key,value in count.items() if value>(n/2)]
print(ans[0])