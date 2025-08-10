a = input()
a = list(a)

b = a[1]
c = a[0]

for i in range(len(a)):
    if b == a[i]:
        a[i] = c

print("".join(a))