N = int(input())

sum = 0
for i in range(N):
    a = int(input())
    if a % 2 != 0 and a % 3 == 0:
        sum += a

print(sum)