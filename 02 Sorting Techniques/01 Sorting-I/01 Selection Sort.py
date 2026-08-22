'''
Given an array of integers nums, sort the array in non-decreasing order
using the selection sort algorithm.
'''

print("Enter the array elements: ")
arr = list(map(int, input().split()))

print(arr)

print("--------------")

for i in range(len(arr) - 1):

    # Selection Sort:
    # In every iteration, find the smallest element
    # from the unsorted part and place it at index i.
    #
    # Example:
    # arr = [22, 2, 12, 77, 23]
    #
    # ------------------------------------------------
    # Iteration 1: i = 0
    #
    # Current array:
    # [22, 2, 12, 77, 23]
    #
    # mini = 0 → arr[mini] = 22
    #
    # j = 1 → 2 < 22 → Yes → mini = 1
    # j = 2 → 12 < 2 → No
    # j = 3 → 77 < 2 → No
    # j = 4 → 23 < 2 → No
    #
    # Smallest element = 2 at index 1
    #
    # Swap arr[0] and arr[1]
    #
    # Array becomes:
    # [2, 22, 12, 77, 23]
    #
    # ------------------------------------------------
    # Iteration 2: i = 1
    #
    # Current array:
    # [2, 22, 12, 77, 23]
    #
    # mini = 1 → arr[mini] = 22
    #
    # j = 2 → 12 < 22 → Yes → mini = 2
    # j = 3 → 77 < 12 → No
    # j = 4 → 23 < 12 → No
    #
    # Smallest element = 12 at index 2
    #
    # Swap arr[1] and arr[2]
    #
    # Array becomes:
    # [2, 12, 22, 77, 23]
    #
    # ------------------------------------------------
    # Iteration 3: i = 2
    #
    # Current array:
    # [2, 12, 22, 77, 23]
    #
    # mini = 2 → arr[mini] = 22
    #
    # j = 3 → 77 < 22 → No
    # j = 4 → 23 < 22 → No
    #
    # Smallest element is already 22 at index 2
    #
    # Swap arr[2] and arr[2]
    #
    # Array remains:
    # [2, 12, 22, 77, 23]
    #
    # ------------------------------------------------
    # Iteration 4: i = 3
    #
    # Current array:
    # [2, 12, 22, 77, 23]
    #
    # mini = 3 → arr[mini] = 77
    #
    # j = 4 → 23 < 77 → Yes → mini = 4
    #
    # Smallest element = 23 at index 4
    #
    # Swap arr[3] and arr[4]
    #
    # Array becomes:
    # [2, 12, 22, 23, 77]
    #
    # ------------------------------------------------

    # Assume the current index contains the minimum element
    mini = i

    # Find the index of the smallest element
    # in the unsorted part of the array
    for j in range(i + 1, len(arr)):

        if arr[j] < arr[mini]:
            mini = j

    # After finding the minimum element,
    # place it at its correct position
    arr[i], arr[mini] = arr[mini], arr[i]


print("--------------")
print("Sorted Array using Selection Sort:", arr)