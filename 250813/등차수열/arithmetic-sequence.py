n = int(input())
a = list(map(int, input().split()))

# Please write your code here.

a.sort()

cnt = 0
for i in range(n):
    for j in range(i+1, n): 
        for k in range(1, 101):
            if a[j]-k == k-a[i]:
                cnt += 1

print(cnt)