"""
Given an array nums of size n and an integer k,
find the length of the longest sub-array that sums to k. If no such sub-array exists, return 0.
"""

nums = [2, 3, -2, 4, 1]
current_sum = 0
prefix = {}
maxLen = 0
k = 5

# For this case :
# i = 0 => sum = 2 => 2 - 5 = -3 not in prefix => prefix = {2 : 0}
# i = 1 => sum = 5 => sum == 5 => length = 1 + 1 = 2 => maxLen = max(0,2) = 2 => prefix = {2 : 0 , 5 : 1}
# i = 2 => sum = 3 => 3 - 5 = -2 not in prefix => prefix = {2 : 0 , 5 : 1 , 3 : 2}
# i = 3 => sum = 6 => 6 - 5 = 1 not in prefix => prefix = {2 : 0 , 5 : 1 , 3 : 2 , 6 : 3}
# i = 4 => sum = 10 => 10 - 5 = 5 in prefix => length = 4 - 1 = 3 => maxLen = max(2,3) = 3 => prefix = {2 : 0 , 5 : 1 , 3 : 2 , 6 : 3 , 10 : 4}
# i = 5 => sum = 11 => 11 - 5 = 6 in prefix => length = 5 - 3 = 2 => maxLen = max(3,2) = 3 => prefix = {2 : 0 , 5 : 1 , 3 : 2 , 6 : 3 , 10 : 4 , 11 : 5}
for i in range(len(nums)):

    # Update the sum
    current_sum += nums[i]

    # Check if the first x elements sum is equal to k
    if current_sum == k:
        maxLen = max(maxLen, i + 1)

    # Use reverse logic means for example the current num is 2 and
    # we need sum 5 so 2 + 3 = 5 so search for 3 in prefix If it is found than the elements between them sum is k.
    pre = current_sum - k
    if pre in prefix:
        length = i - prefix[pre]
        maxLen = max(maxLen, length)

    # To get max length use only first occurrence of the element
    # for example : nums = [1,2,-1,1] k = 3
    # So prefix sum = [1,3,2,3] so here 3 repeat two times now if count length so for
    # first 3 length = 2 for second length = 3 so as we need max length we store only first occurrence
    if current_sum not in prefix:
        prefix[current_sum] = i

print(maxLen)
print(prefix)
