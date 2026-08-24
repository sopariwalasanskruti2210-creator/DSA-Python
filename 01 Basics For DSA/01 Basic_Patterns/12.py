"""
1        1
12      21
123    321
1234  4321
1234554321
"""

n = int(input("Enter a num : "))
for i in range(1, n + 1):
    for j in range(1, i + 1):
        print(j, end="")
    for k in range(1, n - i + 1):
        print(" ", end=" ")
    for s in range(i, 0, -1):
        print(s, end="")
    print()
