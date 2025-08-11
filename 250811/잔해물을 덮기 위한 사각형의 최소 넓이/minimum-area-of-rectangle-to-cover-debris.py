x1, y1, x2, y2 = [0] * 2, [0] * 2, [0] * 2, [0] * 2
x1[0], y1[0], x2[0], y2[0] = map(int, input().split())
x1[1], y1[1], x2[1], y2[1] = map(int, input().split())

# Please write your code here.

OFFSET = 1000
MAX_R = 2000
arr = [[0]*MAX_R for _ in range(MAX_R)]

for q in range(2):
    for i in range(x1[q]+OFFSET, x2[q]+OFFSET):
        for j in range(y1[q]+OFFSET, y2[q]+OFFSET):
            if q == 1:
                arr[i][j] = 2
            else:
                arr[i][j] = 1
import sys
max_x = -sys.maxsize
min_x = sys.maxsize
max_y = -sys.maxsize
min_y = sys.maxsize

for i in range(MAX_R):
    for j in range(MAX_R):
        if arr[i][j] == 1:
            if max_x < i:
                max_x = i
            if min_x > i:
                min_x = i
            if max_y < j:
                max_y = j
            if min_y > j:
                min_y = j

for i in range(min_x, max_x+1):
    for j in range(min_y, max_y+1):
        arr[i][j] = 1

sum1 = 0

for i in range(MAX_R):
    for j in range(MAX_R):
        if arr[i][j] == 1:
            sum1 += 1
print(sum1)


