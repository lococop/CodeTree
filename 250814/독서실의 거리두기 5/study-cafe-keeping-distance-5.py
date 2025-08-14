import sys

N = int(input())
seat = input()

max_d = -sys.maxsize

for person in range(N):
    if seat[person] == '1':  # 이미 사람 있음
        continue

    temp = list(map(int, seat))
    temp[person] = 1

    # 불가능한 값으로 초기화
    l_point = -sys.maxsize
    r_point = sys.maxsize

    # 왼쪽 가장 가까운 사람
    for left in range(person - 1, -1, -1):
        if temp[left] == 1:
            l_point = left
            break

    # 오른쪽 가장 가까운 사람
    for right in range(person + 1, N):
        if temp[right] == 1:
            r_point = right
            break

    # 거리 계산 (한쪽이 없으면 그쪽 거리는 무한대라서 min에서 제외)
    dist_left = abs(person - l_point) if l_point != -sys.maxsize else sys.maxsize
    dist_right = abs(person - r_point) if r_point != sys.maxsize else sys.maxsize
    min_d = min(dist_left, dist_right)

    max_d = max(max_d, min_d)

print(0 if max_d == -sys.maxsize else max_d)
