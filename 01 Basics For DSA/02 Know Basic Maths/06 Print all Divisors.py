'''
You are given an integer n. You need to find all the divisors of n. Return 
all the divisors of n as an array or list in a sorted order.
A number which completely divides another number is called it's divisor.
'''
import math
n = int(input("Enter a num : "))
ans = []
for i in range(1,math.isqrt(n)+1):

  # Divisor of any number for example 36 : 
  # 1 x 1
  # 2 x 18
  # 3 x 12
  # 4 x 9
  # 6 x 6
  # We only need to check divisors up to √n because every divisor greater than √n 
  # has a corresponding divisor smaller than √n. 
  # So we check if i!=(n//i) this is to prevent duplicates like for 36 : 6 x 6 so the 6 might comes two times 
  # so we check if it is same as i or not and if it is not then we can append (n//i)
  if n%i==0:
    ans.append(i)

    if i!=n//i:
      ans.append(n//i)

ans.sort()
print(ans)