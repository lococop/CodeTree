N = int(input())

sum1 = 0
cnt = 0

for _ in range(N):
    a = input()
    sum1 += len(a)
    if a[0] == 'a':
        cnt += 1

print(sum1, cnt)