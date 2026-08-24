"""
A
BB
CCC
DDDD
EEEEE
"""

n = int(input("Enter a num : "))
for row in range(1, n + 1):
    for column in range(1, row + 1):
        print(chr(65 + row - 1), end="")
    print()
