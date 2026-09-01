'''
You are given A painters and an array C of N integers where C[i] denotes the length of the ith board. 
Each painter takes B units of time to paint 1 unit of board. You must assign boards to painters such that:
Each painter paints only contiguous segments of boards.
No board can be split between painters.
The goal is to minimize the time to paint all boards.
Return the minimum time required to paint all boards modulo 10000003.
'''

def countPaint(paint,mid):
    
    cnt = 1
    total = 0
    
    for p in paint:
        
        if p + total <= mid:
            total += p
            
        else:
            cnt += 1
            total = p*time
            
    return cnt

def minTime(paint,time,painters) :
    
    low = max(paint)
    high = sum(paint)
    
    ans = 0
    
    while low <= high:
        
        mid = ((low + high)//2)
        
        totalPainters = countPaint(paint,mid)
        
        if totalPainters <= painters :
            ans = mid
            high = mid - 1
        else :
            low = mid + 1
            
    return ans*time

painters = 3
time = 2
paint = [5,10,30,20]

res = minTime(paint,time,painters)
print(res)