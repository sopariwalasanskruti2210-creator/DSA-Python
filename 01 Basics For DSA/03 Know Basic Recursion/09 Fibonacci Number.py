'''
The Fibonacci numbers form a sequence where each number
is the sum of the previous two numbers.

F(0) = 0
F(1) = 1

F(n) = F(n - 1) + F(n - 2)
'''

def fib(n):

    # Example: fib(5)
    #
    # fib(5)
    # = fib(4) + fib(3)
    #
    # fib(4)
    # = fib(3) + fib(2)
    #
    # fib(3)
    # = fib(2) + fib(1)
    #
    # The recursion continues until it reaches
    # the base cases:
    #
    # fib(0) = 0
    # fib(1) = 1

    # Base case
    if n == 0:
        return 0

    if n == 1:
        return 1

    # Recursive case:
    # Current Fibonacci number is the sum
    # of the previous two Fibonacci numbers
    return fib(n - 1) + fib(n - 2)


n = int(input("Enter a num till which Fibonacci series you need: "))

for i in range(n + 1):
    print(fib(i), end=", ")