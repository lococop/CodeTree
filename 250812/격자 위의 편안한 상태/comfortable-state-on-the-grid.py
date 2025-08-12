n, m = map(int, input().split())
points = [tuple(map(int, input().split())) for _ in range(m)]

# Please write your code here.
# N*N 2차원 배열을 선언한다.
# 칠해야할 좌표에 칠한 표시를 한다.
# 칠하면서 상하좌우에 칠해져 있는 좌표가 3개인지 확인하여 1 아니면 0을 출력한다.

paint_arr = [[0]*n for _ in range(n)]   # 2차원 배열 선언

dxs, dys = [0, 1, 0, -1],[1, 0, -1, 0]

# 유효한 범위의 좌표인지 확인
def in_range(x, y):
    return 1 <= x and x < n+1 and 1 <= y and y < n+1

for i in range(m):
    # 칠하는 표시는 1
    paint_arr[points[i][0]-1][points[i][1]-1] = 1
    
    # 칠해져 있는 횟수
    paint_cnt = 0
    # 상하좌우에 칠해져 있는지 확인
    for j in range(4):
        dx, dy = points[i][0] + dxs[j], points[i][1] + dys[j]
        if in_range(dx, dy) and paint_arr[dx-1][dy-1] == 1:
            paint_cnt += 1
    
    if paint_cnt == 3:
        print(1)
    else:
        print(0)

    

