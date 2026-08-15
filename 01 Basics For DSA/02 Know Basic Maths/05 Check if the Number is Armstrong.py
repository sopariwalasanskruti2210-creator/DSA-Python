''' 
You are given an integer n. You need to 
check whether it is an armstrong number or not. Return true if it is an armstrong number, otherwise return false.
An armstrong number is a number which is equal to the sum of the digits of the number, 
raised to the power of the number of digits.
'''
n=int(input("Enter a num : "))
temp=n
armstrong=0
digits = len(str(n))
print(digits)
while n>0:
  rmd = n%10
  armstrong = armstrong + rmd**digits
  n//= 10

print(armstrong)
if(temp==armstrong):
  print("True")
else:
  print("False")