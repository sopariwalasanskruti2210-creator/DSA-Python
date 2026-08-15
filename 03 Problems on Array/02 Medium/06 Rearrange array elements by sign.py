'''
Given an integer array nums of even length consisting of an equal number of positive and negative integers.
Return the answer array in such a way that the given conditions are met:
Every consecutive pair of integers have opposite signs.
For all integers with the same sign, the order in which they were present in nums is preserved.
The rearranged array begins with a positive integer.
'''
nums=[1, -1, -2, 2, 3]
ans=[0]*len(nums)
pos_index=0
neg_index=1
for i in range(len(nums)):
  if nums[i]>0:
    ans[pos_index]=nums[i]
    pos_index+=2
  else:
    ans[neg_index]=nums[i]
    neg_index+=2

print(ans)