'''
Given an array arr of integers. A peak element is defined as an element greater than both of its neighbors.
Formally, if arr[i] is the peak element, arr[i - 1] < arr[i] and arr[i + 1] < arr[i].
Find the index(0-based) of a peak element in the array. If there are multiple peak numbers, return the index of any peak number.
Note:
As there can be many peak values, "true" is given as output if the returned index is a peak number, otherwise the returned value of index.
'''
def peakElement(nums):
    n = len(nums)
    low = 1
    high = n-2

    #Edge Cases
    if n==1:
        return 0

    if nums[0]>nums[1]:
        return 0

    if nums[n-1]>nums[n-2]:
        return n-1

    while low<=high:
        mid = (low+high)//2

        #Check if mid is peak
        if nums[mid]>nums[mid-1] and nums[mid]>nums[mid+1]:
            return mid

        # check if we are going uphill or downhill
        # If we are going downhill search left(or eliminate right) and 
        # if we are going uphill search right(or eliminate left)
        if nums[mid]<nums[mid+1]:
            low = mid+1
        else:
            high = mid-1

    return -1

nums = [1, 2, 1, 3, 5, 6, 4]
res = peakElement(nums)
print(res)