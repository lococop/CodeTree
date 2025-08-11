n = int(input())

# Please write your code here.

def w(n):
    if n == 0:
        return

    print("* "*n)
    
    w(n-1)
    print("* "*n)
    


w(n)