n = int(input())
a = list(map(int, input().split()))

# Please write your code here.
min_num = a[0]
cnt = 0

for i in range(1, n):
    if min_num > a[i]:
        min_num = a[i]

for elem in a:
    if min_num == elem:
        cnt += 1

print(min_num, cnt)