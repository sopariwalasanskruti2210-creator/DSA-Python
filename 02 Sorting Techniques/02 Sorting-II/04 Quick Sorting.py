'''
Given an array of integers called nums, sort the array in non-decreasing 
order using the quick sort algorithm and return the sorted array.
A sorted array in non-decreasing order is an array where each element is 
greater than or equal to all preceding elements in the array.
'''
def Partion(arr,low,high):
  pivot=arr[low]
  i=low+1
  j=high
  while(i<=j):
    while(i<=high and arr[i]<pivot):
      i+=1
    while(j>=low and arr[j]>pivot):
      j-=1
    if i<j:
      arr[i],arr[j]=arr[j],arr[i]
  arr[low],arr[j]=arr[j],arr[low]
  return j

def QuickSort(arr,low ,high):
  if(low<high):
    partion=Partion(arr,low,high)
    QuickSort(arr,low,partion-1)
    QuickSort(arr,partion+1,high)

print("Enter the array : ")
arr=list(map(int,input().split()))
QuickSort(arr,0,len(arr)-1)
print(arr)