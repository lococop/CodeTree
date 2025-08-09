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

print(max_num1, max_num2)
        