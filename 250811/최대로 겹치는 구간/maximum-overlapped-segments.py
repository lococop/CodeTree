import sys

n = int(input())
segments = [tuple(map(int, input().split())) for _ in range(n)]

# 최대 끝점을 찾아서 배열의 크기를 정합니다.
max_end = 0
for start, end in segments:
    if end > max_end:
        max_end = end

# 배열의 크기를 최대 끝점 + 1로 설정하여 인덱스 에러를 방지합니다.
# 예를 들어 최대 끝점이 15라면, 인덱스 15에 접근할 수 있도록 크기를 16으로 만듭니다.
arr = [0] * (max_end + 1)

# 각 구간을 순회하며 배열에 값을 더합니다.
for start, end in segments:
    for i in range(start, end):
        arr[i] += 1

# 배열에서 최댓값을 찾아 출력합니다.
print(max(arr))