"""
Given an integer N, return the sum of first N natural numbers. Try to solve this using recursion.
"""


def sum(n):

    # Example: n = 5
    #
    # sum(5)
    # = 5 + sum(4)
    # = 5 + 4 + sum(3)
    # = 5 + 4 + 3 + sum(2)
    # = 5 + 4 + 3 + 2 + sum(1)
    # = 5 + 4 + 3 + 2 + 1 + sum(0)
    #
    # Base case:
    # sum(0) returns 0
    #
    # Then recursion starts returning:
    #
    # sum(1) = 1 + 0 = 1
    # sum(2) = 2 + 1 = 3
    # sum(3) = 3 + 3 = 6
    # sum(4) = 4 + 6 = 10
    # sum(5) = 5 + 10 = 15
    if n == 0:
        return 0
    return n + sum(n - 1)


n = int(input("Enter a num : "))
x = sum(n)
print("Sum = ", x)
