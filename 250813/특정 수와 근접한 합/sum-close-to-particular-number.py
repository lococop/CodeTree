N, S = map(int, input().split())
arr = list(map(int, input().split()))

# Please write your code here.

import sys

min_diff = sys.maxsize

# 

for i in range(N):

    
    temp = arr.copy()

    temp.pop(i)
    
    for j in range(N-1):
        
        total = 0
        temp1 = temp.copy()
        temp1.pop(j)

        for k in range(N-2):
            total += temp1[k]
    
        min_diff = min(min_diff, abs(S-total))

print(min_diff)
