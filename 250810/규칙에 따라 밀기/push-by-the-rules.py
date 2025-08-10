a = input()
b = input()

for elem in b:
    if elem == 'L':
        a = a[1:] + a[0]
    elif elem == 'R':
        a = a[-1] + a[:-1]

print(a)