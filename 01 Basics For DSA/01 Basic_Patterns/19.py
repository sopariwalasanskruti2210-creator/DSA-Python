'''
**********
****  ****
***    ***
**      **
*        *
*        *
**      **
***    ***
****  ****
**********
'''
n=int(input("Enter a num : "))
for row in range(n,0,-1):
  for column in range(1,row+1):
    print("*",end="")
  for space in range(1,n-row+1):
    print("",end="  ")
  for reverse in range(1,row+1):
    print("*",end="")
  print()
for row in range(1,n+1):
  for column in range(1,row+1):
    print("*",end="")
  for space in range(1,n-row+1):
    print(" "*2,end="")
  for reverse in range(1,row+1):
    print("*",end="")
  print()