n, k = map(int, input().split())
x = []
c = []
for _ in range(n):
    pos, char = input().split()
    x.append(int(pos))
    c.append(char)

# Please write your code here.
# 크기가 10001인 배열에 각 위치에 알파벳을 넣는다.
# K 크기의 영역으로 1씩 증가하면서 그 영역에 알파벳에 따른 점수의 합이 최대가 되는 값을 찾는 문제

size = 10001
arr = [0]*size

# 배열 안에 위치에 맞는 값을 할당
for i in range(n):
    arr[x[i]] = c[i]

import sys
max_score = -sys.maxsize


for i in range(1, max(x)+2-k):

    total = 0
    for j in range(i, i+k+1):
        if arr[j] == 'G':
            total += 1
        elif arr[j] == 'H':
            total += 2
        
    max_score = max(max_score, total)

print(max_score)