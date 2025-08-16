n = int(input())
arr = list(map(int, input().split()))

# Please write your code here.

for i in range(n):

    min_n = i
    for j in range(i, n):
        if arr[j] < arr[min_n]:
            min_n = j
    
    arr[i], arr[min_n] = arr[min_n], arr[i]

for elem in arr:
    print(elem, end = " ")