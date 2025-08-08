N = int(input())

cnt = 1
for i in range(N):

    if i % 2 == 0:
        for j in range(cnt, N+cnt):
            print(j, end = " ")
            cnt += 1
    else:
        for j in range(N+cnt-1, cnt-1, -1):
            print(j, end = " ")
            cnt += 1
    print()

