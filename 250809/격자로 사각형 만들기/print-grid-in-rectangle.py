N = int(input())

arr = [[0 for _ in range(N)] for _ in range(N)]

for i in range(N):
    arr[0][i] = 1
for j in range(N):
    arr[j][0] = 1

for i in range(1, N):
    for j in range(1, N):
        arr[i][j] = arr[i-1][j-1] + arr[i][j-1] + arr[i-1][j]

for row in arr:
    print(*row)