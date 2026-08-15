'''
Given an array of integers nums and an integer target. Return the indices(0 - indexed) 
of two elements in nums such that they add up to target.
Each input will have exactly one solution, and the same element cannot be used twice. Return the answer in any order.
'''
nums = [1, 6, 0, 10, -3]
target = 7
prefix = {}
ans = []
for i in range(len(nums)):

  pre=target-nums[i]
  if pre in prefix:
    ans.append([prefix[pre],i])
    print(ans[0])
    break

  prefix[nums[i]]=i
