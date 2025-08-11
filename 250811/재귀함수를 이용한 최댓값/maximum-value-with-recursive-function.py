n = int(input())
arr = list(map(int, input().split()))

# Please write your code here.

def w(n, arr):

    if n == 0:
        return arr[0]

    if arr[n-1] > w(n-1, arr):
        return arr[n-1]
    
    else:
        return w(n-1, arr)


print(w(n, arr))