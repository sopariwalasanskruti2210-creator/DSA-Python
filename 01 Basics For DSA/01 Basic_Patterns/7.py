'''
    *
   ***
  *****
 *******
*********
'''
n=int(input("Enter a num : "))
for i in range(1,n+1):
  for j in range(1,n-i+1):
    print(" ",end="")
  for k in range(1,i+1):
    print("*",end="")
  for s in range(2,i+1):
    print("*",end="")
  print()
