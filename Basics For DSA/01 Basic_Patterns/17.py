'''
    A
   ABA
  ABCBA
 ABCDCBA
ABCDEDCBA
'''
n=int(input("Enter a num : "))
for row in range(1,n+1):
  for space in range(1,n-row+1):
    print("",end=" ")
  for column in range(1,row+1):
    print(chr(65+column-1),end="")
  for reverse in range(row-1,0,-1):
    print(chr(65+reverse-1),end="")
  print()