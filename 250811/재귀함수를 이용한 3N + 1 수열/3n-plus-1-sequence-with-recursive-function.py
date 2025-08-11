n = int(input())

# Please write your code here.

def w(n):
    if n == 1:
        return 0
    
    if n % 2 == 0:
        return w(n//2) + 1
    
    else:
        return w(n*3+1) + 1

print(w(n))