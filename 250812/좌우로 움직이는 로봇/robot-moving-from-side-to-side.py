n, m = map(int, input().split())

# Process robot A's movements
t = []
d = []
for _ in range(n):
    time, direction = input().split()
    t.append(int(time))
    d.append(direction)

# Process robot B's movements
t_b = []
d_b = []
for _ in range(m):
    time, direction = input().split()
    t_b.append(int(time))
    d_b.append(direction)

# Please write your code here.
# 위치가 저장된 배열을 순회하면서 위치정보가 같아지는 순간의 횟수를 구한다.

# 시간에 따른 위치정보 배열
MAX_T = max(sum(t), sum(t_b))   # 최대 움직이는 시간
A_Location = [0]*(MAX_T+1)
B_Location = [0]*(MAX_T+1)



LocA = 0
time = 0
for i in range(n):
    if d[i] == 'R':
        for j in range(time+1, time+t[i]+1):
            LocA += 1
            A_Location[j] = LocA
        time += t[i]
    elif d[i] == 'L':
        for j in range(time+1, time+t[i]+1):
            LocA -= 1
            A_Location[j] = LocA
        time += t[i]
for i in range(time+1, MAX_T+1):
    A_Location[i] = LocA


LocB = 0
timeB = 0
for i in range(m):
    if d_b[i] == 'R':
        for j in range(timeB+1, timeB+t_b[i]+1):
            LocB += 1
            B_Location[j] = LocB
        timeB += t_b[i]
    elif d_b[i] == 'L':
        for j in range(timeB+1, timeB+t_b[i]+1):
            LocB -= 1
            B_Location[j] = LocB
        timeB += t_b[i]
for i in range(timeB+1, MAX_T+1):
    B_Location[i] = LocB


move_cnt = 0



for i in range(2, MAX_T+1):

    if A_Location[i] == B_Location[i] and A_Location[i-1] != B_Location[i-1]:
        move_cnt += 1


print(move_cnt)



