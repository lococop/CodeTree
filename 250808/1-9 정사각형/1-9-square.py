N = int(input())

cnt = 0

for i in range(N):
    for j in range(N):
        cnt += 1
        print(cnt, end = "")
        if cnt == 9:
            cnt = 0

    
    print()