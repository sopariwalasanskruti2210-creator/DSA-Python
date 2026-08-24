"""
Given two sorted arrays nums1 and nums2, return an array that contains the union of these two arrays.
The elements in the union must be in ascending order.
The union of two arrays is an array where all values are distinct and are present in either the first array,
the second array, or both.
"""

nums1 = [1, 2, 3, 4, 5]
nums2 = [1, 2, 7]
left = 0
right = 0
ans = []

# Here we can use merging algorithm of merge sort to merge both arrays
while left < len(nums1) and right < len(nums2):

    # Check if left element is smaller
    if nums1[left] < nums2[right]:
        ans.append(nums1[left])
        left += 1

    # Check if right element is smaller
    elif nums2[right] < nums1[left]:
        ans.append(nums2[right])
        right += 1

    # If both are same add any
    else:
        ans.append(nums1[left])
        left += 1
        right += 1

# Add remaining left element if there is any
while left < len(nums1):
    ans.append(nums1[left])
    left += 1

# Add remaining right element if there is any
while right < len(nums2):
    ans.append(nums2[right])
    right += 1

print(ans)
