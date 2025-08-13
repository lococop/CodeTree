N, K = map(int, input().split())
num = [int(input()) for _ in range(N)]

# Please write your code here.
import sys

max_n = -sys.maxsize

if N == K:
    K = N-1
    

for i in range(N-(K+1)+1):
    for j in range(i, i+K+1):
        if num[i:i+K+1].count(num[j]) >= 2:
            max_n = max(max_n, num[j])

if max_n == -sys.maxsize:
    print(-1)
else:
    print(max_n)
