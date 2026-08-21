'''
Given a sorted array nums and an integer x. Find the floor and ceil of x in nums. 
The floor of x is the largest element in the array which is smaller than or equal to x. 
The ceiling of x is the smallest element in the array greater than or equal to x. If no floor or ceil exists, output -1.
'''
# If target is present in the array,
# both Floor and Ceil can be the target itself.
def floor(nums,target):
    low = 0
    high = len(nums)-1
    ans = len(nums)

    # FLOOR: Largest element <= target
    while low<=high:
        mid = (low+high)//2
        if nums[mid]<=target:
            ans = nums[mid]
            low = mid+1
        else:
            high = mid-1

    return ans

def ceil(nums,target):
    low = 0
    high = len(nums)-1
    ans = len(nums)

    # CEIL: Smallest element >= target
    while low<=high:
        mid = (low+high)//2
        if nums[mid]>=target:
            ans = nums[mid]
            high = mid-1
        else:
            low = mid+1

    return ans

nums =[3, 4, 4, 7, 8, 10]
x= 5
f = floor(nums,x)
c = ceil(nums,x)
print(f"Floor:{f} Ceil:{c}")