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

	# In permutation suppose we have nums = [1,2,3,4,5] so we have permutation = [5,4,3,2,1] 
	# so here if we start from right every element is greater than previous so we find the breakpoint 
	# where it is not greater because the next permutation is by rearraging those element only
	if nums[i]<nums[i+1]:
		breakPoint=i
		break

# So if we find no breakpoint means it is last permutation so we have to return first permutation means nums = [1,2,3,4,5]
if breakPoint==-1:
  	nums=reversed(nums)

# Now find an element on the right side which is
# greater than the breakpoint element.
# We start from the right because the first element greater
# than the breakpoint will be the smallest possible element
# that can make the permutation greater.
# Example: nums = [2,3,5,4,1] breakpoint = 3
# From the right, 4 is the first element greater than 3.
else:
	for j in range(n-1,breakPoint,-1):
		if nums[j]>nums[breakPoint]:
			nums[breakPoint],nums[j]=nums[j],nums[breakPoint]
			break

	# After breakpoint just reverse the num to make smaller permutation
	nums[breakPoint+1:]=reversed(nums[breakPoint+1:])

# Example: nums = [2,3,5,4,1]
#
# First, find the breakpoint from the right.
# breakpoint = 3 because 3 < 5.
#
# Then find the smallest element greater than 3 from the right.
# That element is 4, so swap them:
# [2,4,5,3,1]
#
# Finally, reverse everything after the breakpoint
# to get the smallest possible arrangement:
# [2,4,1,3,5]
print(nums)