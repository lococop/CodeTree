N = int(input())

cnt = 0

for i in range(N):
    for j in range(N):
        cnt += 2
        print(cnt, end = " ")
        if cnt == 8:
            cnt = 0 
    print()