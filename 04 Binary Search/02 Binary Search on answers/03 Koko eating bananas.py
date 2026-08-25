'''
A monkey is given n piles of bananas, where the 'ith' pile has nums[i] bananas. 
An integer h represents the total time in hours to eat all the bananas.
Each hour, the monkey chooses a non-empty pile of bananas and eats k bananas. If the pile contains fewer than k bananas, 
the monkey eats all the bananas in that pile and does not consume any more bananas in that hour.
Determine the minimum number of bananas the monkey must eat per hour to finish all the bananas within h hours.
'''

import math

# k = banana/hr
# The k should be in the range of h
# Here check for each hour and calc total hour and if it is the min time then store it in ans

# Check total time for to eat all banana
def totalHours(nums,mid):
    
    totalHour = 0
    for i in range(len(nums)):
        totalHour+=math.ceil(nums[i]/mid)
        
    return totalHour

def minbanana(nums,h):
    
    low = 1
    high = max(nums)
    ans = 0
    
    # Start binary search
    while low <= high : 
        
        # Compute minimum
        mid = (low+high)//2
        
        reqTime = totalHours(nums,mid)
        
        # Check the total time is under h or not
        if reqTime <= h:
            
            ans = mid
            # Check for the min hrs in left half
            high = mid-1
            
        else:
            
            # Check in right half
            low = mid+1
            
    return ans
    
    
    
n = 4
nums = [3, 7, 6, 11]
h = 8
res = minbanana(nums,h)
print(res)