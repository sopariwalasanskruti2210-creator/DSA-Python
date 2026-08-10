'''
1 
2 3 
4 5 6 
7 8 9 10 
11 12 13 14 15
'''
n=int(input("enter a num : "))
j=1
for row in range(1,n+1):
  for column in range(1,row+1):
    print(j,end=" ")
    j+=1
  print()