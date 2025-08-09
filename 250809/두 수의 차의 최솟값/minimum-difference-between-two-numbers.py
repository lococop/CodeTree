N = int(input())

arr = list(map(int, input().split()))

import sys

min_n = sys.maxsize

for i in range(N):
    for j in range(i+1, N):
        if min_n > (arr[j] - arr[i]):
            min_n = arr[j] - arr[i]
print(min_n)