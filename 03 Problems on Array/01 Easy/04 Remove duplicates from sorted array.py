"""
Given an integer array nums sorted in non-decreasing order, remove all duplicates in-place so that each unique element
appears only once.
Return the number of unique elements in the array.
If the number of unique elements be k, then,
Change the array nums such that the first k elements of nums contain the unique values in the order that they were
present originally.
The remaining elements, as well as the size of the array does not matter in terms of correctness.
The driver code will assess correctness by printing and checking only the first k elements of the modified array.
An array sorted in non-decreasing order is an array where every element to the right of an element is
either equal to or greater in value than that element.
"""

nums = [0, 0, 3, 3, 5, 6]
ans = [nums[0]]
k = 1

for ele in range(1, len(nums)):

    # As array is sorted we check it's previos element we it is same ,
    # if it is same as previos then it is duplicate as here we start from index 1
    if nums[ele] != nums[ele - 1]:
        ans.append(nums[ele])
        k += 1

print(k)
