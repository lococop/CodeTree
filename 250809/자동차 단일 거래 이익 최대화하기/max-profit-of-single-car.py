n = int(input())
price = list(map(int, input().split()))

# Please write your code here.
import sys

max_n = -sys.maxsize

for i in range(n):
    for j in range(i+1, n):
        if price[i] < price[j]:
            if max_n < (price[j]-price[i]):
                max_n = price[j]-price[i]

if max_n == -sys.maxsize:
    max_n = 0
print(max_n)