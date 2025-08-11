N = input()

# Please write your code here.

n = 0
for i in range(len(N)):
    n = n*2 + int(N[i])

n *= 17

arr = []
while True:
    if n < 2:
        arr.append(n)
        break
    arr.append(n%2)
    n //= 2

for elem in arr[::-1]:
    print(elem, end = "")