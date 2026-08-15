'''
You are given an integer n. Return the value of n! or n factorial.
Factorial of a number is the product of all positive integers less than or equal to that number.
'''
def factorial(n):
  if n==0 or n==1:
    return 1
  return n*factorial(n-1)

n = int(input("Enter a num : "))
fact = factorial(n)
print(f"Factorial of {n} = {fact}")