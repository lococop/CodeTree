N = int(input())
a = [input() for _ in range(N)]

b = input()

cnt = 0
sum1 = 0

for elem in a:
    if elem[0] == b:
        cnt += 1
        sum1 += len(elem)

print(cnt, f"{sum1/cnt:.2f}")