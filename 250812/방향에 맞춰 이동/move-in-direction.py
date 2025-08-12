n = int(input())
moves = [tuple(input().split()) for _ in range(n)]
dir = [move[0] for move in moves]
dist = [int(move[1]) for move in moves]

# Please write your code here.
# 방향에 따라 특정 좌표값을 이동거리만큼 움직이게 하는 문제

# 처음 좌표
x, y = 0, 0
dx, dy = [1, 0, -1, 0], [0, -1, 0, 1]

# N번 명령을 실행한다.
for i in range(n):
    
    # 방향에 따라 특정 좌표값을 움직인다.
    if dir[i] == 'N':
        y += dy[3] * dist[i]
    elif dir[i] == 'W':
        x += dx[2] * dist[i]
    elif dir[i] == 'S':
        y += dy[1] * dist[i]
    elif dir[i] == 'E':
        x += dx[0] * dist[i]

print(x, y)