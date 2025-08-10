cnt = 0
arr = []
i = 1
while True:

    a = input()
    
    if a == '0':
        break
    else:
        cnt += 1

        if i % 2 != 0:
            arr.append(a)
        i += 1

print(cnt)
for elem in arr:
    print(elem)