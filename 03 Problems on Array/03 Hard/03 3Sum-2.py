'''
Given an integer array nums. Return all triplets such that:
i != j, i != k, and j != k
nums[i] + nums[j] + nums[k] == 0.
Notice that the solution set must not contain duplicate triplets. One element can be a part of multiple triplets. 
The output and the triplets can be returned in any order.
'''
# Better Approach
nums = [-1,0,1,2,-1,-4]
ans = set()
for i in range(len(nums)):
  hashmap = set()
  for j in range(i+1,len(nums)):
    third = -(nums[i]+nums[j])

    if third in hashmap:
      triplet = tuple(sorted([nums[i],nums[j],third]))
      ans.add(triplet)

    hashmap.add(nums[j])

for a in ans:
  print(list(a),end="")