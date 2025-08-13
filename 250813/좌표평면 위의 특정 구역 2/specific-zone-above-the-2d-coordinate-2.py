n = int(input())
points = [tuple(map(int, input().split())) for _ in range(n)]
x = [p[0] for p in points]
y = [p[1] for p in points]

# Please write your code here.
# 각 점들을 완전탐색 하면서 x,y의 최소 최대 값을 구해 직시각형 넓이를 구한다.
# 넓이의 값이 최소가 되는 값을 찾는다.


import sys

MIN_N = sys.maxsize

for i in range(n):

    min_x = sys.maxsize
    max_x = -sys.maxsize
    
    min_y = sys.maxsize
    max_y = -sys.maxsize

    for j in range(n):
        if i == j:
            continue
        
        min_x = min(min_x, x[j])
        max_x = max(max_x, x[j])

        min_y = min(min_y, y[j])
        max_y = max(max_y, y[j])
    
    MIN_N = min(MIN_N, abs(max_x-min_x)*abs(max_y-min_y))

print(MIN_N)

