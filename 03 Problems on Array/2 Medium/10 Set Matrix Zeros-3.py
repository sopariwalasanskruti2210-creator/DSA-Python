'''
Given an m x n integer matrix matrix, if an element is 0, set its entire row and column to 0. You must do it in place.
'''
# Make Zeos in matrix - Optimal Approach
# Optimal Approach
nums = [[1,1,1],[1,0,1],[1,1,1]]
m=len(nums)
n=len(nums[0])
col0 = 1
for i in range(m):
  for j in range(n):
    if nums[i][j]==0:
      nums[i][0]=0
      if j!=0:
        nums[0][j]=0
      else:
        col0 = 0

for i in range(1,m):
  for j in range(1,n):
    if nums[i][0]==0 or nums[0][j]==0:
      nums[i][j]=0

if col0==0:
  for j in range(n):
    nums[0][j]=0

print(nums)