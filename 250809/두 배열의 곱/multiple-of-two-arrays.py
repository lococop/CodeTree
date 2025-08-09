arr1 = []
arr2 = []
# arr3 = [[0 for _ in range(3)] for _ in range(3)]

for i in range(3):
    arr = list(map(int, input().split()))
    arr1.append(arr)

a = input()

for i in range(3):
    arr = list(map(int, input().split()))
    arr2.append(arr)

for i in range(3):
    for j in range(3):
        print(arr1[i][j]*arr2[i][j], end = " ")
    print()
