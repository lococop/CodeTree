n = int(input())
a = list(map(int, input().split()))

# Please write your code here.
max_num1 = a[0]
max_num2 = a[0]

for elem in a:
    if max_num1 < elem:
        max_num1 = elem
for elem in a:
    if max_num2 < elem and elem != max_num1:
        max_num2 = elem

cnt = 0
for elem in a:
    if elem == max_num1:
        cnt += 1
if cnt >= 2:
    max_num2 = max_num1

print(max_num1, max_num2)
        