"""
Given an integer n, write a function to print all numbers from n to 1 (inclusive) using recursion.
You must not use any loops such as for, while, or do-while.
The function should print each number on a separate line, in decreasing order from n to 1
"""


def print_num(n):

    # Recursion is done using stack it goes like below in this case :
    # for example : n = 5
    # 5 -> print 5 -> 4
    # 4 -> print 4 -> 3
    # 3 -> print 3 -> 2
    # 2 -> print 2 -> 1
    # 1 -> print 1 -> 0(base case)
    # So in stack it is like
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
    if n == 0:
        return 0
    print(n)
    print_num(n - 1)


x = int(input("Enter a num : "))
print_num(x)
