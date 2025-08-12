n, m = map(int, input().split())

# Please write your code here.
arr = [[0]*m for _ in range(n)]

dxs, dys = [1, 0, -1, 0], [0, 1, 0, -1]

move_dir = 0

x, y = 0, 0

arr[x][y] = 1

def in_range(x, y):
    return 0 <= x and x < n and 0 <= y and y < m

for num in range(2, n*m+1):
    
    dx, dy = x + dxs[move_dir], y + dys[move_dir]
    if not in_range(dx, dy) or arr[dx][dy] != 0:
        move_dir = (move_dir + 1) % 4
    
    x, y = x + dxs[move_dir], y + dys[move_dir]
    arr[x][y] = num

for i in range(n):
    for j in range(m):
        print(arr[i][j], end = " ")
    print()
        


    