N = int(input())

cnt = 65

for i in range(1, N+1):
    for i in range(1, i+1):
        print(chr(cnt), end = "")
        if chr(cnt) == "Z":
            cnt = 64
        cnt += 1
    print()