'''
Given two sorted arrays nums1 and nums2, return an array that contains the union of these two arrays. 
The elements in the union must be in ascending order.
The union of two arrays is an array where all values are distinct and are present in either the first array, 
the second array, or both.
'''
nums1 = [1, 2, 3, 4, 5]
nums2 = [1, 2, 7]
left = 0
right = 0
ans=set()
while left<len(nums1) and right<len(nums2):
  if nums1[left]<nums2[right]:
    ans.add(nums1[left])
    left+=1
  elif nums2[right]<nums1[left]:
    ans.add(nums2[right])
    right+=1
  else:
    ans.add(nums1[left])
    left+=1
    right+=1

while left<len(nums1):
  ans.add(nums1[left])
  left+=1

while right<len(nums2):
  ans.add(nums2[right])
  right+=1

ans = list(ans)
print(ans)