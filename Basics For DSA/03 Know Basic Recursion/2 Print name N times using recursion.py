''' 
Print name N times using recursion
'''
def print_name(name,n):
    if(n==0):
        return 0

    print(name)
    print_name(name,n-1)

n = int(input("Enter a num till name should be printed : "))
name = input("Enter your name : ")
print_name(name,n)