"""
Given an integer array nums. Return all triplets such that:
i != j, i != k, and j != k
nums[i] + nums[j] + nums[k] == 0.
Notice that the solution set must not contain duplicate triplets. One element can be a part of multiple triplets.
The output and the triplets can be returned in any order.
"""

# Optimal Approach
nums = [-1, 0, 1, 2, -1, -4]
nums.sort()
ans = []
n = len(nums)
for i in range(n):

    if i > 0 and nums[i] == nums[i - 1]:
        continue

    left = i + 1
    right = n - 1

    while left < right:

        total = nums[i] + nums[left] + nums[right]

        if total == 0:
            ans.append([nums[i], nums[left], nums[right]])
            left += 1
            right -= 1

            while left < right and nums[left] == nums[left - 1]:
                left += 1
            while left < right and nums[right] == nums[right + 1]:
                right -= 1

        elif total < 0:
            left += 1
        else:
            right -= 1

for item in ans:
    print(item, end=" ")
