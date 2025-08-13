n = int(input())
arr = list(map(int, input().split()))

# Please write your code here.

ans = 0
for i in range(n):
    for j in range(i, n):

        total = 0
        cnt = 0
        for k in range(i, j+1):
            total += arr[k]
            cnt += 1
        
        average = total/cnt

        

        for k in range(i, j+1):
            if average == arr[k]:
                ans += 1
                break

print(ans)
