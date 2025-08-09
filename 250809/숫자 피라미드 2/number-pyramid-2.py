N = int(input())
cnt = 1
for i in range(1, N+1):
    for j in range(0, i):
        print(cnt, end = " ")
        cnt += 1
    print()