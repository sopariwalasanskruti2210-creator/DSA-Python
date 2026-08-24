"""
You are given two integers n1 and n2.
You need find the Greatest Common Divisor (GCD) of the two given numbers. Return the GCD of the two numbers.
The Greatest Common Divisor (GCD) of two integers is the largest positive integer that divides both of the integers.
"""

n1 = int(input("Enter a num : "))
n2 = int(input("Enter a num : "))
gcd = 1
for num in range(min(n1, n2), 0, -1):

    # For two numbers the GCD would be always GCD<=min(n1,n2) so to find it easily we start from
    # min(n1,n2) to goes till 1 only numbers like 11 and 13 will come in worst case. where time complexity will be O(n)
    # This solution will be easier to find GCD for nums like (40,20) where GCD = 20
    if n1 % num == 0 and n2 % num == 0:
        gcd = num
        break

print(gcd)
