arr = list(map(int, input().split()))

import sys

max_n = -sys.maxsize
min_n = sys.maxsize

for elem in arr:
    if max_n < elem and elem < 500:
        max_n = elem
    if min_n > elem and elem > 500:
        min_n = elem

print(max_n, min_n)