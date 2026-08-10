'''
You are given an integer n. You need to find all the divisors of n. Return 
all the divisors of n as an array or list in a sorted order.
A number which completely divides another number is called it's divisor.
'''
import math
n = int(input("Enter a num : "))
ans = []
for i in range(1,math.isqrt(n)+1):
  if n%i==0:
    ans.append(i)

    if i!=n//i:
      ans.append(n//i)

ans.sort()
print(ans)