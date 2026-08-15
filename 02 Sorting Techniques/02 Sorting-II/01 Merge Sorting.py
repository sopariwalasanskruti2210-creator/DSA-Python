'''
Given an array of integers nums, sort the array in non-decreasing order u
sing the selection sort algorithm and return the sorted array.
A sorted array in non-decreasing order is an array where each element is 
greater than or equal to all previous elements in the array.(using Merge Sort)
'''
def merge(arr,low,mid,high):
  left,right=low,mid+1

  #Merge both sorted array
  temp=[]
  while left<=mid and right<=high:
    if(arr[left]<arr[right]):
      temp.append(arr[left])
      left+=1
    else:
      temp.append(arr[right])
      right+=1

  #Add remaining left element
  while left<=mid:
    temp.append(arr[left])
    left+=1
  #Add remaining right element
  while right<=high:
    temp.append(arr[right])
    right+=1

  #Copy sorted temp into original
  for i in range(low,high+1):
    arr[i]=temp[i-low]

#Recursive merge sort
def merge_sort(arr,low,high):
  if low>=high:
    return
  mid = (low+high)//2
  merge_sort(arr,low,mid)
  merge_sort(arr,mid+1,high)
  merge(arr,low,mid,high)


arr = [5,2,8,4,1]
sol = merge_sort(arr,0,len(arr)-1)
print("Sorted Array : " ,arr)