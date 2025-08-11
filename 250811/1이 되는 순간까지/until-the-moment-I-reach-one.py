N = int(input())

# Please write your code here.


def w(N):
 
    if N == 1:
        return 0

    if N % 2 == 0:
        return w(N//2) + 1
    else:
        return w(N//3) + 1

print(w(N))