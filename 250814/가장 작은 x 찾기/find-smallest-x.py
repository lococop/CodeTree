n = int(input())
ranges = [tuple(map(int, input().split())) for _ in range(n)]
a, b = zip(*ranges)
a, b = list(a), list(b)

# Please write your code here.

import sys

min_n = sys.maxsize

for num in range(min(a), max(b)):

    temp = num*2
    for i in range(n):

        if a[i] > temp or temp > b[i]:
            continue
        
        temp *= 2

        if i == n-1:
            
            min_n = min(min_n, num)


print(min_n)
    
        
        
