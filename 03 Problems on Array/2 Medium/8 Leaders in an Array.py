'''
Given an integer array nums, return a list of all the leaders in the array.
A leader in an array is an element whose value is strictly greater than all elements to its right in 
the given array. The rightmost element is always a leader. The elements in the leader array must appear in the order 3
they appear in the nums
'''
nums = [1, 2, 5, 3, 1, 2]
ans = []
max_val = nums[-1]
ans.append(nums[-1])
for i in range(len(nums)-1,-1,-1):
  if nums[i]>max_val:
    ans.append(nums[i])
    max_val=nums[i]

ans.reverse()
print(ans)