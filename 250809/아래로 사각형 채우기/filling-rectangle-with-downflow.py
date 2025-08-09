N = int(input())

arr = [[0 for _ in range(N)] for _ in range(N)]

cnt = 1
for j in range(N):
    for i in range(N):
        arr[i][j] = cnt
        cnt += 1

for i in range(N):
    for j in range(N):
        print(arr[i][j], end = " ")
    print()