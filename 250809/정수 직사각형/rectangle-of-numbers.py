N, M = map(int, input().split())

arr = [[0 for _ in range(M)] for _ in range(N)]

cnt = 1
for i in range(N):
    for j in range(M):
        arr[i][j] = cnt
        cnt += 1

for i in range(N):
    for j in range(M):
        print(arr[i][j], end = " ")
    print()