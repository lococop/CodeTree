a = input()

b = a.index('e')
a = list(a)
a.pop(b)

print("".join(a))