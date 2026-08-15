'''
Given an integer array nums. Find the subarray with the largest product 
and return the product of the elements present in that subarray.
A subarray is a contiguous non-empty sequence of elements within an array.
'''
nums = [4, 5, 3, 7, 1, 2]
n =len(nums)
max_product = float("-inf")
pre,suff = 1,1
for i in range(n):

    if pre==0:
        pre=1

    if suff==0:
        suff=1

    pre= pre*nums[i]
    suff = suff*nums[n-i-1]
    max_product = max(max_product,pre,suff)

print(max_product)


