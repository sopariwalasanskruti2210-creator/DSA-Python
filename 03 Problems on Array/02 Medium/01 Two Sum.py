'''
Given an array of integers nums and an integer target. Return the indices(0 - indexed) 
of two elements in nums such that they add up to target.
Each input will have exactly one solution, and the same element cannot be used twice. Return the answer in any order.
'''

nums = [1, 6, 0, 10, -3]
target = 7
prefix = {}
ans = []

for i in range(len(nums)):

	# Check if target - nums[i] is in prefix 
	# for example : 2 + 3 = 5 target = 7 if we have nums[i] = 2 
	# so we will check if 3 is there in prefix or not if it is thne they add up to target
	pre=target-nums[i]
	if pre in prefix:
		ans.append([prefix[pre],i])
		print(ans[0])
		break

	# Append the nums[i] in prefix
	prefix[nums[i]]=i
