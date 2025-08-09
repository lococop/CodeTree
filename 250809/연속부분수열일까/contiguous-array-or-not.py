N1, N2 = map(int, input().split())

arr1 = list(map(int, input().split()))
arr2 = list(map(int, input().split()))

cnt = 0
i = 0
j = 0
while True:

    if arr1[i] == arr2[j]:
        cnt += 1
        i += 1
        j += 1
    else:
        i += 1
        cnt = 0
    
    if cnt == N2:
        print("Yes")
        break
    if i == N1-1:
        print("No")
        break

