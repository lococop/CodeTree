N = int(input())
moves = [tuple(input().split()) for _ in range(N)]
dir = [move[0] for move in moves]
dist = [int(move[1]) for move in moves]

# Please write your code here.
first_x, first_y = 0, 0
x, y = 0, 0

dxs, dys = [0, 1, 0, -1], [1, 0, -1, 0]

mapper = {
    "E" : 0,
    "S" : 1,
    "W" : 2,
    "N" : 3
}

move_dir = 0
time = 0
Is = False
for i in range(N):
    # 방향 설정
    move_dir = mapper[dir[i]]

    for j in range(dist[i]):
        x, y = x + dxs[move_dir], y + dys[move_dir]
        time += 1
        if x == first_x and y == first_y:
            Is = True
            break
    if Is:
        break

if not Is:
    print(-1)
else:
    print(time)