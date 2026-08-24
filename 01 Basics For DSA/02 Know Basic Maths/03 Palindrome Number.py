"""
You are given an integer n. You need to check whether the number is a palindrome number or not.
Return true if it's a palindrome number, otherwise return false.
A palindrome number is a number which reads the same both left to right and right to left.
"""

n = int(input("Enter a num : "))
temp = n
rev = 0
while n > 0:
    # When we reversed the num and it same as original num then that num is called palindrome num.
    # For Example :
    # 141
    # 141%10 => rmd = 1 => rev = 0*10+1 = 1 => 141//10 = 14
    # 14%10 => rmd = 4 => rev = 1*10+4 = 14 => 14//10 = 1
    # 1%10 => rmd = 1 => rev = 14*10+1 = 141 => 1//10 = 0
    # Therefore 141 is palindrome num
    rmd = n % 10
    rev = rev * 10 + rmd
    n //= 10

if rev == temp:
    print(temp, " is palindrome")
else:
    print(temp, " is not  palindrome")
