A, B = map(int, input().split())

sum = 1
for i in range(1, B+1):
    if i % A == 0:
        sum *= i

print(sum)