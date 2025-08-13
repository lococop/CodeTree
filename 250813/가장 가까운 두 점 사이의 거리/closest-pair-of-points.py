n = int(input())
points = [tuple(map(int, input().split())) for _ in range(n)]
x = [p[0] for p in points]
y = [p[1] for p in points]

# Please write your code here.
# 점을 두 개씩 빼서 거리가 가장 짧은 점들을 골라 제곱을 해준다.
import sys

min_d = sys.maxsize
for i in range(n):
    for j in range(i+1, n):

        min_d = min(min_d, abs(x[i]-x[j])**2 + abs(y[i]-y[j])**2)

print(min_d)
