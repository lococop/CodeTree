N, C, G, H = map(int, input().split())
ranges = [tuple(map(int, input().split())) for _ in range(N)]

# Please write your code here.

def work(tem, machine):
    if tem < ranges[machine][0]:
        return C
    elif ranges[machine][0] <= tem <= ranges[machine][1]:
        return G
    elif ranges[machine][1] < tem:
        return H

import sys
max_q = -sys.maxsize

for tem in range(0, 1001):
    sum_q = 0
    for machine in range(N):
        sum_q += work(tem, machine)
    max_q = max(max_q, sum_q)

print(max_q)