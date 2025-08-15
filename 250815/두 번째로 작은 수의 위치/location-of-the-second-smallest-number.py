n = int(input())
a = list(map(int, input().split()))

# Please write your code here.
import sys

second_n = sys.maxsize
second_i = -1

for num in range(n):

    if abs(a[num]-min(a)) < second_n and abs(a[num]-min(a)) > 0:
        second_n = abs(a[num]-min(a))
        second_i = num+1

cnt = 0
for elem in a:
    if elem == a[second_i-1]:
        cnt += 1

if cnt >= 2:
    print(-1)
elif cnt == 1:
    print(second_i)