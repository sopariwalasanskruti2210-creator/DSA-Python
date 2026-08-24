"""
You are given an integer n. Return the integer formed by placing the digits of n in reverse order.
"""

n = int(input("Enter a num : "))
rev = 0
while n > 0:

    # For Example : 123
    # rmd : 3 => rev = 0*10 + 3 =3
    # rmd : 2 => rev = 3*10 + 2 = 32
    # rmd : 1 => rev = 32*10 + 1 =321
    rmd = n % 10
    rev = rev * 10 + rmd
    n //= 10

print(rev)
