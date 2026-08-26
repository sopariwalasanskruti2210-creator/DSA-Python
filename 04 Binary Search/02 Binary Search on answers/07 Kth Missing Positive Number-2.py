'''
Given a sorted array of unique positive integers arr, your task is to return the
kᵗʰ missing positive number that is not present in arr.
The array is guaranteed to be strictly increasing, and the missing numbers are 
those positive integers that do not appear in arr but would appear in a full sequence starting from 1.
'''

# Optimal Approach

def missingNum(arr,k):
    
    if k < min(arr) :
        return k
    
    low = 0
    high = len(arr)-1
    
    # Start binary search
    while low <= high:
        
        # Find mid
        mid = (low+high)//2
        
        # To find missing num = current_num - num which actually should be present at that index
        # as we start it from 1 so the num present at each index will be index + 1
        missing = arr[mid] - (mid+1)
        
        # Search in left half
        if missing >= k :
            high = mid - 1
            
        # Search in right half
        else : 
            low = mid + 1
            
    # To calc final missing num at kth pos :
    # So at the high we point to the missing number which is less than k in that array
    # like here arr[high] = 7 at the position 3 nums are already missing 
    # so the final kth missing num will be = nums[high] + more
    # more = k - (nums[high] - high - 1) = k - missing
    # final kth missing num = arr[high] + more = arr[high] + k - (nums[high] - high - 1) = k + high + 1
    return k + high + 1
    
arr = [3, 5, 7, 10]
k = 6
res = missingNum(arr,k)
print(res)


