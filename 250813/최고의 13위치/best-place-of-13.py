n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.

import sys

Max_Cnt = -sys.maxsize


for i in range(n):
    for j in range(n-2):
        Max_Cnt = max(Max_Cnt, grid[i][j] + grid[i][j+1] + grid[i][j+2])


print(Max_Cnt)