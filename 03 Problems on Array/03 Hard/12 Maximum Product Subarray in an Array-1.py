'''
Given an integer array nums. Find the subarray with the largest product 
and return the product of the elements present in that subarray.
A subarray is a contiguous non-empty sequence of elements within an array.
'''
nums = [4, 5, 3, 7, 1, 2]
prod = {}
n =len(nums)
max_product = float("-inf")
for i in range(n):
    prod = 1
    for j in range(i,n):
        prod*=nums[j]
        max_product=max(max_product,prod)

print(max_product)


