n, t = map(int, input().split())
arr = list(map(int, input().split()))

# Please write your code here.

import sys
Max_n = -sys.maxsize

cnt = 0

for i in range(n):
    if i == 0 or (arr[i] > arr[i-1] and arr[i] > t and arr[i-1] > t):
        cnt += 1
    if (arr[i] < arr[i-1] or arr[i] < t):
        cnt = 1
    
    if Max_n < cnt:
        Max_n = cnt

print(Max_n)