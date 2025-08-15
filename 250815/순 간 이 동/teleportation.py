a, b, x, y = map(int, input().split())

# Please write your code here.

print(min(abs(b-a), abs(x-a + b-y), abs(a-y + b-x)))

