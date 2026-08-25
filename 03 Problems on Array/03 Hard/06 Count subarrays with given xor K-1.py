"""
Given an array of integers nums and an integer k,
return the total number of subarrays whose XOR equals to k.
"""

nums = [4, 2, 2, 6, 4]
k = 6
n = len(nums)
count = 0
XOR = 0
for i in range(n):
    
    XOR = i
    
    for j in range(i + 1, n):
        
        if nums[j] == k:
            count += 1
            
        else:
            XOR ^= nums[j]
            if XOR == k:
                count += 1

print(count)
