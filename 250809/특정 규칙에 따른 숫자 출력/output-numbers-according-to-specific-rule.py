N = int(input())

cnt = 1
for i in range(N, 0, -1):
    for j in range(N-i):
        print(end = "  ")
    for j in range(i):
        print(cnt, end = " ")
        if cnt == 9:
            cnt = 0
        cnt += 1
    print()