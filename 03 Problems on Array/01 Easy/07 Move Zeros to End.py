"""
Given an integer array nums, move all the 0's to the end of the array.
The relative order of the other elements must remain the same.
This must be done in place, without making a copy of the array.
"""

nums = [1, 2, 0, 0, 3, 4]
left = 0

for right in range(len(nums)):

    # Search element 0 element using right if we find any then swap it with left
    # for this example :
    # i = 0 => nums[right] != 0 => left = 0 => swaped with element itself
    # i = 1 => nums[right] != 0 => left = 1 => swaped with element itself
    # i = 2 => nums[right] == 0 => left = 1
    # i = 3 => nums[right] == 0 => left = 1
    # i = 4 => nums[right] != 0 => swap(left,right) = (right,left) => (3,0) = (0,3) => nums = [1,2,3,0,0,4] => left = 3
    # i = 5 => nums[right] != 0 => swap(0,4) = (4,0) => nums = [1,2,3,4,0,0] => left = 4
    if nums[right] != 0:
        nums[left], nums[right] = nums[right], nums[left]
        left += 1

print(nums)
