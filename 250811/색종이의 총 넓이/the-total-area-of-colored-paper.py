n = int(input())
points = [tuple(map(int, input().split())) for _ in range(n)]
x, y = zip(*points)
x, y = list(x), list(y)

# Please write your code here.
OFFSET = 100
MAX_R = 200
arr = [[0]*MAX_R for _ in range(MAX_R)]

for q in range(n):
    for i in range(x[q]+OFFSET, x[q]+8+OFFSET):
        for j in range(y[q]+OFFSET, y[q]+8+OFFSET):
            arr[i][j] = 1

sum1 = 0
for i in range(MAX_R):
    for j in range(MAX_R):
        if arr[i][j] == 1:
            sum1 += 1
print(sum1)