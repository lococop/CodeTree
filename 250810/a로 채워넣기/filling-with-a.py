a = input()

a = list(a)

a[1] = 'a'
a[-2] = 'a'

print("".join(a))