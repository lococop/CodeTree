n = int(input())
times = [tuple(map(int, input().split())) for _ in range(n)]
a = [t[0] for t in times]
b = [t[1] for t in times]

# Please write your code here.
# 한명씩 완전탐색 하면서 구간으로 배열에 표시해준다.
# 배열의 모든 합의 최댓값을 구한다.


import sys

MAX_N = -sys.maxsize

for i in range(n):

    arr = [0]*max(b)
    for j in range(n):
        if i == j:
            continue
        
        for k in range(a[j], b[j]):
            arr[k] = 1
        
        MAX_N = max(MAX_N, sum(arr))

        
print(MAX_N)