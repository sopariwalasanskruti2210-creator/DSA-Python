'''
Given n roses and an array nums where nums[i] denotes that the 'ith' rose will bloom on the nums[i]th day, 
only adjacent bloomed roses can be picked to make a bouquet. Exactly k adjacent bloomed roses are required to make a single bouquet. 
Find the minimum number of days required to make at least m bouquets, each containing k roses. Return -1 if it is not possible.
'''

# Check the num of flower bloomed
def bloomedCount(nums,mid,m,k):
    
    cnt = 0
    minCount = 0
    for i in range(len(nums)):
        
        if nums[i]<=mid:
            cnt += 1
            
            if cnt == k:
                minCount+=1
                cnt = 0
        else:
            cnt = 0
            
    return minCount 

def bouquets(nums,m,n,k):
    
    low = min(nums)
    high = max(nums)
    ans = -1
    
    if n<m*k:
        return -1
    
    # Start binary search
    while low<=high: 
        
        mid = (low+high)//2
        
        # Check the num of flowers bloomed on midth day
        bloomed = bloomedCount(nums,mid,m,k)
        
        if bloomed>=m:
            ans = mid
            # Check on left half for minimum value
            high = mid - 1
            
        else:
            # If it is higher check on right half
            low = mid + 1

    return ans

nums = [7,7,7,7,12,7,7]
m = 2
k = 3
n = 7
res = bouquets(nums,m,n,k)
print(res)