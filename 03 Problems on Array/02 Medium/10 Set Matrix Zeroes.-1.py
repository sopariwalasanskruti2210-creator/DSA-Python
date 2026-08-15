'''
Given an m x n integer matrix matrix, if an element is 0, set its entire row and column to 0. You must do it in place.
'''
# Make Zeos in matrix - Brute Force
nums = [[1,1,1],[1,0,1],[1,1,1]]
n=len(nums)
m=len(nums[0])
for i in range(n):
  for j in range(m):
    if nums[i][j]==0:
      for row in range(n):
        if nums[row][j]!=0:
          nums[row][j]=-1

      for col in range(m):
        if nums[i][col]!=0:
          nums[i][col]=-1

for i in range(n):
  for j in range(m):
    if nums[i][j]==-1:
      nums[i][j]=0

print(nums)