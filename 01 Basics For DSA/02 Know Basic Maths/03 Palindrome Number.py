'''
You are given an integer n. You need to check whether the number is a palindrome number or not. 
Return true if it's a palindrome number, otherwise return false.
A palindrome number is a number which reads the same both left to right and right to left.
'''
n=int(input("Enter a num : "))
temp = n
rev=0
while n>0:
  rmd=n%10
  rev=rev*10+rmd
  n//=10

if (rev==temp):
  print(temp," is palindrome")
else:
  print(temp," is not  palindrome")