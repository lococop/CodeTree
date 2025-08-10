n, m = map(int, input().split())
A = list(map(int, input().split()))

# Please write your code here.

def w(n, m, A):
    m = m
    sum1 = 0
    while m != 0:
        sum1 += A[m-1]
        if m % 2 != 0:
            m -= 1
        else:
            m //= 2
    return sum1

print(w(n, m, A))
        
