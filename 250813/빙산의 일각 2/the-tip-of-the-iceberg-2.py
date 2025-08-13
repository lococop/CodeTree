n = int(input())
h = [int(input()) for _ in range(n)]

# Please write your code here.

ans = 0

for height in range(1, 1001):

    cnt = 0

    if h[n-1] > height:
        cnt += 1


    for i in range(n-1):
        if h[i] > height and h[i+1] <= height:
            cnt += 1
    
    ans = max(ans, cnt)

print(ans)
