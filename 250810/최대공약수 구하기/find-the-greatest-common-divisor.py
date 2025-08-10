n, m = map(int, input().split())

# Please write your code here.
import sys

def a(n, m):
    max_n = -sys.maxsize
    for i in range(1, n+1):
        if n % i == 0 and m % i == 0 and max_n < i:
            max_n = i
    print(max_n)

a(n,m)