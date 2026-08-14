'''
Given an integer array nums. Return the number of inversions in the array.
Two elements a[i] and a[j] form an inversion if a[i] > a[j] and i < j.
It indicates how close an array is to being sorted.
A sorted array has an inversion count of 0.
An array sorted in descending order has maximum inversion.
'''
nums = [2, 3, 7, 1, 3, 5]
count = 0
def mrgsrt(nums,low,mid,high):
    temp = []
    left = low
    right = mid+1
    cnt = 0
    while left<=mid and right<=high:
        if nums[left]<=nums[right]:
            temp.append(nums[left])
            left+=1
        else:
            temp.append(nums[right])
            cnt += (mid-left+1)
            right+=1

    while left <= mid:
        temp.append(nums[left])
        left += 1

    while right <= high:
        temp.append(nums[right])
        right += 1

    for i in range(low, high + 1):
        nums[i] = temp[i - low]

    return cnt
    
def mergeSort(nums,low,high):
    cnt = 0
    if low>=high:
        return cnt
    mid = (low+high)//2
    cnt+=mergeSort(nums,low,mid)
    cnt+=mergeSort(nums,mid+1,high)
    cnt+=mrgsrt(nums,low,mid,high)
    return cnt

nums = [2, 3, 7, 1, 3, 5]
res = mergeSort(nums,0,len(nums)-1)
print(nums)
print(res)
