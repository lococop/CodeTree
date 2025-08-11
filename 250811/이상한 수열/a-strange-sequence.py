N = int(input())

# Please write your code here.

def w(N):

    if N == 1:
        return 1
    if N == 2:
        return 2

    return w(N//3) + w(N-1)


print(w(N))