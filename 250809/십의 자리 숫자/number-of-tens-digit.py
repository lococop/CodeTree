arr = list(map(int, input().split()))

arr1 = []

for i in arr:
    if i == 0:
        break
    else:
        arr1.append(i)

for i in range(1,10):
    cnt = 0
    for elem in arr1:
        if elem//10 == i:
            cnt += 1
    print(f"{i} - {cnt}")