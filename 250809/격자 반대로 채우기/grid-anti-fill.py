N = int(input())

arr = [[0]*N for _ in range(N)]
cnt = 1
Is = True
for i in range(N-1, -1, -1):
    if Is == True:

        for j in range(N-1, -1, -1):
            arr[j][i] = cnt 
            cnt += 1
        Is = False
    else:
        for j in range(N):
            arr[j][i] = cnt
            cnt += 1
        Is = True

for row in arr:
    print(*row)
    