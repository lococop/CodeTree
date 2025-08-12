dirs = input()

# Please write your code here.
x, y = 0, 0

D = 3

dx, dy = [1, 0, -1, 0], [0, -1, 0, 1]


for i in range(len(dirs)):
    if dirs[i] == 'L':
        D = (D+3)%4
    elif dirs[i] == 'R':
        D = (D+1)%4
    elif dirs[i] == 'F':
        x, y = x + dx[D], y + dy[D]
    

print(x, y)