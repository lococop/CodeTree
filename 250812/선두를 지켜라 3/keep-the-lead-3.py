N, M = map(int, input().split())

# Process A's movements
v = []
t = []
for _ in range(N):
    vi, ti = map(int, input().split())
    v.append(vi)
    t.append(ti)

# Process B's movements
v2 = []
t2 = []
for _ in range(M):
    vi, ti = map(int, input().split())
    v2.append(vi)
    t2.append(ti)

# Please write your code here.
# 동일위치에 있을 때도 선두로 인정
# 명예의 전당의 조합의 변화 횟수를 묻는 문제
# 1. 시간에 따른 위치정보 배열을 만든다.
# 2. 두 배열을 비교하면서 위치정보 조합이 이전이랑 다를 때 카운트 해준다.



Total_Time = sum(t) # 총 시간
A_Time = [0]*(Total_Time+1) # A 시간에 따른 위치정보 배열
B_Time = [0]*(Total_Time+1) # B 시간에 따른 위치정보 배열

# A 타임라인 배열 설정
time = 0
LocA = 0
for i in range(N):
    for j in range(time+1, time+t[i]+1):
        LocA += v[i]
        A_Time[j] = LocA
    time += t[i]

# B 타임라인 배열 설정
time = 0
LocB = 0
for i in range(M):
    for j in range(time+1, time+t2[i]+1):
        LocB += v2[i]
        B_Time[j] = LocB
    time += t2[i]

# 조합이 변화한 횟수
Change_cnt = 0 

# 두 배열을 비교하면서 위치정보가 가장 높은 사람을 명예의 전당에 추가한다.
for i in range(1, Total_Time+1):
    # 비교하면서 명예의 전당 업데이트
    if A_Time[i] > B_Time[i] and A_Time[i-1] <= B_Time[i-1]:
        Change_cnt += 1
    elif A_Time[i] < B_Time[i] and A_Time[i-1] >= B_Time[i-1]:
        Change_cnt += 1
    elif (A_Time[i-1] < B_Time[i-1] or A_Time[i-1] > B_Time[i-1]) and A_Time[i] == B_Time[i]:
        Change_cnt += 1
    
    
        

print(Change_cnt)
        