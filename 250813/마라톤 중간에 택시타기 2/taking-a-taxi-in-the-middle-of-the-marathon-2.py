n = int(input())
points = [tuple(map(int, input().split())) for _ in range(n)]
x = [p[0] for p in points]
y = [p[1] for p in points]

# Please write your code here.
# 첫 번째, 마지막을 제외한 좌표 중 하나를 빼고 인접 지점의 거리의 합이 최소가 되는 값을 찾는 문제


import sys

min_d = sys.maxsize

for i in range(1, n-1):

    temp_x, temp_y = x.copy(), y.copy()

    total_d = 0

    for j in range(1, n):
        if j == i:
            temp_x[j], temp_y[j] = temp_x[j+1], temp_y[j+1]

        total_d += abs(temp_x[j]-temp_x[j-1]) + abs(temp_y[j]-temp_y[j-1])

    min_d = min(min_d, total_d)

print(min_d)
    

