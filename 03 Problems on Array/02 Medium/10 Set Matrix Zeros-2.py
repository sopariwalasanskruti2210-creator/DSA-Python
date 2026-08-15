'''
Given an m x n integer matrix matrix, if an element is 0, set its entire row and column to 0. You must do it in place.
'''
# Make Zeos in matrix - Better Approach
nums = [[1,1,1],[1,0,1],[1,1,1]]
m=len(nums)
n=len(nums[0])
rows = [0]*m
cols = [0]*n
for i in range(m):
  for j in range(n):
    if nums[i][j]==0:
      rows[i]=1
      cols[j]=1

for i in range(m):
  for j in range(n):
    if rows[i] or cols[j]:
      nums[i][j]=0

print(nums)