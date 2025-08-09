N = int(input())

arr = [1, N]

while True:
    arr.append(arr[-1]+arr[-2])
    
    if arr[-2]+arr[-3] > 100:
        break

for i in arr:
    print(i, end = " ")