N = int(input())
a, b, c = map(int, input().split())

# Please write your code here.
# 한자리씩 반복문을 통해 차이가 2이내인지 알아본다.

cnt = 0
for i in range(1, N+1):
    for j in range(1, N+1):
        for k in range(1, N+1):

            if abs(a-i) <= 2 or abs(b-j) <= 2 or abs(c-k) <= 2:
                cnt += 1

print(cnt)