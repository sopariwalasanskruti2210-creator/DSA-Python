"""
Given an array of integers nums and an integer k,
return the total number of subarrays whose XOR equals to k.
"""

nums = [4, 2, 2, 6, 4]
k = 6
n = len(nums)
current_XOR = 0
count = 0
freq = {}
for i in range(n):

    current_XOR ^= nums[i]
    if current_XOR == k:
        count += 1

    target = current_XOR ^ k
    if target in freq:
        count += freq[target]

    if current_XOR not in freq:
        freq[current_XOR] = 1
    else:
        freq[current_XOR] += 1

print(count)
