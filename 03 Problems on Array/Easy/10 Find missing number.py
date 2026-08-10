'''
Given an integer array of size n containing distinct values in the 
range from 0 to n (inclusive), return the only number missing from the array within this range.
'''
nums = [0, 2, 3, 1, 4]
n = len(nums)+1
for i in range(n):
  found = False
  for j in range(n-1):
    if(nums[j]==i):
      found=True
      break

  if not found:
    print(i)