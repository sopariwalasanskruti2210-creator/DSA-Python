'''
A permutation of an array of integers is an arrangement of its members into a sequence or linear order.
For example, for arr = [1,2,3], the following are all the permutations of arr.
[1,2,3], [1,3,2], [2,1,3], [2,3,1], [3,1,2], [3,2,1].
The next permutation of an array of integers is the next lexicographically greater permutation of its integers.
More formally, if all the permutations of the array are sorted in lexicographical order, 
then the next permutation of that array is the permutation that follows it in the sorted order.
If such arrangement is not possible (i.e., the array is the last permutation), 
then rearrange it to the lowest possible order (i.e., sorted in ascending order).
You must rearrange the numbers in-place and use only constant extra memory.
'''
nums = [2,3,5,4,1]
n=len(nums)
breakPoint=-1
for i in range(n-2,-1,-1):
  if nums[i]<nums[i+1]:
    breakPoint=i
    break

if breakPoint==-1:
  nums=reversed(nums)
else:
  for j in range(n-1,breakPoint,-1):
    if nums[j]>nums[breakPoint]:
      nums[breakPoint],nums[j]=nums[j],nums[breakPoint]
      break

  nums[breakPoint+1:]=reversed(nums[breakPoint+1:])

print(nums)