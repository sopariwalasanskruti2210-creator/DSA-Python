'''
Given an integer array nums, find the subarray with the largest sum and return the sum of the 
elements present in that subarray.
A subarray is a contiguous non-empty sequence of elements within an array.
'''

nums = [-2,1,-3,4,-1,2,1,-7,4]
sum = 0
max_sum = float("-inf")
i=0
current_start = 0
best_start = 0
end = -1

while i<len(nums):

	# Update sum with current element
	sum+=nums[i]

	# If current sum is greater than max_sum then store it start and end as 
	# best_start as we are finding best start
	if sum>max_sum:
		max_sum=sum
		best_start = current_start
		end=i

	# If sum is negative then drop it and reset current_start
	# IMPORTANT : Don't drop the if element is negative because there might be case where the sum be positive 
	# For example : nums = [2,-1,2,4] => so at index sum = 1 but nums[i] = -1 
	# but at next index nums[i] = 2 so sum increase 
	# Here there is no point in taking negative sum because it will just decrease 
	# the sum but negative element may hepl to get max sum
	if sum<0:
		sum=0
		current_start=i+1

	i+=1

print(max_sum)
ans = []
for i in range(best_start,end+1):
  	ans.append(nums[i])

print(ans)