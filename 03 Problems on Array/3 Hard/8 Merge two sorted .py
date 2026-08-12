'''
Given two integer arrays nums1 and nums2. Both arrays are sorted in non-decreasing order.
Merge both the arrays into a single array sorted in non-decreasing order.
The final sorted array should be stored inside the array nums1 and it should be done in-place.
nums1 has a length of m + n, where the first m elements denote the elements of nums1 and rest are 0s.
nums2 has a length of n.
'''
nums1 = [-5, -2, 4, 5, 0, 0, 0]
nums2 = [-3, 1, 8]
n1 = 0
for i in nums1:
    if i!=0:
        n1+=1
n2 = len(nums2)
left = nums1[0]
right = nums2[0]
while left<n1:
    if nums2[right]<nums1[left]:
        
