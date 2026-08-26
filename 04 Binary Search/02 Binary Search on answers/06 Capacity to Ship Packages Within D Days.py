'''
You are given an array weights where weights[i] represents the weight of the i-th package on a conveyor belt. 
All the packages must be shipped in the order given from one port to another within days days.
Each day, the ship can carry a contiguous sequence of packages, as long as the total weight does not exceed its maximum capacity.
Your task is to find the minimum possible capacity of the ship so that all packages can be shipped within the given number of days.
'''

def totalDays(weights,mid):
    
    # Init currentLoad with 0
    currentLoad = 0
    
    # Init cnt with 1 as it should count last day too
    cnt = 1
    
    for w in weights:
        
        # Check if it exceeds max capacity
        if currentLoad + w > mid:
            cnt += 1
            
            # if it exceeds max capacity then start with new weight
            currentLoad = w
        else:
            
            # else add it into current load
            currentLoad += w
            
    return cnt
            
            

def minCapacity(weights,days):
    
    low = max(weights)
    high = sum(weights)
    ans = 0
    
    # Start binary search 
    while low <= high:
        
        mid = (low+high)//2
        
        # Count the total num of days for each mid value
        totalDay = totalDays(weights,mid)
        
        # Find for the minimum days
        if totalDay <= days:
            ans = mid
            high = mid - 1
        else:
            low = mid + 1
            
    return ans
        

weights = [3,2,2,4,1,4]
days = 3
res = minCapacity(weights,days)
print(res)