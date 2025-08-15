N = int(input())
pigeon = []
position = []
for _ in range(N):
    p, pos = map(int, input().split())
    pigeon.append(p)
    position.append(pos)

# Please write your code here.
# 비둘기 번호에 맞게 배열을 생성한다.
# 만약 비둘기 번호를 처음 조회했을 때 값을 바꿔주면서 카운팅은 해주지 않는다.
# 두 번 같은 번호를 조회했을 때 값이 바뀌면 카운트를 해준다.

arr = [0]*(11)

check = [0]*(11)

cnt = 0

for num in range(N):

    # 처음 조회이면 체크 및 위치 초기화
    if check[pigeon[num]] == 0:
        check[pigeon[num]] = 1
        arr[pigeon[num]] = position[num]
    
    else:
        if arr[pigeon[num]] != position[num]:
            arr[pigeon[num]] = position[num]
            cnt += 1


print(cnt)


