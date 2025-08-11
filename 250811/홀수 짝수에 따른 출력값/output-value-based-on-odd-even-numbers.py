N = int(input())

# Please write your code here.


def w(N):
    if N % 2 != 0:
        if N == 1:
            return 1

        return w(N-2) + N
    
    else:
        if N == 2:
            return 2
        
        return w(N-2) + N
    
print(w(N))