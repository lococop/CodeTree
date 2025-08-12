n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.
# dxs, dys 초기화
dxs, dys = [0, 1, 0, -1], [1, 0, -1, 0]

# 범위에 있는 좌표인지 확인하는 함수
def Is_Range(x, y):
    return 0 <= x and x < n and 0 <= y and y < n

# 최종적으로 인근값이 1인게 3개 이상인 좌표의 수
Total_Cnt = 0
for i in range(n):
    for j in range(n):
        cnt = 0
        for dx, dy in zip(dxs, dys):
            if Is_Range(i+dx, j+dy) and grid[i+dx][j+dy] == 1:
                cnt += 1
        if cnt >= 3:
            Total_Cnt += 1

print(Total_Cnt)