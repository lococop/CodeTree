n, m = map(int, input().split())

# Please write your code here.
arr = [[0] * m for _ in range(n)]

num = 1
# 1. 첫 행에서 시작하는 대각선들
for start_col in range(m):
    r, c = 0, start_col
    while r < n and c >= 0:
        arr[r][c] = num
        num += 1
        r += 1
        c -= 1

# 2. 마지막 열에서 시작하는 대각선들 (첫 행 제외)
for start_row in range(1, n):
    r, c = start_row, m - 1
    while r < n and c >= 0:
        arr[r][c] = num
        num += 1
        r += 1
        c -= 1

# 출력
for row in arr:
    print(*row)