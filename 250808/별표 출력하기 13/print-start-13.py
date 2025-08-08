N = int(input())

for i in range(N, 0, -1):
    for j in range(i):
        print("*", end = " ")
    print()
    for j in range(N-i+1):
        print("*", end = " ")
    print()