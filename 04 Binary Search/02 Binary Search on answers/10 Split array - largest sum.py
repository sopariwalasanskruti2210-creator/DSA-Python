'''
Given an integer array a of size n and an integer k. Split the array a into k non-empty subarrays such that the largest sum of any 
subarray is minimized. Return the minimized largest sum of the split.
'''

# Count the num of array for give distance
def numOfarr(nums,mid) :
    
    cnt = 1
    total = 0
    
    for num in nums :
        
        # If it is lesser than or equal then add it to total
        if total + num <= mid :
            total += num
            
        # Else start new part
        else : 
            total = num
            cnt += 1
            
    return cnt

def largetSum(nums,k) :
    
    low = max(nums)
    high = sum(nums)
    ans = 0
    
    # Edge cases
    if len(nums) < k:
        return -1
    
    if len(nums) == 0:
        return 0
    
    if len(nums) == k:
        return low
    
    # Start binary search
    while low <= high :
        
        mid = (low + high)//2
        
        totalArray = numOfarr(nums,mid)
        
        # Search in left part for more lower min
        if totalArray <= k :
            ans = mid
            high = mid - 1
            
        # Else search in right part
        else :
            low = mid + 1
            
    return ans

nums = [3,5,1,6]
k = 3

res = largetSum(nums,k)
print(res)