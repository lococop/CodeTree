N = int(input())

for i in range(N):
    for j in range(i+1):
        print("*", end = "")
    print()
    print()

for i in range(N, 0, -1):
    for j in range(i-1):
        print("*", end = "")
    print()
    print()