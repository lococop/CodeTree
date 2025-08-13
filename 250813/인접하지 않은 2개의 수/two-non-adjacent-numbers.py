n = int(input())
numbers = list(map(int, input().split()))

# Please write your code here.
import sys

max_num = -sys.maxsize

for i in range(n):

    for j in range(i+2, n):
        max_num = max(max_num, numbers[i]+numbers[j])

print(max_num)
