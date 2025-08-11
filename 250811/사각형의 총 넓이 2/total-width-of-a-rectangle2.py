n = int(input())
x1, y1, x2, y2 = [], [], [], []
for _ in range(n):
    a, b, c, d = map(int, input().split())
    x1.append(a)
    y1.append(b)
    x2.append(c)
    y2.append(d)

# Please write your code here.

OFFSET = 100
MAX_R = 200
arr = [[0]*MAX_R for _ in range(MAX_R)]

for x in range(2):
    for i in range(x1[x], x2[x]):
        for j in range(y1[x], y2[x]):
            arr[i][j] = 1

sum1 = 0
for i in range(MAX_R):
    for j in range(MAX_R):
        if arr[i][j] == 1:
            sum1 += 1
print(sum1)