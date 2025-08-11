n = int(input())
arr = list(map(int, input().split()))

# Please write your code here.

def w(n, arr):

    if n == 0:
        return arr[0]

    prev = w(n-1, arr)
    if arr[n-1] > prev:
        return arr[n-1]
    
    else:
        return prev


print(w(n, arr))