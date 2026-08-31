'''
Given an array nums of size n, which denotes the positions of stalls, and an integer k,
which denotes the number of aggressive cows, assign stalls to k cows such that the minimum distance between any two cows is the
maximum possible. Find the maximum possible minimum distance.
'''

# Calc the possible min distance between two cows
def countCows(stalls,mid):
    
    cnt = 1
    last = stalls[0]
    
    for i in range(1,len(stalls)):
        
        # Count the distance between current - last appended
        minDis = stalls[i] - last
        
        # Only append it if minDis is greater than or equal to mid else go to next iteration
        if minDis >= mid:
            last = stalls[i]
            
            # Update the cnt
            cnt += 1
            
            # If we put all the cows then just break cuz we don't need to go further that
            if cnt == cows:
                break
    
    return cnt


def minDistance(stalls,n,cows):
    
    low = 0
    high = stalls[-1] - stalls[0]
    ans = 0
    
    # Edge cases
    if cows > n:
        return -1
    
    if cows == 1:
        return 0
    
    # Start binary search
    while low <= high:
        
        mid = (low+high)//2
        
        totalnumOfcows = countCows(stalls,mid)
        
        # If the totalnumOfcows is greater than find for min possible dis which is max overall for that search in right half
        if totalnumOfcows >= cows :
            ans = mid
            low = mid + 1
            
        # Else search in left part
        else:
            high = mid - 1
            
    return ans


n = 5
cows = 3
stalls = [10, 1, 2, 7, 5]
stalls.sort()

res = minDistance(stalls,n,cows)
print(res)