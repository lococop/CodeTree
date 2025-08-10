while True:
    a = input()
    if a == 'END':
        break
    else:
        b = ''
        for i in range(len(a)-1, -1, -1):
            b += a[i]
        print(b)