"""
Given an integer array nums, return a list of all the leaders in the array.
A leader in an array is an element whose value is strictly greater than all elements to its right in
the given array. The rightmost element is always a leader. The elements in the leader array must appear in the order 3
they appear in the nums
"""

nums = [1, 2, 5, 3, 1, 2]
ans = []
max_val = nums[-1]

# As there is no element in right of last so it will always be a leader
ans.append(nums[-1])

# Here as we don't know the next element so instead of traversing from left to right we go right to left
# In which if we greater element than current one so we store it as leader
for i in range(len(nums) - 1, -1, -1):

    # If nums[i] is greater than max_val then nums[i] is the leader
    # update max_val
    if nums[i] > max_val:
        ans.append(nums[i])
        max_val = nums[i]

# Reverse the ans as we need it in sequence
ans.reverse()

# Example: nums = [1,2,5,3,1,2]
#
# Start from the right because the last element is always a leader.
# max_val = 2 → leader
#
# Moving left:
# 1 < 2 → not a leader
# 3 > 2 → leader, max_val = 3
# 5 > 3 → leader, max_val = 5
#
# ans = [2,3,5], but we found them from right to left,
# so reverse it to get: [5,3,2]
print(ans)
