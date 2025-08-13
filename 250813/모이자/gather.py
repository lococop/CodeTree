n = int(input())
A = list(map(int, input().split()))

# Please write your code here.

import sys

Min_D = sys.maxsize


for i in range(n):

    sum_distance = 0
    for j in range(n):

        sum_distance += abs(i-j) * A[j]
        
    if Min_D > sum_distance:
        Min_D = sum_distance

print(Min_D)

