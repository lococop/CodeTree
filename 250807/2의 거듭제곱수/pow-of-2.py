N = int(input())

cnt = 1
a = 2
while True:
    a *= 2
    cnt += 1
    if N == a:
        break

print(cnt)