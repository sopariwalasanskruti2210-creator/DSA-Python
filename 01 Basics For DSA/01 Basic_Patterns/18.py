"""
E
D E
C D E
B C D E
A B C D E
"""

n = int(input("Enter a num : "))
for row in range(1, n + 1):
    for column in range(n - row, n):
        print(chr(65 + column), end="")
    print()
