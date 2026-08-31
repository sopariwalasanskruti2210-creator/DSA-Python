'''
Given an array nums of n integers, where nums[i] represents the number of pages in the i-th book, 
and an integer m representing the number of students, allocate all the books to the students so that each student gets at least one book, 
each book is allocated to only one student, and the allocation is contiguous.
Allocate the books to m students in such a way that the maximum number of pages assigned to a student is minimized. 
If the allocation of books is not possible, return -1.
'''

# Count total num of books for given min distance
def booksCount(books,mid) :
    
    cnt = 1
    total = 0
    
    for pages in books : 
        
        # If it is in the range or mid or equla to mid then add it in total
        if total + pages <= mid :
            total += pages
            
        # Else start for next contingous part
        else :
            cnt += 1
            total = pages
            
            
    return cnt

def maxBooks(books,student) :
    
    low = max(books)
    high = sum(books)
    ans = 0
    
    if len(books) < student:
        return -1
    
    # Start binary search
    while low <= high :
        
        mid = (low + high)//2
        
        totalStudents = booksCount(books,mid)
        
        # Search in left half
        if totalStudents <= student :
            ans = mid
            high = mid - 1
        
        # Else search in right half
        else :
            low = mid + 1

    return ans


books = [12, 34, 67, 90]
student=2

res = maxBooks(books,student)
print(res)