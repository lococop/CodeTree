x1 = [0] * 3
y1 = [0] * 3
x2 = [0] * 3
y2 = [0] * 3

x1[0], y1[0], x2[0], y2[0] = map(int, input().split())
x1[1], y1[1], x2[1], y2[1] = map(int, input().split())
x1[2], y1[2], x2[2], y2[2] = map(int, input().split())

# Please write your code here.

OFFSET = 1000
MAX_R = 2000
arr = [[0]*MAX_R for _ in range(MAX_R)]

for q in range(3):
    for i in range(x1[q], x2[q]):
        for j in range(y1[q], y2[q]):
            arr[i][j] = 1
            if q == 2:
                arr[i][j] =0

sum1 = 0
for i in range(MAX_R):
    for j in range(MAX_R):
        if arr[i][j] == 1:
            sum1 += 1

print(sum1)
            

