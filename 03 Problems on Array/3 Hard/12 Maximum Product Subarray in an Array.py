'''
Given an integer array nums. Find the subarray with the largest product 
and return the product of the elements present in that subarray.
A subarray is a contiguous non-empty sequence of elements within an array.
'''
nums = [4, 5, 3, 7, 1, 2]
prod = {}
n =len(nums)
max_product = 0
current_product = 1
for i in range(n):
    current_product*=nums[i]

    if current_product>max_product:
        max_product = current_product

print(max_product)

nums = [-5, -1, -2]
prod = 1
max_prod = float("-inf")
for i in range(len(nums)):
    prod*=nums[i]
    if prod<0 and i!=len(nums)-1:
        if nums[i+1]>0:
            prod=1
    max_prod = max(max_prod,prod)

print(prod)