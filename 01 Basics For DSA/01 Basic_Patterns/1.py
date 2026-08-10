'''
Given an integer n. 
You need to recreate the pattern given below for any value of N. 
Let's say for N = 5, the pattern should look like as below:

*****
*****
*****
*****
*****
'''
n = int(input("Enter a num : "))
for i in range(n+1):
    for j in range(n+1):
        print("*",end=" ")
    print()