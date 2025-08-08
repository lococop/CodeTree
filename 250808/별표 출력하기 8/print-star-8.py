N = int(input())


for i in range(1, N+1):
    for j in range(i):
        if i % 2 != 0:
            print("*", end = "")
            break
        else:
            print("*",end = " ")
    print()
