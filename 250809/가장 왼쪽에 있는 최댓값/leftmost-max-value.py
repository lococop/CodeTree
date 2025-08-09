n = int(input())
a = list(map(int, input().split()))

# Please write your code here.
import sys

arr = []
max_n = 0
idx = -1

while True:
    if idx == 0:
        break

    max_n = max(a)
    idx = a.index(max_n)
    arr.append(idx+1)
    
    a = a[:a.index(max_n)]

for elem in arr:
    print(elem, end = " ")