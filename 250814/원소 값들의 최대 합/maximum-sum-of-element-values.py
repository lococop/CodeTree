n, m = map(int, input().split())
arr = [0] + list(map(int, input().split()))

# Please write your code here.
# 시작위치를 0부터 n까지 반복하면서 m번의 움직임의 결과가 가장 큰 값을 찾는 문제
import sys

max_n = -sys.maxsize

for start in range(n):

    point = start

    total_sum = 0

    for num in range(m):

        # 위치에 대한 값 합산
        total_sum += arr[point]

        # 위치 값 갱신
        point = arr[point] - 1
    
    max_n = max(max_n, total_sum)

print(max_n)