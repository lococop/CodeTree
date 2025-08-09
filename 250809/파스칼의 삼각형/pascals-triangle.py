N = int(input())

arr = [[0 for _ in range(N)] for _ in range(N)]
arr[0][0] = 1

for i in range(N):
    for j in range(i+1):
        if i >= 1 and j >= 1:
            arr[i][j] = arr[i-1][j-1] + arr[i-1][j]
        elif i >= 1 and j < 1:
            arr[i][j] = arr[i-1][j]


for i in range(N):
    for j in range(i+1):
        print(arr[i][j], end = " ")
    print()