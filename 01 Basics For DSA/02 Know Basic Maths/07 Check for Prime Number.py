"""
You are given an integer n.
You need to check if the number is prime or not. Return true if it is a prime number, otherwise return false.
A prime number is a number which has no divisors except 1 and itself.
"""

import math


def is_prime(n):
    flag = False

    # To find prime num first check if it is greater than 1 or not
    # If a number has a divisor greater than √n, its paired divisor must be smaller than √n.
    # So if we don't find any divisor up to √n, there cannot be any divisor after that either.
    # For Example : n = 5
    # for => (2,3) => 5%2!=0 and 5%3!=0
    # Therefore 5 is a prime num.
    if n > 1:
        for i in range(2, math.isqrt(n) + 1):
            if n % i == 0:
                flag = False
                break
        else:
            flag = True

    return flag


n = int(input("Enter a num : "))
prime = is_prime(n)
print(prime)
