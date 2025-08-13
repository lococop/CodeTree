N, M = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

# Please write your code here.

total_cnt = 0
for i in range(N-M+1):
    cnt = 0

    temp = B.copy()

    for j in range(i, i+M):
        if A[j] in temp:
            cnt += 1
            temp.remove(A[j])
        
        if cnt == M:
            total_cnt += 1

print(total_cnt)
    