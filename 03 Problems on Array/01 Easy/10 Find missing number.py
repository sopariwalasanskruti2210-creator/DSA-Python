'''
Given an integer array of size n containing distinct values in the 
range from 0 to n (inclusive), return the only number missing from the array within this range.
'''

nums = [0, 2, 3, 1, 4]
n = len(nums)+1

for i in range(n):

	# Find in the array range
	found = False

	for j in range(n-1):

		# If found return true
		if(nums[j]==i):
			found=True
			break

	# If not found print i
	if not found:
		print(i)
