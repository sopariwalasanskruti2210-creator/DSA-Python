'''
Given an integer array nums of size n. 
Return all elements which appear more than n/3 times in the array. The output can be returned in any order.
'''
nums = [1, 2, 1, 1, 3, 2, 2, 3]
n = len(nums)
count = {}
for num in nums:
  if num not in count:
    count[num]=1
  else:
    count[num]+=1

ans=[]
ans = [key for key,value in count.items() if value>(n//3)]
print(count)
print(ans)