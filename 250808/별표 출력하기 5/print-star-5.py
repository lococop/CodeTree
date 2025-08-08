N = int(input())

for i in range(N, 0, -1):
    for j in range(i):
        for m in range(i):
            print("*", end = "")
        print(end = " ")
    print()