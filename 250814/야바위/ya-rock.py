n = int(input())
moves = [tuple(map(int, input().split())) for _ in range(n)]
a, b, c = zip(*moves)
a, b, c = list(a), list(b), list(c)

# Please write your code here.
# 3개의 배열을 만들고 a b c에 따라 값에 변화를 주고 체크한다.
# 근데 값을 체크할 때 수가 확인되는 횟수가 최대가 되는 시작점을 찾는다.




import sys

max_n = -sys.maxsize

for start in range(3):

    arr = [0]*3

    # 시작하는 지점 초기화
    arr[start] = 1

    cnt = 0

    for i in range(n):
        # a, b 값 교환
        arr[a[i]-1], arr[b[i]-1] = arr[b[i]-1], arr[a[i]-1]

        if arr[c[i]-1] == 1:
            cnt += 1
        
    max_n = max(max_n, cnt)

print(max_n)