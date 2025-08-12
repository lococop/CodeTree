n, m = map(int, input().split())
arr = [[0] * m for _ in range(n)]

# Please write your code here.

dxs, dys = [0, 1, 0, -1], [1, 0, -1, 0]

x, y = 1, 1

arr[x-1][y-1] = 1


def in_range(x, y):
    return 1 <= x and x < n+1 and 1 <= y and y < m+1

move_dir = 0

for i in range(2, n*m+1):

    dx, dy = x + dxs[move_dir], y + dys[move_dir]
    if not in_range(dx, dy) or arr[dx-1][dy-1] != 0:
        move_dir = (move_dir+1) % 4
    
    x, y = x + dxs[move_dir], y + dys[move_dir]
    arr[x-1][y-1] = i

for i in range(n):
    for j in range(m):
        print(arr[i][j], end = " ")
    print()