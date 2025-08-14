n, m = map(int, input().split())
pairs = [tuple(map(int, input().split())) for _ in range(m)]

# Please write your code here.
# 1 ~ N 까지 반복하고 또 1 ~ N까지 반복하면서 각 쌍도 순회한다.
# 각 쌍에서 1 ~ N, 1 ~ N 조합이 가장 많이 나온 조합을 찾는다.


max_n = 0

for num1 in range(1, n+1):
    for num2 in range(1, n+1):

        cnt = 0
        for i in range(m):

            if (num1 == pairs[i][0] and num2 == pairs[i][1]) or (num1 == pairs[i][1] and num2 == pairs[i][0]):
                cnt += 1
        
        max_n = max(max_n, cnt)

print(max_n)

        