arr = list(map(int, input().split()))

arr1 = []

for i in arr:
    if i != 0:
        arr1.append(i)
    else:
        break
for i in range(len(arr1)-1, -1, -1):
    print(arr1[i], end = " ")