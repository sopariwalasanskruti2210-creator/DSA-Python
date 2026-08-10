'''
Given an array of integers nums, sort the array in non-decreasing order using the recursive Bubble Sort algorithm, and return the sorted array.
You must implement Bubble Sort using recursion only.
Do not use built-in sorting functions (sort, sorted, Arrays.sort, etc.).
A sorted array in non-decreasing order is an array where each element is greater than or equal to the previous one.
'''
def bubbleSort(arr,n):
  if n==1:
    return

  did_swap = False
  for j in range(n-1):
    if(arr[j]>arr[j+1]):
      arr[j],arr[j+1]=arr[j+1],arr[j]
      print(arr)
      did_swap = True

  if not did_swap:
    return

  bubbleSort(arr,n-1)

print("Enter array : ")
arr = list(map(int,input().split()))
res = bubbleSort(arr,len(arr))

print(arr)