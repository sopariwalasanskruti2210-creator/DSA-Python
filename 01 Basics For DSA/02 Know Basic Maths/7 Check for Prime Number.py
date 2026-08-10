'''
You are given an integer n. 
You need to check if the number is prime or not. Return true if it is a prime number, otherwise return false.
A prime number is a number which has no divisors except 1 and itself.
'''
def is_prime(n):
  flag=False
  if(n>1):
    for i in range(2,n):
      if(n%i==0):
        flag=False
        break
      else:
        flag=True
  return flag
n=int(input("Enter a num : "))
prime=is_prime(n)
print(prime)