N = int(input())
seat = input()

# Please write your code here.
# N번 반복하면서 0인 자리에 인원을 추가한다.
# 반복문을 두 번 사용하면서 최근에 추가한 인원 왼쪽 오른쪽에 있는 사람과의 거리가 최소가 되는 값을 찾는다.
# 최소가 되는 값의 최댓값을 찾는 문제


import sys

max_d = -sys.maxsize


for person in range(N):

    if seat[person] == '1':  # 이미 사람이 있는 자리
        continue

    temp = list(map(int, seat))
    temp[person] = 1
    
    l_point = 0
    r_point = 0

    # 추가한 인원 기준 왼쪽에 있는 사람의 위치를 찾는다.
    for left in range(person-1, -1, -1):

        if temp[left] == 1:
            l_point = left
            break
    
    # 추가한 인원 기준 오른쪽에 있는 사람의 위치를 찾는다.
    for right in range(person+1, N):

        if temp[right] == 1:
            r_point = right
            break

    

    min_d = min(abs(person-l_point), abs(person-r_point))

    max_d = max(max_d, min_d)

print(max_d)