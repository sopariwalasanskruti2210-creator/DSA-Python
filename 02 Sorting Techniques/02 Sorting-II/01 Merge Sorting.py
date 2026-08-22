'''
Given an array of integers nums, sort the array in non-decreasing order
using the Merge Sort algorithm.

A sorted array in non-decreasing order is an array where each element is
greater than or equal to all previous elements.
'''

# This function merges two already sorted parts of the array.
def merge(arr, low, mid, high):

    # left pointer starts from the first half
    # right pointer starts from the second half
    left, right = low, mid + 1

    # Temporary array to store the merged sorted elements
    temp = []

    # Compare elements from both sorted halves.
    #
    # Example:
    # Left half  = [2, 5]
    # Right half = [1, 4, 8]
    #
    # Compare:
    # 2 vs 1 → add 1
    # 2 vs 4 → add 2
    # 5 vs 4 → add 4
    # 5 vs 8 → add 5
    #
    # Then add the remaining element: 8
    #
    # temp = [1, 2, 4, 5, 8]

    while left <= mid and right <= high:

        # Add the smaller element to temp
        if arr[left] < arr[right]:
            temp.append(arr[left])
            left += 1

        else:
            temp.append(arr[right])
            right += 1


    # If elements are remaining in the left half,
    # add all of them to temp.
    while left <= mid:
        temp.append(arr[left])
        left += 1


    # If elements are remaining in the right half,
    # add all of them to temp.
    while right <= high:
        temp.append(arr[right])
        right += 1


    # Copy the sorted elements from temp
    # back into the original array.
    #
    # i goes from low to high
    # temp[i - low] gives the correct index in temp
    # temp starts from index 0, but arr starts from index low.
	# So we use i - low to get the correct temp index.
	#
	# Example: low = 3
	# arr[3] = temp[0]
	# arr[4] = temp[1]
	# arr[5] = temp[2]
    for i in range(low, high + 1):
        arr[i] = temp[i - low]


# Recursive Merge Sort function
def merge_sort(arr, low, high):

    # Base case:
    # If there is only one element or no element,
    # it is already sorted.
    if low >= high:
        return

    # Find the middle index
    mid = (low + high) // 2

    # Divide the left half
    merge_sort(arr, low, mid)

    # Divide the right half
    merge_sort(arr, mid + 1, high)

    # Merge both sorted halves
    merge(arr, low, mid, high)


arr = [5, 2, 8, 4, 1]

# Sort the complete array
merge_sort(arr, 0, len(arr) - 1)

print("Sorted Array:", arr)