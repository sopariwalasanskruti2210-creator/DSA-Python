'''
Given an array of integers nums, return 
the second-largest element in the array. 
If the second-largest element does not exist, return -1.
'''
'''
Given an array of integers nums, return the value of the largest element in the array
'''
# def merge(nums,low,mid,high):
#     left,right = low,mid+1
#     temp=[]

#     while left<=mid and right<=high:
#         if(nums[left]>nums[right]):
#             temp.append(nums[left])
#             left+=1
#         else:
#             temp.append(nums[right])
#             right+=1

#         while left<=mid:
#             temp.append(nums[left])
#             left+=1

#         while right<=high:
#             temp.append(nums[right])
#             right+=1

#         for i in range(low,high+1):
#             nums[i]=temp[i-low]

# def mrgsrt(nums,low,high):
#     mid = (low+high) // 2
#     if low>=high:
#         return
#     mrgsrt(nums,low,mid)
#     mrgsrt(nums,mid+1,high)
#     merge(nums,low,mid,high)

# nums= [1,5,42,11,56]
# if (len(nums)-1==1):
#     print(-1)
# else:
#     mrgsrt(nums,0,len(nums)-1)
#     print(nums[1])

nums= [1,5,42,11]
max1 = float("-inf")
max2 = float("-inf")
for i in range(len(nums)):
    if nums[i]>max1:
        max2 = max1
        max1 = nums[i]
    elif nums[i]>max2:
        max2=nums[i]

print(max2)