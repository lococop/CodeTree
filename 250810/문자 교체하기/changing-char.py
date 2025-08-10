a = input().split()

a[0] = list(a[0])

a[1] = list(a[1])

a[1][0] = a[0][0]
a[1][1] = a[0][1]

print("".join(a[1]))