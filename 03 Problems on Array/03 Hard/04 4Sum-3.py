'''
Given an integer array nums and an integer target. Return all quadruplets [nums[a], nums[b], nums[c], nums[d]] such that:
a, b, c, d are all distinct valid indices of nums.
nums[a] + nums[b] + nums[c] + nums[d] == target.
Notice that the solution set must not contain duplicate quadruplets. One element can be a part of multiple quadruplets. 
The output and the quadruplets can be returned in any order.
'''
# Optimise
nums = [1, -2, 3, 5, 7, 9]
target = 7
nums.sort()
ans = []
n = len(nums)
for i in range(n):

  if i>0 and nums[i]==nums[i-1]:
    continue

  for j in range(i+1,n):
    if j>i+1 and nums[j]==nums[j-1]:
      continue

    left = j+1
    right = n-1

    while left<right:
      total = nums[i]+nums[j]+nums[left]+nums[right]

      if total==target:
        ans.append([nums[i],nums[j],nums[left],nums[right]])
        left+=1
        right-=1

        while left<right and nums[left]==nums[left-1]:
          left+=1
        while left<right and nums[right]==nums[right+1]:
          right-=1

      elif total<target:
        left+=1
      else:
        right-=1

print(ans)