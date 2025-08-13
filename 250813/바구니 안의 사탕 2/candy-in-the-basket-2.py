N, K = map(int, input().split())
candy = []
pos = []

for _ in range(N):
    c, p = map(int, input().split())
    candy.append(c)
    pos.append(p)

# Please write your code here.

size = 100
arr = [0]*(size+1)

for i in range(N):
    arr[pos[i]] += candy[i]


import sys
max_candy = -sys.maxsize

for i in range(size):
    sum_candy = 0
    for j in range(i-K, i+K+1):
        if j >= 0 and j <= size:
            sum_candy += arr[j]
    
    max_candy = max(max_candy, sum_candy)

print(max_candy)