'''
Given an array of nums of n integers. 
Every integer in the array appears twice except one integer. Find the number that appeared once in the array.
'''
nums = [1, 2, 2, 4, 3, 1, 4]
hash=[0]*len(nums)
for i in nums:
  hash[i]+=1

print(hash.index(1))