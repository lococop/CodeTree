A, B = map(int, input().split())

sum  = 1

for i in range(A, B+1):
    sum *= i

print(sum)