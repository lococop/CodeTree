dirs = input()

# Please write your code here.
x, y = 0, 0

dx, dy = [1, 0, -1, 0], [0, -1, 0, 1]

if dirs[0] == 'L' and dirs[1] == 'F':
    x, y = x + dx[(3+3)%4], y + dy[(3+3)%4]
elif dirs[0] == 'R' and dirs[1] == 'F':
    x, y = x + dx[(3+1)%4], y + dy[(3+1)%4]

print(x, y)