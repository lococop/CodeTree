n = int(input())
commands = [tuple(input().split()) for _ in range(n)]
x = []
dir = []
for num, direction in commands:
    x.append(int(num))
    dir.append(direction)

# Please write your code here.

OFFSET = 100000
MAX_R = 200000
arr = [0] * (MAX_R + 1)

cnt = 0

for i in range(n):
    if dir[i] == 'R':
        for j in range(cnt+OFFSET, cnt+OFFSET+x[i]):
            arr[j] = 1
        cnt += x[i]-1

    elif dir[i] == 'L':
        for j in range(cnt+OFFSET, cnt+OFFSET-x[i], -1):
            arr[j] = 2
        cnt -= x[i]-1
black = 0
white = 0

for elem in arr:
    if elem == 1:
        black += 1
    elif elem == 2:
        white += 1


print(white, black)

