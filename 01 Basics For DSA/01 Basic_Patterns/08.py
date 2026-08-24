"""
*********
 *******
  *****
   ***
    *
"""

n = int(input("Enter a num : "))
for i in range(n, 0, -1):
    for j in range(1, n - i + 1):
        print(" ", end="")
    # for k in range(1,i+1):
    #   print("*",end="")
    # for s in range(2,i+1):
    #   print("*",end="")
    for k in range(1, 2 * i):
        print("*", end="")
    print()
