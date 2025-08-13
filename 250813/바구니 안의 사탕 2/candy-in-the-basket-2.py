N, K = map(int, input().split())
candy = []
pos = []

for _ in range(N):
    c, p = map(int, input().split())
    candy.append(c)
    pos.append(p)

# Please write your code here.

arr = [0]*101

for i in range(N):
    arr[pos[i]] = candy[i]

import sys
max_candy = -sys.maxsize

for i in range(1, max(pos)-K*2+1):

    sum_candy = 0
    for j in range(i, i+2*K+1):
        sum_candy += arr[j]
    
    max_candy = max(max_candy, sum_candy)

print(max_candy)