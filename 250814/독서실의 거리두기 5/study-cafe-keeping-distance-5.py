import sys

N = int(input())
seat = input()

max_d = -sys.maxsize

for person in range(N):
    if seat[person] == '1':  # 이미 사람 있음
        continue

    temp = list(map(int, seat))
    temp[person] = 1

    # 왼쪽 가장 가까운 사람
    l_point = -1
    for left in range(person - 1, -1, -1):
        if temp[left] == 1:
            l_point = left
            break

    # 오른쪽 가장 가까운 사람
    r_point = -1
    for right in range(person + 1, N):
        if temp[right] == 1:
            r_point = right
            break

    # 거리 계산
    if l_point == -1 and r_point == -1:
        continue  # 사람 한 명도 없는 경우
    elif l_point == -1:
        min_d = r_point - person
    elif r_point == -1:
        min_d = person - l_point
    else:
        min_d = min(person - l_point, r_point - person)

    max_d = max(max_d, min_d)

print(0 if max_d == -sys.maxsize else max_d)
