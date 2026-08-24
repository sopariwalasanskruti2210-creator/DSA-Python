"""
Given an integer array nums of even length consisting of an equal number of positive and negative integers.
Return the answer array in such a way that the given conditions are met:
Every consecutive pair of integers have opposite signs.
For all integers with the same sign, the order in which they were present in nums is preserved.
The rearranged array begins with a positive integer.
"""

nums = [1, -1, -2, 2, 3]
ans = [0] * len(nums)
pos_index = 0
neg_index = 1

# As her we need one pos one neg as ans
# As element is pos it will be one odd index and neg element will be on even index
for i in range(len(nums)):

    # If element is pos then append it on odd index and increase it by 2 as next pos index too will be on odd index
    if nums[i] > 0:
        ans[pos_index] = nums[i]
        pos_index += 2

    # If element is neg then append it on even index and increase it by 2 as next neg index too will be on even index
    else:
        ans[neg_index] = nums[i]
        neg_index += 2

print(ans)
