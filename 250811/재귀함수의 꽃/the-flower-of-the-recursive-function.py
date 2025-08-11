N = int(input())

# Please write your code here.

def w(n):
    if n == 0:
        return

    print(n, end = " ")
    w(n-1)
    print(n, end = " ")

w(N)