N = int(input())

# Please write your code here.

def w(N):
    if N == 1:
        return 2
    if N == 2:
        return 4

    return w(N-1)*w(N-2) % 100

print(w(N))