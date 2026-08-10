'''
Given a string s, return true if the string is palindrome, otherwise false.
A string is called palindrome if it reads the same forward and backward.
'''
def rev_str(left,right,s):
  if(left>=right):
    return True

  if(s[left]!=s[right]):
    return False

  return rev_str(left+1,right-1,s)

s = input("Enter a string : ")
reverse = rev_str(0,len(s)-1,s)
if(reverse):
  print(s," is palindrome")
else:
  print(s," is not palindrome")