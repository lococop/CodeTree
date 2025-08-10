a, b = map(int, input().split())

a = a+b

cnt = 0
for elem in str(a):
    if elem == '1':
        cnt += 1

print(cnt)