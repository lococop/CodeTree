a, b = map(int, input().split())

# Please write your code here.

def w(a,b):
    sum1 = 1
    for _ in range(b):
        sum1 *= a
    return sum1

print(w(a,b))