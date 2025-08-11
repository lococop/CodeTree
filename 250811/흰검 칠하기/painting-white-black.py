n = int(input())
commands = [tuple(input().split()) for _ in range(n)]
x = []
dir = []
for num, direction in commands:
    x.append(int(num))
    dir.append(direction)

# Please write your code here.

OFFSET = 10000
MAX_R = 20000
arr = [[0, 0, 0] for _ in range(MAX_R+1)]

cnt = 0
if dir[0] == 'L':
    cnt = 1
for i in range(n):
    if dir[i] == 'R':
        for j in range(cnt+OFFSET, cnt+OFFSET+x[i]):
            arr[j][0] = 1
            arr[j][1] += 1
            if arr[j][1] >= 2 and arr[j][2] >= 2:
                arr[j][0] = 3   # 3은 회색
            cnt += 1
    elif dir[i] == 'L':
        for j in range(cnt+OFFSET-1, cnt+OFFSET-x[i]-1, -1):
            arr[j][0] = 2
            arr[j][2] += 1
            if arr[j][1] >= 2 and arr[j][2] >= 2:
                arr[j][0] = 3   # 3은 회색 
            cnt -= 1
black = 0
white = 0
gray = 0

for elem in arr:
    if elem[0] == 1:
        black += 1
    elif elem[0] == 2:
        white += 1
    elif elem[0] == 3:
        gray += 1

print(white, black, gray)


