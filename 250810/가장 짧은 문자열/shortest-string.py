import sys

max_n = -sys.maxsize
min_n = sys.maxsize

for _ in range(3):
    a = input()
    if max_n < len(a):
        max_n = len(a)

    if min_n > len(a):
        min_n = len(a)

print(max_n-min_n)