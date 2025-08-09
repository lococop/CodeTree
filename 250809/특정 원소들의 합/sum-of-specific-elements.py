arr2d = []

for i in range(4):
    arr = list(map(int, input().split()))
    arr2d.append(arr)

sum1 = 0

for i in range(4):
    for j in range(i+1):
        sum1 += arr2d[i][j]

print(sum1)
