'''
Given an array nums of n integers.
Return the length of the longest sequence of consecutive integers. 
The integers in this sequence can appear in any order.
'''
nums = [100, 4, 200, 1, 3, 2]
st = set()
cn1=1
longest = 1
for i in range(len(nums)):
  st.add(nums[i])

for it in st:
  if it-1 not in st:
    cnt = 1
    x = it
    while x+1 in st:
      x=x+1
      cnt+=1
    longest=max(longest,cnt)

print(longest)