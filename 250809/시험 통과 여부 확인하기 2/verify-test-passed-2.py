N = int(input())

cnt = 0
for i in range(N):
    arr = list(map(int, input().split()))

    if sum(arr)/len(arr) >= 60:
        print("pass")
        cnt += 1
    else:
        print("fail")

print(cnt)