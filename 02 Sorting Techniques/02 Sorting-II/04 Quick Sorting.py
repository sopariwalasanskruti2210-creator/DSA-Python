'''
Given an array of integers called nums, sort the array in non-decreasing
order using the Quick Sort algorithm.
'''

# Partition function:
# It selects a pivot and places it in its correct sorted position.
def partition(arr, low, high):

    # Choose the first element as the pivot.
    #
    # Example:
    # arr = [5, 2, 8, 4, 1]
    #
    # pivot = 5
    pivot = arr[low]

    # i searches from left to right
    # j searches from right to left
    i = low + 1
    j = high

    # Keep checking until both pointers cross.
    while i <= j:

        # Move i to the right while elements are
        # smaller than the pivot.
        while i <= high and arr[i] < pivot:
            i += 1

        # Move j to the left while elements are
        # greater than the pivot.
        while j >= low and arr[j] > pivot:
            j -= 1

        # If i and j have not crossed,
        # their elements are on the wrong sides
        # of the pivot, so swap them.
        if i < j:
            arr[i], arr[j] = arr[j], arr[i]

            # Move both pointers after swapping.
            i += 1
            j -= 1

    # Now j points to the correct position
    # where the pivot should be placed.
    #
    # Put the pivot in its correct position.
    arr[low], arr[j] = arr[j], arr[low]

    # Return the pivot's final index.
    return j


# Recursive Quick Sort
def quick_sort(arr, low, high):

    # Base case:
    # If there is one or zero elements,
    # that part is already sorted.
    if low < high:

        # Place pivot at its correct position.
        partition_index = partition(arr, low, high)

        # Sort the left part of the pivot.
        quick_sort(arr, low, partition_index - 1)

        # Sort the right part of the pivot.
        quick_sort(arr, partition_index + 1, high)


print("Enter the array:")

arr = list(map(int, input().split()))

quick_sort(arr, 0, len(arr) - 1)

print("Sorted Array:", arr)