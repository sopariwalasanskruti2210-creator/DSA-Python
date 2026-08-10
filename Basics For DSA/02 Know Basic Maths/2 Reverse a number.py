'''
You are given an integer n. Return the integer formed by placing the digits of n in reverse order.
'''
n=int(input("Enter a num : "))
rev=0
while n>0:
  rmd=n%10
  rev=rev*10+rmd
  n//=10

print(rev)