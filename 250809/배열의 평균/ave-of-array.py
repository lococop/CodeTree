arr2d = []
sum2 = 0
cnt = 0
for i in range(2):
    arr = list(map(int, input().split()))
    arr2d.append(arr)
    print(f"{sum(arr)/len(arr):.1f}", end = " ")
    sum2 += sum(arr)
    cnt += len(arr)
print()

for j in range(4):
    sum1 = 0
    for i in range(2):
        sum1 += arr2d[i][j]
    print(f"{sum1/2:.1f}", end = " ")

print()

print(f"{sum2/cnt:.1f}")