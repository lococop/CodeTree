a, b, c = map(int, input().split())

# Please write your code here.

import sys

def showMin(a, b, c):
    min_n = sys.maxsize
    
    if min_n > a:
        min_n = a
    if min_n > b:
        min_n = b
    if min_n > c:
        min_n = c
    return min_n

print(showMin(a,b,c))