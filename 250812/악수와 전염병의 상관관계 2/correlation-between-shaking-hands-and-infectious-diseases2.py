N, K, P, T = map(int, input().split())
handshakes = [tuple(map(int, input().split())) for _ in range(T)]

# Please write your code here.
# 개발자 악수 클래스 생성 - 시간, A, B
class Developer:
    def __init__(self, time, A, B):
        self.time = time
        self.A = A
        self.B = B

result = [0]*N  # 개발자 음성 양성 여부
result[P-1] = 1 # 첫 감염자 음성 설정

# 개발자 악수 객체 배열 생성
Developer_Arr = [
    Developer(handshakes[i][0], handshakes[i][1], handshakes[i][2]) for i in range(T)
]

# 시간 순으로 정렬
Developer_Arr.sort(key=lambda x:x.time)

# 감염자 리스트
Infect_P = [P]
HandLimit = [K]*N
for i in range(T):
    if Developer_Arr[i].A in Infect_P or Developer_Arr[i].B in Infect_P:    # 감염자 리스트에 A,B가 있다면
        
        if Developer_Arr[i].A in Infect_P and Developer_Arr[i].B in Infect_P:      # 둘 다 감염자라면 횟수를 각각 횟수를 차감한다.
            HandLimit[Developer_Arr[i].A-1] -= 1
            HandLimit[Developer_Arr[i].B-1] -= 1
        # 둘 중 한명이 감염자가 아니고 악수 횟수가 남아 있다면 새로운 감염자를 추가한다.
        elif Developer_Arr[i].A not in Infect_P and HandLimit[Developer_Arr[i].B-1] > 0:
            Infect_P.append(Developer_Arr[i].A)
            result[Developer_Arr[i].A-1] = 1
            HandLimit[Developer_Arr[i].B-1] -= 1
        elif Developer_Arr[i].B not in Infect_P and HandLimit[Developer_Arr[i].A-1] > 0:
            Infect_P.append(Developer_Arr[i].B)
            result[Developer_Arr[i].B-1] = 1
            HandLimit[Developer_Arr[i].A-1] -= 1
    


for elem in result:
    print(elem, end = "")