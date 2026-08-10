'''
Given an integer n, write a function to print all numbers from n to 1 (inclusive) using recursion.
You must not use any loops such as for, while, or do-while.
The function should print each number on a separate line, in decreasing order from n to 1
'''
def print_num(n):
  if(n==0):
    return 0
  print(n)
  print_num(n-1)

x=int(input("Enter a num : "))
print_num(x)