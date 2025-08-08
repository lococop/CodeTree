N = int(input())

for i in range(N):
    for j in range(N):
        if i == 0 or (j % 2 != 0 and j >= i):
            print("*", end = " ")
        else:
            print(end="  ")
    print()