'''
Given an integer n, write a function to print all numbers from 1 to n (inclusive) using recursion.
You must not use any loops such as for, while, or do-while.
The function should print each number on a separate line, in increasing order from 1 to n.
'''
def print_num(n):
  if(n==0):
    return 0
  print_num(n-1)
  print(n)

x=int(input("Enter a num : "))
print_num(x)