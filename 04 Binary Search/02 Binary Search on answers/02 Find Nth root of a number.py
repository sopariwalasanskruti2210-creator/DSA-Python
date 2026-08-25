'''
Given two numbers N and M, find the Nth root of M. The Nth root of a number M is defined as a number X 
such that when X is raised to the power of N, it equals M. If the Nth root is not an integer, return -1.
'''

def nthRoot(n,m):
    
    low = 1
    high = m
    
    # Edge case
    if n==0 and m==0:
        return 0
    
    # start binary search
    while low<=high:
        
        # Find mid
        mid = (low+high)//2
        
        ans = 1
        # Calculate mid^n
        for i in range(n):
            ans *= mid
            if ans>m:
                break
            
        # If ans is found retrun 
        if ans==m:
            ans = mid
            return ans
        # Search right half
        elif ans<m:
            low = mid+1
        # Search left half
        else:
            high = mid-1
            
    return -1
            
        

n = 4
m = 69
res = nthRoot(n,m)
print(res)
