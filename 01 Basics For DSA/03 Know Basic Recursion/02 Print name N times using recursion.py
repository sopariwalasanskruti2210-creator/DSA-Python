''' 
Print name N times using recursion
'''
def print_name(name,n):

    # Recursion uses the call stack.
    # For example:
    # name = "Sanskruti"
    # n = 5
    #
    # 5 -> print Sanskruti -> call function with 4
    # 4 -> print Sanskruti -> call function with 3
    # 3 -> print Sanskruti -> call function with 2
    # 2 -> print Sanskruti -> call function with 1
    # 1 -> print Sanskruti -> call function with 0 (base case)
    #
    # So when n becomes 0, the call stack looks like:
    #
    #         CALL STACK
    # ┌──────────────────────────────┐
    # │ print_name("Sanskruti", 0)   │ ← currently executing
    # ├──────────────────────────────┤
    # │ print_name("Sanskruti", 1)   │ ← waiting
    # ├──────────────────────────────┤
    # │ print_name("Sanskruti", 2)   │ ← waiting
    # ├──────────────────────────────┤
    # │ print_name("Sanskruti", 3)   │ ← waiting
    # ├──────────────────────────────┤
    # │ print_name("Sanskruti", 4)   │ ← waiting
    # ├──────────────────────────────┤
    # │ print_name("Sanskruti", 5)   │ ← first call
    # └──────────────────────────────┘
    #
    # Once n == 0, the base case is reached.
    # Then all the function calls return one by one.
    if(n==0):
        return 0

    print(name)
    print_name(name,n-1)

n = int(input("Enter a num till name should be printed : "))
name = input("Enter your name : ")
print_name(name,n)