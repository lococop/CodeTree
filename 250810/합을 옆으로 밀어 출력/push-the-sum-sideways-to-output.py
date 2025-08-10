N = int(input())

a = 0
for i in range(N):
    a += int(input())

a = str(a)[1:] + str(a)[0]

print(a)