a, b, c = map(int, input().split())

# Please write your code here.

def w(a):

    if a < 10:
        return a

    return a % 10 + w(a//10)

print(w(a*b*c)) 