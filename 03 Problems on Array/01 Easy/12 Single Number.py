"""
Given an array of nums of n integers.
Every integer in the array appears twice except one integer. Find the number that appeared once in the array.
"""

nums = [1, 2, 2, 4, 3, 1, 4]
hash = [0] * len(nums)

# Use Hashmap to count num of occurrence of element
# Store it as element : count => nums[1] = 2
for i in nums:
    hash[i] += 1

# Return the element whose count is one
print(hash.index(1))
