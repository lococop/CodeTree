N, Q = map(int, input().split())

arr = list(map(int, input().split()))

for i in range(Q):
    a = list(map(int, input().split()))

    if a[0] == 1:
        print(arr[a[1]-1])

    elif a[0] == 2:
        if a[1] in arr:
            print(arr.index(a[1])+1)

        else:
            print(0)

    elif a[0] == 3:
        for i in range(a[1], a[2]+1):
            print(arr[i-1], end = " ")
        print()
        