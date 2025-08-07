A, B = map(int, input().split())

sum = A
for i in range(B-1):
    sum *= A

print(sum)