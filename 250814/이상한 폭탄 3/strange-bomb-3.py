N, K = map(int, input().split())
num = [int(input()) for _ in range(N)]

# Please write your code here.

size = 1000000

import sys

max_n = -sys.maxsize

for n in range(size+1):
    
    for i in range(N-K+1):

        cnt = 0
        for j in range(i, i+K):
            if n == num[j]:
                cnt += 1
        
        max_n = max(max_n, cnt)

if max_n == -sys.maxsize:
    print(0)
else:
    print(max_n)