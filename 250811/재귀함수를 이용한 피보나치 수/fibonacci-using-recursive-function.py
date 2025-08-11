N = int(input())

# Please write your code here.

def w(N):
    if N == 1:
        return 1
    if N == 2:
        return 1

    return w(N-1) + w(N-2)


print(w(N))