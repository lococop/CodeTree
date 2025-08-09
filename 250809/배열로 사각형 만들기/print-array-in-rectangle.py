arr = [[0]*5 for _ in range(5)]

for i in range(5):
    arr[0][i] = 1

for i in range(1, 5):
    for j in range(5):
        if j >= 1:
            arr[i][j] = arr[i-1][j] + arr[i][j-1]
        else:
            arr[i][j] = arr[i-1][j]

for row in arr:
    print(*row)