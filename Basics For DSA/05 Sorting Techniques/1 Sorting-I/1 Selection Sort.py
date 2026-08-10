'''
Given an array of integers nums, sort the array in non-decreasing order u
sing the selection sort algorithm and return the sorted array.
A sorted array in non-decreasing order is an array where each element is 
greater than or equal to all previous elements in the array.
'''
print("Enter the array elements : ")
arr = list(map(int,input().split()))
print(arr)
print("--------------")
for i in range(len(arr)-1):
  mini = i
  for j in range(i,len(arr)):
    if(arr[j]<arr[mini]):
      arr[j],arr[mini]=arr[mini],arr[j]
      print(arr)

print("--------------")
print("Sorted Array using Selection Sort : ",arr)