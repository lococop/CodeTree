A, B = map(int, input().split())

sum = 0

if A > B:
    temp = A
    A = B
    B = temp

for i in range(A, B+1):
    if i % 5 == 0:
        sum += i

print(sum)