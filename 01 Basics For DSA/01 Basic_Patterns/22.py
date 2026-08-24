"""
5 5 5 5 5 5 5 5 5
5 4 4 4 4 4 4 4 5
5 4 3 3 3 3 3 4 5
5 4 3 2 2 2 3 4 5
5 4 3 2 1 2 3 4 5
5 4 3 2 2 2 3 4 5
5 4 3 3 3 3 3 4 5
5 4 4 4 4 4 4 4 5
5 5 5 5 5 5 5 5 5
"""

n = int(input("Enter a num : "))
for i in range(2 * n - 1):
    for j in range(2 * n - 1):
        # Find the minimum distance from element and then do n-minimum distance
        top = i
        left = j
        right = (2 * n - 2) - j
        bottom = (2 * n - 2) - i

        print(n - min(min(top, bottom), min(left, right)), end=" ")
    print()
