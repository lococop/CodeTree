n = int(input())
a = [int(input()) for _ in range(n)]

# Please write your code here.
import sys

min_d = sys.maxsize

for i in range(n):

    total_d = 0
    cnt = 1
    for _ in range(n-1):
        total_d += cnt*a[(i+cnt)%n]
        cnt += 1
    
    min_d = min(min_d, total_d)

print(min_d)
