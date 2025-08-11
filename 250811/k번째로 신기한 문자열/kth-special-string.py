n, k, t = input().split()
n, k = int(n), int(k)
str = [input() for _ in range(n)]

# Please write your code here.

arr = []

for elem in str:

    if t == elem[:len(t)]:
        arr.append(elem)
    
arr.sort()

print(arr[k-1])