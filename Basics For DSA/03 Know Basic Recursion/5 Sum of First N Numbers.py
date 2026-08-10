'''
Given an integer N, return the sum of first N natural numbers. Try to solve this using recursion.
'''
def sum(n):
  if(n==0):
    return 0
  return n + sum(n-1)

n = int(input("Enter a num : "))
x = sum(n)
print("Sum = ",x)