a, b = map(int, input().split())

# Please write your code here.
def w(a,b):
    a = a
    b = b
    if a > b:
        a += 25
        b *= 2
    else:
        a *= 2
        b += 25

    return (a,b)

a, b = w(a,b)

print(a, b)