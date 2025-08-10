n = int(input())
arr = list(map(int, input().split()))

# Please write your code here.

def w(arr):
    for i in range(n):
        arr[i] = abs(arr[i])

w(arr)

for elem in arr:
    print(elem, end = " ")