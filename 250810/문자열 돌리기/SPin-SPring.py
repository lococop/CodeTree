a = input()


for i in range(len(a)+1):
    print(a)
    a = a[-1] + a[:-1]
    