n, k = map(int, input().split())
commands = [tuple(map(int, input().split())) for _ in range(k)]

# Please write your code here.
arr = [0]*n

for i in commands:
    for j in range(i[0], i[1]+1):
        arr[j-1] += 1

print(max(arr))
