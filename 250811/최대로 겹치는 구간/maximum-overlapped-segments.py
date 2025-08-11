n = int(input())
segments = [tuple(map(int, input().split())) for _ in range(n)]

# Please write your code here.
OFFSET = 100
MAX_R = 200

arr = [0]*(MAX_R+1)

for elem in segments:
    for j in range(elem[0]+OFFSET,elem[1]+OFFSET):
        arr[j] += 1
print(max(arr))