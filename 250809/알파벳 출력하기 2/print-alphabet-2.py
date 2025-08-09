N = int(input())

cnt = 65
for i in range(N, 0, -1):
    for j in range(N-i):
        print(end = "  ")
    for j in range(i):
        print(chr(cnt), end = " ")
        if chr(cnt) == "Z":
            cnt = 64
        cnt += 1
    print()