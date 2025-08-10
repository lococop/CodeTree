n, m = map(int, input().split())

# Please write your code here.

import sys
def a(n,m):
    min_n = sys.maxsize
    for i in range(1, n*m+1):
        if i % n == 0 and i % m == 0 and min_n > i:
            min_n = i
    print(min_n)

a(n,m)
