"""
Recursive Insertion Sort

No for loop
No while loop
"""


def insert(arr, j):

    # Base case:
    # If j reaches 0, the element is already
    # at the beginning of the array.
    if j == 0:
        return

    # If the left element is greater,
    # swap them and continue moving left.
    if arr[j - 1] > arr[j]:

        arr[j - 1], arr[j] = arr[j], arr[j - 1]

        print(arr)

        # Recursively check the previous position.
        insert(arr, j - 1)


def insert_sort(arr, i, n):

    # Base case:
    # If all elements have been processed,
    # the array is sorted.
    if i == n:
        return

    # Insert arr[i] into its correct position
    # in the already sorted left part.
    insert(arr, i)

    # Move to the next element recursively.
    insert_sort(arr, i + 1, n)


print("Enter array:")

arr = list(map(int, input().split()))

insert_sort(arr, 0, len(arr))

print("Sorted Array:", arr)
