n = int(input())
arr = list(map(int, input().split()))

# Please write your code here.

for i in range(n):
    for j in range(n-1-i):
        if arr[j] > arr[j+1]:
            arr[j], arr[j+1] = arr[j+1], arr[j]
    

for elem in arr:
    print(elem, end = " ")