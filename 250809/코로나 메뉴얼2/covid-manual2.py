A = 0
B = 0
C = 0
D = 0

for i in range(3):
    a, b = input().split()

    if a == 'Y' and int(b) >= 37:
        A += 1
    elif a == 'N' and int(b) >= 37:
        B += 1
    elif a == 'Y' and int(b) < 37:
        C += 1
    else:
        D += 1

print(A, B, C, D, end = " ")
if A >= 2:
    print('E')
