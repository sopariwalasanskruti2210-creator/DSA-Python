'''
Given an array of integers nums, sort the array in non-decreasing order u
sing the selection sort algorithm and return the sorted array.
A sorted array in non-decreasing order is an array where each element is 
greater than or equal to all previous elements in the array.
'''
print("Enter the array element : ")
arr = list(map(int,input().split()))

for i in range(len(arr)):
  j=i
  while(j>0 and arr[j-1]>arr[j]):
    arr[j-1],arr[j]=arr[j],arr[j-1]
    j-=1
    print(arr)

print("Sorted Array : ",arr)