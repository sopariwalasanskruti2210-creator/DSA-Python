'''
Given a sorted array of nums consisting of distinct integers and a target value, 
return the index if the target is found. If not, return the index where it would be if it were inserted in order.
'''
def binarySearch(nums,target):
    low = 0
    high = len(nums)-1
    ans = len(nums)

    while low<=high:
        mid = (low+high)//2
        if nums[mid]>=target:
            ans = mid
            high = mid-1
        else:
            low = mid+1

    return ans


nums = [1, 3, 5, 6]
target = 2
res = binarySearch(nums,target)
print(res)