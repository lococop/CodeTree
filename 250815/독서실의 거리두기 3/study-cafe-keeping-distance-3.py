N = int(input())
seats = list(input())

# Please write your code here.

# 거리가 가장 먼 쌍을 찾는다.
# 순회하면서 1이 처음 나오면 시작점으로 설정
# 그다음 1이 나오면 거리 계산 후 쌍 저장 및 시작점 재설정
# 최종적으로 거리가 먼 쌍 가운데에 1 설정 후 양쪽 점 중 가까운 사람과의 거리를 구하는 문제

max_d = 0

first, second = -1, -1

for i in range(N):

    if seats[i] == '1':

        for j in range(i+1, N):
            if seats[j] == '1':

                if j-i > max_d:
                    max_d = j-i

                    first, second = i, j
                break

seats[(first+second)//2] = '1'

import sys
ans = sys.maxsize

for i in range(N):
    if seats[i] == '1':
        for j in range(i+1, N):
            if seats[j] == '1':
                ans = min(ans, j-i)

                break

print(ans)




