N = int(input())

cnt = 9

for i in range(N):
    for j in range(N):
        
        print(cnt, end = "")
        if cnt == 1:
            cnt = 10
        cnt -= 1

    print()