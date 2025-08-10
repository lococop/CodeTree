a = input()
b = input()

cnt = 0
while True:

    if a == b:
        print(cnt)
        break

    else:
        a = a[1:] + a[0]
        cnt += 1
    
    if cnt == len(a):
        print(-1)
        break

