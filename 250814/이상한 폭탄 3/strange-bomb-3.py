N, K = map(int, input().split())
num = [int(input()) for _ in range(N)]

# Please write your code here.

size = 1000000

import sys

max_n = -sys.maxsize

number = 0

for i in range(N-K):
    arr = num[i:i+K+1]

    dic = {}
    for elem in arr:
        if elem in dic:
            dic[elem] += 1
        else:
            dic[elem] = 1

    for n, cnt in dic.items():
        if max_n < cnt and cnt >= 2:
            number = n
            max_n = cnt
        elif max_n == cnt and cnt >= 2 and number < n:
            number = n  

print(number)