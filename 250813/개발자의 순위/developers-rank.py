k, n = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(k)]

# Please write your code here.
# 첫 경기 때 한 경기씩 완전탐색하면서 쌍을 지어준다.
# 두 번째 경기 부터 순위가 바뀐 것이 있으면 쌍을 지워준다.
# 최종적으로 남은 쌍의 개수를 카운트한다.

rank_list = []
for i in range(n):
   for j in range(i+1, n):
    rank_list.append((arr[0][i], arr[0][j]))


for i in range(1, k):
    temp = []
    for a, b in rank_list:

        if arr[i].index(a) < arr[i].index(b):
            temp.append((a,b))
    
    rank_list = temp

print(len(rank_list))

