N, M = map(int, input().split())

arr1 = []
arr2 = []
for i in range(N):
    arr = list(map(int, input().split()))
    arr1.append(arr)
for i in range(N):
    arr = list(map(int, input().split()))
    arr2.append(arr)


for i in range(N):
    for j in range(M):
        if arr1[i][j] == arr2[i][j]:
            print(0, end = " ")
        else:
            print(1, end = " ")
    print()

