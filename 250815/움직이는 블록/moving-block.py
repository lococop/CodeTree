n = int(input())
blocks = [int(input()) for _ in range(n)]

# Please write your code here.

average = sum(blocks) // n

total = 0

for elem in blocks:
    if elem > average:
        total += elem-average

print(total)