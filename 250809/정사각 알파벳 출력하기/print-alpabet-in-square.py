N = int(input())

cnt = 65
for i in range(N):
    for j in range(N):
        print(chr(cnt),end="")
        cnt += 1
    print()