"""
Given a string s, return true if the string is palindrome,
otherwise false.

A string is called palindrome if it reads the same
forward and backward.
"""


def is_palindrome(left, right, s):

    # Example:
    # s = "madam"
    #
    # left = 0, right = 4
    #
    # Step 1:
    # s[0] == s[4]
    # 'm' == 'm' → continue
    #
    # Step 2:
    # left = 1, right = 3
    # s[1] == s[3]
    # 'a' == 'a' → continue
    #
    # Step 3:
    # left = 2, right = 2
    #
    # left >= right
    # All characters matched → Palindrome

    # Base case:
    # If pointers meet or cross,
    # all characters have matched.
    if left >= right:
        return True

    # If characters don't match,
    # the string is not a palindrome.
    if s[left] != s[right]:
        return False

    # Move left forward and right backward
    return is_palindrome(left + 1, right - 1, s)


s = input("Enter a string: ")

result = is_palindrome(0, len(s) - 1, s)

if result:
    print(s, "is palindrome")
else:
    print(s, "is not palindrome")
