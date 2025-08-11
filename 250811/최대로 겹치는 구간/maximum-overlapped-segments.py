n = int(input())
segments = [tuple(map(int, input().split())) for _ in range(n)]

# Please write your code here.
import sys
max_n = -sys.maxsize

for elem in segments:
    if max_n < elem[1]:
        max_n = elem[1]

arr = [0]*max_n

for elem in segments:
    for j in range(elem[0],elem[1]):
        arr[j] += 1

print(max(arr))