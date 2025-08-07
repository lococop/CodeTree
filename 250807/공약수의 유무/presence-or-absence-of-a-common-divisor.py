A, B = map(int, input().split())

IsG = False
for i in range(A, B+1):
    if 1920 % i == 0 and 2880 % i == 0:
        IsG = True

print(int(IsG))
