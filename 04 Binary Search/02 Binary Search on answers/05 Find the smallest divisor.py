'''
Given an array of integers nums and an integer limit as the threshold value, find the smallest positive integer 
divisor such that upon dividing all the elements 
of the array by this divisor, the sum of the division results is less than or equal to the threshold value.
After dividing each element by the chosen divisor, take the ceiling of the result (i.e., round up to the next whole number).
'''

def divisorSum(nums,mid):
    
    div_sum = 0
    for i in range(len(nums)):
        div_sum += (nums[i]+mid-1)//mid
        
    return div_sum

def divisor(nums,limit):
    
    low = 1
    high = max(nums)
    ans = -1
    
    # Start binary search
    while low <= high:
        
        mid = (low+high)//2
        
        div = divisorSum(nums,mid)
        
        # Check if it exceeds limit or not
        if div <= limit:
            ans = mid
            # Check for minimum in left half
            high = mid - 1
        else:
            # Search in right half
            low = mid + 1
            
    return ans

nums = [8,4,2,3]
limit = 4
res = divisor(nums,limit)
print(res)
