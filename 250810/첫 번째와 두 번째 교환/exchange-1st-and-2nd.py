a = input()
a = list(a)

b = a[0]
c = a[1]

for i in range(len(a)):
    if c == a[i]:
        a[i] = b
    elif b == a[i]:
        a[i] = c

print("".join(a))