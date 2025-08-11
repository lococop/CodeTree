N = int(input())

# Please write your code here.


def w(N):
    if N < 10:
        return N**2
    
    return w(N // 10) + (N%10)**2


print(w(N))