n = int(input())
a = list(map(int, input().split()))

# Please write your code here.

import sys

max_n = -sys.maxsize

for k in range(1, 101):
    cnt = 0


    for i in range(n):
        for j in range(i+1, n):
            if a[j]-k == k-a[i]:
                cnt += 1
    max_n = max(max_n, cnt)

print(max_n)