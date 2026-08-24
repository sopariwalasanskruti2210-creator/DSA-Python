"""
Given an array of integers nums, sort the array in non-decreasing order
using the Bubble Sort algorithm.

A sorted array in non-decreasing order is an array where each element
is greater than or equal to all previous elements.
"""

print("Enter the array elements: ")

arr = list(map(int, input().split()))


# Bubble Sort
for i in range(len(arr)):

    # Bubble Sort works by comparing adjacent elements.
    #
    # If the left element is greater than the right element,
    # swap them.
    #
    # After every iteration, the largest element from the
    # unsorted part moves to its correct position at the end.
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
    # Compare adjacent elements:
    #
    # j = 0:
    # 22 > 2 → Yes → Swap
    # [2, 22, 12, 77, 23]
    #
    # j = 1:
    # 22 > 12 → Yes → Swap
    # [2, 12, 22, 77, 23]
    #
    # j = 2:
    # 22 > 77 → No → No swap
    #
    # j = 3:
    # 77 > 23 → Yes → Swap
    # [2, 12, 22, 23, 77]
    #
    # After Iteration 1:
    # The largest element (77) has moved to the end.
    #
    # [2, 12, 22, 23 | 77]
    #
    # ------------------------------------------------
    # Iteration 2: i = 1
    #
    # Current array:
    # [2, 12, 22, 23, 77]
    #
    # Compare only the unsorted part.
    # We don't need to check 77 because it is already sorted.
    #
    # j = 0:
    # 2 > 12 → No
    #
    # j = 1:
    # 12 > 22 → No
    #
    # j = 2:
    # 22 > 23 → No
    #
    # No swapping happened.
    #
    # This means the array is already sorted,
    # so we can stop early.

    # Assume no swapping happens in this iteration.
    swapped = False

    # Compare adjacent elements in the unsorted part.
    #
    # - i because after every iteration,
    #   one largest element reaches its correct position at the end.
    for j in range(len(arr) - 1 - i):

        # If the left element is greater than the right element,
        # they are in the wrong order.
        if arr[j] > arr[j + 1]:

            # Swap the adjacent elements.
            arr[j], arr[j + 1] = arr[j + 1], arr[j]

            # A swap happened in this iteration.
            swapped = True

            # Print array after every swap.
            print(arr)

    # If no swapping happened in the entire iteration,
    # the array is already sorted.
    if not swapped:
        break


print("Sorted Array:", arr)
