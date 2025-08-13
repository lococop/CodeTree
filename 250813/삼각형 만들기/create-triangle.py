n = int(input())
points = [tuple(map(int, input().split())) for _ in range(n)]
x = [p[0] for p in points]
y = [p[1] for p in points]

# Please write your code here.
# x축에 평행하려면? -> y좌표가 동일해야함, y축에 평행하려면? -> x좌표가 동일해야함
# 점 3개를 조합하면서 각각 다른 두 점만 x, y 가 동일하면서 넓이가 제일 큰 값을 찾고 2를 곱해주는 문제
# 삼각형 넓이 구하는 법 -> 최소 최대 x,y 값의 곱

import sys


MAX_N = -sys.maxsize


for i in range(n):
    for j in range(i+1, n):
        
        min_x = sys.maxsize
        max_x = -sys.maxsize

        min_y = sys.maxsize
        max_y = -sys.maxsize

        for k in range(j+1, n):

            if (x[i] == x[j] or x[i] == x[k] or x[j] == x[k]) and (y[i] == y[j] or y[i] == y[k] or y[j] == y[k]):
                min_x = min(min_x, x[i],x[j],x[k])
                max_x = max(max_x, x[i],x[j],x[k])

                min_y = min(min_y, y[i],y[j],y[k])
                max_y = max(max_y, y[i],y[j],y[k])
            
                MAX_N = max(MAX_N, abs(max_x-min_x)*abs(max_y-min_y))



print(MAX_N)
