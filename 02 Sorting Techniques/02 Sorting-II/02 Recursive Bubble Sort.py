'''
Given an array of integers nums, sort the array in non-decreasing order
using the recursive Bubble Sort algorithm.
'''

def bubble_sort(arr, n):

    # Base case:
    # If only one element is left, it is already sorted.
    if n == 1:
        return

    # Assume no swapping happens in this pass
    did_swap = False

    # One Bubble Sort pass:
    # Compare adjacent elements from index 0 to n - 1.
    #
    # After this loop, the largest element among the
    # first n elements moves to index n - 1.
    for j in range(n - 1):

        # If left element is greater than right element,
        # swap them.
        if arr[j] > arr[j + 1]:

            arr[j], arr[j + 1] = arr[j + 1], arr[j]

            print(arr)

            # A swap happened
            did_swap = True

    # If no swaps happened, the array is already sorted,
    # so stop the recursion.
    if not did_swap:
        return

    # The largest element is now at index n - 1.
    # Recursively sort the remaining n - 1 elements.
    bubble_sort(arr, n - 1)


print("Enter array:")

arr = list(map(int, input().split()))

bubble_sort(arr, len(arr))

print("Sorted Array:", arr)