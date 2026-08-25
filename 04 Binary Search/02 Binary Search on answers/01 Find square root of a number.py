'''
Given a positive integer n. Find and return its square root. 
If n is not a perfect square, then return the floor value of sqrt(n).
'''

def squareRoot(n):
    
    # Square root of any num will max be num itself so it range will be 1 to n.
    low = 1
    high = n
    sqrt = 1
    
    # Edge case
    if n==0:
        return 0
    
    # Check if low and high crosses
    while low<=high:
        
        mid = (low+high)//2
        
        # Eliminate left half
        if mid*mid <= n:
            low = mid + 1
            
            # Store ans in sqrt
            sqrt = mid
            
        # Eliminiate right half
        else:
            high = mid - 1

    return sqrt

n = 108
res = squareRoot(n)
print(res)
