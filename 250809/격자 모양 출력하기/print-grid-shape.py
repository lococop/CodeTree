N, M = map(int, input().split())
arr = [[0]*N for _ in range(N)]

for i in range(M):
    a, b = map(int, input().split())

    arr[a-1][b-1] = a*b

for row in arr:
    print(*row)