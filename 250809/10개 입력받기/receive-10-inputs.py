arr = list(map(int, input().split()))

arr1 = []

for i in arr:
    if i != 0:
        arr1.append(i)
    else:
        break

print(sum(arr1), f"{sum(arr1)/len(arr1):.1f}")