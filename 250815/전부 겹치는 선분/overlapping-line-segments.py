n = int(input())
segments = [tuple(map(int, input().split())) for _ in range(n)]
x1, x2 = zip(*segments)
x1, x2 = list(x1), list(x2)

# Please write your code here.
cnt = 0
for i in range(n):

    
    for j in range(i+1, n):

        if x2[i] < x1[j]:
            continue
        else:
            cnt += 1


if n*(n-1)//2 == cnt:
    print("Yes")
else:
    print("No")