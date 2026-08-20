'''
Given an integer array nums, sorted in ascending order (with distinct values) and a 
target value k. The array is rotated at some pivot point that is unknown. Find the index at which k is present and if 
k is not present return -1.
'''
def binarySearch(nums,k):
    low = 0
    high = len(nums)-1
    ans = -1

    while low<=high:
        mid = (low+high)//2

        if nums[mid]==k:
            ans = mid
            return ans

        if nums[low]==nums[mid]==nums[high]:
            low +=1
            high -=1
            continue
        
        if nums[low]<=nums[mid]:
            if (nums[low]<=k<nums[mid]):
                high = mid-1
            else:
                low = mid+1
        else:
            if(nums[mid]<k<=nums[high]):
                low = mid+1
            else:
                high = mid-1

    return ans


nums = [4, 4, 4, 4, 0, 1, 2]
k = 4
res = binarySearch(nums,k)
print(res)