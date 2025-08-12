N = int(input())
arr = [int(input()) for _ in range(N)]

# Please write your code here.

import sys
Max_n = -sys.maxsize
cnt = 0

for i in range(N):
    if i == 0 or (arr[i] < 0 and arr[i-1] < 0) or (arr[i] > 0 and arr[i-1] > 0):
        cnt += 1
    
    if (arr[i] > 0 and arr[i-1] < 0) or (arr[i] > 0 and arr[i-1] < 0):
        cnt = 1
    
    if Max_n < cnt:
        Max_n = cnt

print(Max_n)