'''
Given a sorted array of unique positive integers arr, your task is to return the
kᵗʰ missing positive number that is not present in arr.
The array is guaranteed to be strictly increasing, and the missing numbers are 
those positive integers that do not appear in arr but would appear in a full sequence starting from 1.
'''

# Brute force

# In this method we are finding 6th missing num not 6th indexed num
# for that we check that if there is any existing element before k 
# for example : arr = [] so the 6th missing num is 6 itself now
# if arr = [5,7,9,10] k = 4 so 4th missing num is 4
# but if arr = [3,5,7,10] k = 6 so the first num of array is 3 which comes before 6 so 6th missing element will pushed to 7
# then after that 5 < 7 so it will again pushed k = 8 now 7 < 8 so it will again pushed now 10 < 9? no so that is the final ans 
arr = [3, 5, 7, 10]
k = 6

for i in range(len(arr)):
    if arr[i]<k:
        k+=1
    else:
        break
    
print(k)

