'''
Given an integer n, write a function to print all numbers from 1 to n (inclusive) using recursion.
You must not use any loops such as for, while, or do-while.
The function should print each number on a separate line, in increasing order from 1 to n.
'''
def print_num(n):

  # Recursion works using the call stack.
    # For example: n = 5
    #
    # First, the function keeps making recursive calls:
    #
    # 5 -> call print_num(4)
    # 4 -> call print_num(3)
    # 3 -> call print_num(2)
    # 2 -> call print_num(1)
    # 1 -> call print_num(0)
    # 0 -> Base case -> return
    #
    # At n = 0, the call stack looks like:
    #
    #         CALL STACK
    # ┌─────────────────┐
    # │ print_num(0)    │ ← currently executing
    # ├─────────────────┤
    # │ print_num(1)    │ ← waiting
    # ├─────────────────┤
    # │ print_num(2)    │ ← waiting
    # ├─────────────────┤
    # │ print_num(3)    │ ← waiting
    # ├─────────────────┤
    # │ print_num(4)    │ ← waiting
    # ├─────────────────┤
    # │ print_num(5)    │ ← first call
    # └─────────────────┘
    #
    # Now the functions return one by one:
    #
    # print_num(0) returns
    # print_num(1) -> print 1
    # print_num(2) -> print 2
    # print_num(3) -> print 3
    # print_num(4) -> print 4
    # print_num(5) -> print 5
  if(n==0):
    return 0
  print_num(n-1)
  print(n)

x=int(input("Enter a num : "))
print_num(x)