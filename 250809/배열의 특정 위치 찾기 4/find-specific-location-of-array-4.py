arr = list(map(int, input().split()))

arr1 = []

for i in arr:
    if i != 0 and i % 2 == 0:
        arr1.append(i)
    elif i == 0:
        break

print(len(arr1), sum(arr1))