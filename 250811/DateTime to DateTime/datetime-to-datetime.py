a, b, c = map(int, input().split())

# Please write your code here.
n = 11*24*60 + 11*60 + 11
m = a*24*60 + b*60 + c
print(m-n)