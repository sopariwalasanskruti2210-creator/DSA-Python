'''
Given an array arr of n elements. The task is to reverse the given array. The reversal of array should be inplace.
'''
def reverse(left,right,arr):
  if(left>=right):
    return
  arr[left],arr[right]=arr[right],arr[left]
  reverse(left+1,right-1,arr)
  return arr

arr = [1,2,3,4,5]
left = 0
right = len(arr) - 1
r = reverse(left,right,arr)
print(r)