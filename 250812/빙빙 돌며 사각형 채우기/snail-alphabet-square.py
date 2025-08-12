n, m = map(int, input().split())

# Please write your code here.

dxs, dys = [0, 1, 0, -1], [1, 0, -1, 0]

arr = [[0]*m for _ in range(n)]

x, y = 0, 0

move_dir = 0

arr[x][y] = 'A'

def in_range(x, y):
    return 0 <= x and x < n and 0 <= y and y < m

char = 66


for _ in range(2, n*m+1):
    dx, dy = x + dxs[move_dir], y + dys[move_dir]
    if not in_range(dx,dy) or arr[dx][dy] != 0:
        move_dir = (move_dir+1) % 4
    
    x, y = x + dxs[move_dir], y + dys[move_dir]
    arr[x][y] = chr(char)
    char += 1
    if char == 91:
        char = 65

for i in range(n):
    for j in range(m):
        print(arr[i][j], end = " ")
    print()
    