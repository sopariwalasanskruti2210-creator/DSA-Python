'''
Given an integer array nums. Return the number of reverse pairs in the array.
An index pair (i, j) is called a reverse pair if:
0 <= i < j < nums.length
nums[i] > 2 * nums[j]
'''
def mergeSort(nums,low,mid,high):
    temp = []
    left = low
    right = mid+1
    while left<=mid and right<=high:
        if nums[left]<nums[right]:
            temp.append(nums[left])
            left+=1
        else:
            temp.append(nums[right])
            right+=1

    while left<=mid:
        temp.append(nums[left])
        left+=1

    while right<=high:
        temp.append(nums[right])
        right+=1

    for i in range(low,high+1):
        nums[i]=temp[i-low]

def countPairs(nums,low,mid,high):
    left = low
    right = mid+1
    cnt = 0
    for i in range(left,right):
        while right<=high and nums[i]>2*nums[right]:
            right+=1
        cnt+=(right-(mid+1))

    return cnt


def merge(nums,low,high):
    cnt = 0
    if low>=high:
        return 0

    mid = (low+high)//2
    cnt+=merge(nums,low,mid)
    cnt+=merge(nums,mid+1,high)
    cnt+=countPairs(nums,low,mid,high)
    mergeSort(nums,low,mid,high)
    return cnt

nums = [6, 4, 1, 2, 7]
res = merge(nums,0,len(nums)-1)
print(res)
