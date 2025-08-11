n = int(input())
arr = list(map(int, input().split()))

# Please write your code here.
a = []
for i in range(n):
    a.append(arr[i])
    a.sort()
    if (i+1) % 2 != 0:
        print(a[len(a)//2], end = " ")
