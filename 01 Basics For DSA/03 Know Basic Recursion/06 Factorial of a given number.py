"""
You are given an integer n. Return the value of n! or n factorial.
Factorial of a number is the product of all positive integers less than or equal to that number.
"""


def factorial(n):

    # Example: n = 5
    #
    # factorial(5)
    # = 5 * factorial(4)
    # = 5 * 4 * factorial(3)
    # = 5 * 4 * 3 * factorial(2)
    # = 5 * 4 * 3 * 2 * factorial(1)
    #
    # Base case:
    # factorial(1) = 1
    #
    # Then recursion returns:
    #
    # factorial(2) = 2 * 1 = 2
    # factorial(3) = 3 * 2 = 6
    # factorial(4) = 4 * 6 = 24
    # factorial(5) = 5 * 24 = 120

    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)


n = int(input("Enter a num : "))
fact = factorial(n)
print(f"Factorial of {n} = {fact}")
