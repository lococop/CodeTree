board = [list(input()) for _ in range(10)]

# Please write your code here.

L_x, L_y = 0, 0
R_x, R_y = 0, 0
B_x, B_y = 0, 0

for i in range(10):
    for j in range(10):

        if board[i][j] == 'L':
            L_x, L_y = i, j
        elif board[i][j] == 'R':
            R_x, R_y = i, j
        elif board[i][j] == 'B':
            B_x, B_y = i, j


if L_x == R_x == B_x and (L_y > R_y > B_y or L_y < R_y < B_y):
    if L_x + 1 >= 0 and L_x+1 < 9:
        L_x += 1
    else:
        L_x -= 1
elif L_y == R_y == B_y and (L_x > R_x > B_x or L_x < R_x < B_x):
    if L_y + 1 >= 0 and L_y+1 < 9:
        L_y += 1
    else:
        L_y -= 1


print(abs(L_x-B_x) + abs(L_y-B_y) - 1)

