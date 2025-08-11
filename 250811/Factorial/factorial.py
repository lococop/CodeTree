N = int(input())

# Please write your code here.

def w(N):

    if N == 1:
        return 1
    
    return N * w(N-1)

print(w(N))