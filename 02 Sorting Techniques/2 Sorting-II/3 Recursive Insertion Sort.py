'''
Given an array of integers nums, sort the array in non-decreasing order 
using the recursive Insertion Sort algorithm, and return the sorted array.
You must implement Insertion Sort using recursion only.
Do not use loops (like for or while) or built-in sorting functions (sort, Arrays.sort, etc.).
A sorted array in non-decreasing order is an array where each element is 
greater than or equal to all elements that come before it.
'''
def insertSort(arr,i,n):
  if i==n:
    return
  j=i
  while(j>0 and arr[j-1]>arr[j]):
    arr[j-1],arr[j]=arr[j],arr[j-1]
    print(arr)
    j-=1

  insertSort(arr,i+1,n)

j=0
print("Enter array : ")
arr = list(map(int,input().split()))
sol = insertSort(arr,0,len(arr))
print(arr)