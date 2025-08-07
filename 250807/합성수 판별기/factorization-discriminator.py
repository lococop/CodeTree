N = int(input())

IsH = False
for i in range(2, N):
    if N % i == 0:
        IsH = True

if IsH == True:
    print("C")
else:
    print("N")