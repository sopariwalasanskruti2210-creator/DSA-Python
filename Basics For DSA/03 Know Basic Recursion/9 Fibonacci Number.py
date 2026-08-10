'''
The Fibonacci numbers, commonly denoted F(n) form a sequence, 
called the Fibonacci sequence, such that each number is the sum of the two preceding ones, starting from 0 and 1. That is,
F(0) = 0, F(1) = 1
F(n) = F(n - 1) + F(n - 2), for n > 1.
Given n, calculate F(n).
'''
def fib(n):
  if(n==0):
    return 0
  elif(n==1):
    return 1
  return fib(n-1) + fib(n-2)

n=int(input("Enter a num till fibonacci series u need to print : "))
for i in range(0,n+1):
  print(fib(i),end=",")