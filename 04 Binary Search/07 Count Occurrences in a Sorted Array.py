'''
You are given a sorted array of integers arr and an integer target. Your task is to determine how many times target appears in arr.
Return the count of occurrences of target in the array.
'''
def lowerBound(arr,target):
    low = 0 
    high = len(arr)-1
    ans = 0

    while low<=high:
        mid = (low+high)//2

        if arr[mid]>=target:
            ans = mid
            high = mid-1
        else:
            low = mid+1

    return ans

def upperBound(arr,target):
    low = 0 
    high = len(arr)-1
    ans = 0

    while low<=high:
        mid = (low+high)//2

        if arr[mid]>target:
            ans = mid
            high = mid-1
        else:
            low = mid+1

    return ans


arr = [0, 0, 1, 1, 1, 2, 3]
target = 1
f = lowerBound(arr,target)
l = upperBound(arr,target)
print("Num of Occurence : ",l-f)