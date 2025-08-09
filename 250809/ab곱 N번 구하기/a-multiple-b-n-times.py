N = int(input())

for i in range(N):
    a, b = map(int, input().split())
    sum = 1
    for j in range(a, b+1):
        sum *= j
    print(sum)