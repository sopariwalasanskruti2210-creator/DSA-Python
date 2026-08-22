'''
You are given an integer n. You need to return the number of digits in the number.
The number will have no leading zeroes, except when the number is 0 itself.
'''
n=int(input("Enter a num : "))
lst=list(str(n))
digits=0

# Iterate through digit then do sum
# For Example : 123 
# 1+2+3 = 6
for digit in lst:
  digits+=1

print(digits)