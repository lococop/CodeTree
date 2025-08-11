n = int(input())

# Please write your code here.

def w(n):

    if n == 0:
        return

    w(n-1)
    print(n, end = " ")

def w1(n,m):
    if n == 0:
        return
    
    w1(n-1, m)
    print(m-n+1, end = " ")

w(n)
print()
w1(n, n)