n = int(input())
x = []
dir = []
for _ in range(n):
    xi, di = input().split()
    x.append(int(xi))
    dir.append(di)

# Please write your code here.
OFFSET = 100
Max_n = 200
arr = [0]*(Max_n+1)
cnt = 0

for i in range(n):
    if dir[i] == 'R':
        for j in range(cnt+OFFSET, x[i]+cnt+OFFSET):
            arr[j] += 1
            cnt += 1
    elif dir[i] == 'L':
        for j in range(cnt+OFFSET-1, cnt+OFFSET-x[i]-1, -1):
            arr[j] += 1
            cnt -= 1

sum1 = 0
for elem in arr:
    if elem >= 2:
        sum1 += 1

print(sum1)