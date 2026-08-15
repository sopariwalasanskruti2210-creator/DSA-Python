'''
Given an array of intervals where intervals[i] = [starti, endi], merge all 
overlapping intervals and return an array of the non-overlapping intervals that cover all the intervals in the input.
You can return the intervals in any order.
'''
intervals = [[5,7],[1,3],[4,6],[8,10]]
intervals.sort()
ans = []
n = len(intervals)
for interval in intervals:

    if not ans or ans[-1][1]<interval[0]:
        ans.append(interval)
    else:
        ans[-1][1] = max(ans[-1][1],interval[1])

print(ans)
