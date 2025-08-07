sum = 0
cnt = 0
for i in range(10):
    a = int(input())

    if a >= 0 and a <= 200:
        sum += a
        cnt += 1

print(sum, f"{sum/cnt:.1f}")