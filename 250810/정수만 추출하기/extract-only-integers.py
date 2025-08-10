a, b = input().split()

sum1 = ''
for elem in a:
    if elem >= '0' and elem <= '9':
        sum1 += elem
    else:
        break
sum2 = ''
for elem in b:
    if elem >= '0' and elem <= '9':
        sum2 += elem
    else:
        break
print(int(sum1)+int(sum2))
    