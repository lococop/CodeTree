a = input()

sum1 = 0
for elem in a:
    if elem >= '0' and elem <= '9':
        sum1 += int(elem)

print(sum1)