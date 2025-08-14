A, B, C = map(int, input().split())

# Please write your code here.

import sys

max_n = -sys.maxsize

for i in range(C//A+1):

    for j in range(C//B+1):

        sumAB = 0

        if A*i + B*j <= C:
            sumAB = A*i + B*j
        
        max_n = max(max_n, sumAB)


print(max_n)