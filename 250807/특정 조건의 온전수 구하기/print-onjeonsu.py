N = int(input())

cnt = 0
for i in range(1, N+1):
    if i % 2 == 0:
        continue
    elif str(i)[-1] == '5':
        continue
    elif i % 3 == 0 and i % 9 != 0:
        continue
    print(i, end = " ")