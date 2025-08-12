n = int(input())
arr = [int(input()) for _ in range(n)]

# Please write your code here.
import sys

Max_n = -sys.maxsize
cnt = 1
for i in range(n):
    if arr[i] == arr[i-1]:
        cnt += 1
    if arr[i] != arr[i-1]:
        cnt = 1
    if Max_n < cnt:
        Max_n = cnt


print(Max_n)



