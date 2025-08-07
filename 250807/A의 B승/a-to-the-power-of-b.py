A, B = map(int, input().split())

sum = 1
for i in range(B):
    sum *= A

print(sum)