n, t = map(int, input().split())
arr = list(map(int, input().split()))

# Please write your code here.

import sys
Max_n = -sys.maxsize

cnt = 0

for i in range(n):
    if arr[i] > t:
        cnt += 1
        Max_n = max(Max_n, cnt)
    else:
        cnt = 0
    



print(Max_n)