a, b, x, y = map(int, input().split())

# Please write your code here.

print(min(abs(b-a), abs(x-a) + abs(b-y), abs(a-y) + abs(b-x)))

