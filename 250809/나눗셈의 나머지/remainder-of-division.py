A, B = map(int, input().split())

arr = [0]*10
while A > 1:
    arr[A % B] += 1
    A = A // B

sum = 0

for elem in arr:
    sum += elem*elem

print(sum)