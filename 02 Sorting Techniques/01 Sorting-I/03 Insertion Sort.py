"""
Given an array of integers nums, sort the array in non-decreasing order
using the Insertion Sort algorithm.

A sorted array in non-decreasing order is an array where each element
is greater than or equal to all previous elements.
"""

print("Enter the array elements: ")
arr = list(map(int, input().split()))

# Insertion Sort
for i in range(len(arr)):

    # Insertion Sort assumes that the left part of the array
    # is already sorted.
    #
    # We take the current element at index i and move it
    # towards the left until it reaches its correct position.
    #
    # Example:
    # arr = [22, 2, 12, 77, 23]
    #
    # ------------------------------------------------
    # Iteration 1: i = 0
    #
    # Current element = 22
    #
    # There is no element on the left side.
    #
    # Sorted part:
    # [22]
    #
    # ------------------------------------------------
    # Iteration 2: i = 1
    #
    # Current array:
    # [22, 2, 12, 77, 23]
    #
    # Current element:
    # arr[1] = 2
    #
    # Compare:
    # arr[0] > arr[1]
    # 22 > 2 → Yes → Swap
    #
    # Array becomes:
    # [2, 22, 12, 77, 23]
    #
    # Now 2 is at its correct position.
    #
    # Sorted part:
    # [2, 22]
    #
    # ------------------------------------------------
    # Iteration 3: i = 2
    #
    # Current element = 12
    #
    # Current array:
    # [2, 22, 12, 77, 23]
    #
    # Compare:
    # 22 > 12 → Yes → Swap
    #
    # Array:
    # [2, 12, 22, 77, 23]
    #
    # Compare again:
    # 2 > 12 → No
    #
    # 12 is now at its correct position.
    #
    # Sorted part:
    # [2, 12, 22]
    #
    # ------------------------------------------------
    # Iteration 4: i = 3
    #
    # Current element = 77
    #
    # Compare:
    # 22 > 77 → No
    #
    # No movement needed.
    #
    # Sorted part:
    # [2, 12, 22, 77]
    #
    # ------------------------------------------------
    # Iteration 5: i = 4
    #
    # Current element = 23
    #
    # Current array:
    # [2, 12, 22, 77, 23]
    #
    # Compare:
    # 77 > 23 → Yes → Swap
    #
    # [2, 12, 22, 23, 77]
    #
    # Compare again:
    # 22 > 23 → No
    #
    # 23 is now at its correct position.
    #
    # Final sorted array:
    # [2, 12, 22, 23, 77]

    # Start comparing the current element
    # with elements on its left.
    j = i

    # Keep moving left while:
    #
    # 1. j is greater than 0, so a left element exists.
    # 2. The left element is greater than the current element.
    while j > 0 and arr[j - 1] > arr[j]:

        # Swap the current element with the larger
        # element on its left.
        arr[j - 1], arr[j] = arr[j], arr[j - 1]

        # Move one position towards the left.
        j -= 1


print("Sorted Array:", arr)
