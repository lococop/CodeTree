n = int(input())
segments = [tuple(map(int, input().split())) for _ in range(n)]

# Please write your code here.
Max_n = 100

arr = [0]*(Max_n+1)

for e in segments:
    for j in range(e[0], e[1]+1):
        arr[j] += 1

print(max(arr))