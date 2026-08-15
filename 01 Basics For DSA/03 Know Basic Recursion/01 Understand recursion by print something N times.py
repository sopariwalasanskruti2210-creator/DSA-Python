'''
Understand recursion by print something N times
'''
def print_num(n):
    if(n==0):
        return 0
    print(n)
    print_num(n-1)

x=int(input("Enter a num : "))
print_num(x)