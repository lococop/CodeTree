n = int(input())
people = [tuple(input().split()) for _ in range(n)]
pos = [int(p[0]) for p in people]
alpha = [p[1] for p in people]

# Please write your code here.

size = 100
arr = ['0']*(size+1)

for i in range(n):
    arr[pos[i]] = alpha[i]

import sys
max_size = -sys.maxsize

for i in range(size):

    for j in range(i+1, size):

        cntG = 0
        cntH = 0

        min_x = sys.maxsize
        max_x = -sys.maxsize
        for k in range(i, j):
            if arr[k] == 'G':
                cntG += 1
                min_x = min(min_x, k)
                max_x = max(max_x, k)
            elif arr[k] == 'H':
                cntH += 1
                min_x = min(min_x, k)
                max_x = max(max_x, k)
        
        if (cntG == cntH and cntG != 0) or (cntG > 0 and cntH == 0) or (cntH > 0 and cntG == 0):

            max_size = max(max_size, max_x-min_x)

if max_size == -sys.maxsize:
    print(0)
else:
    print(max_size)
        