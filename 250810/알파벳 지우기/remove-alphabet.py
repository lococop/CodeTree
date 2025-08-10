a = input()
b = input()

sum1 = ''
for elem in a:
    if elem >= '0' and elem <= '9':
        sum1 += elem

sum2 = ''
for elem in b:
    if elem >= '0' and elem <= '9':
        sum2 += elem

print(int(sum1)+int(sum2))
