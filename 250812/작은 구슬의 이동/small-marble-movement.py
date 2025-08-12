n, t = map(int, input().split())
r, c, d = input().split()
r, c = int(r), int(c)

# Please write your code here.

dxs, dys = [0, 1, -1, 0], [1, 0, 0, -1]

x, y = r, c

mapper = {
    "U" : 2,
    "D" : 1,
    "R" : 0,
    "L" : 3
}

def in_range(x, y):
    return 1 <= x and x < n+1 and 1 <= y and y < n+1

# 방향을 숫자로 변환
direction = mapper[d]

for i in range(t):
    # 증가된 좌표가 유효한지 확인 후 유효 하면 이동
    dx, dy = x + dxs[direction], y + dys[direction]
    if in_range(dx, dy):
        x, y = dx, dy
    # 유효하지 않은 좌표이면 방향만 바꿔준다.
    else:
        direction = 3 - direction

print(x, y)



