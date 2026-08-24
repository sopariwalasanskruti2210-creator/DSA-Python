"""
You are given an integer array arr of size n which contains both positive and negative integers.
Your task is to find the length of the longest contiguous subarray with sum equal to 0.
Return the length of such a subarray. If no such subarray exists, return 0.
"""

arr = [15, -2, 2, -8, 1, 7, 10, 23]
prefix = {}
current_sum = 0
maxLen = 0
for i in range(len(arr)):
    current_sum += arr[i]

    if current_sum == 0:
        maxLen = max(maxLen, i + 1)

    if current_sum in prefix:
        maxLen = max(maxLen, i - prefix[current_sum])

    if current_sum not in prefix:
        prefix[current_sum] = i

print(prefix)
print(maxLen)
