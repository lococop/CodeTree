n, m = map(int, input().split())

d = []
t = []
for _ in range(n):
    direction, time = input().split()
    d.append(direction)
    t.append(int(time))

d2 = []
t2 = []
for _ in range(m):
    direction, time = input().split()
    d2.append(direction)
    t2.append(int(time))

# Please write your code here.
cnt = 0
OFFSET = 10000
arr1 = [0]*20000
arr2 = [0]*20000

cnt = 0
time1 = 0
for i in range(n):
    if d[i] == 'R':
        for j in range(time1 + OFFSET+1, time1+OFFSET+t[i]+1):
            cnt += 1
            time1 += 1
            arr1[j] = cnt
            
    
    elif d[i] == 'L':
        for j in range(time1+OFFSET+1, time1+OFFSET+t[i]+1):
            cnt -= 1
            time1 += 1
            arr1[j] = cnt
        

cnt1 = 0
time2 = 0
for i in range(m):
    if d2[i] == 'R':
        for j in range(time2+OFFSET+1, time2+OFFSET+t2[i]+1):
            cnt1 += 1
            time2 += 1
            arr2[j] = cnt1
            
    
    elif d2[i] == 'L':
        for j in range(time2+OFFSET+1, time2+OFFSET+t2[i]+1):
            cnt1 -= 1
            time2 += 1
            arr2[j] = cnt1



max_time = min(sum(t), sum(t2))
for i in range(1, max_time + 1):
    if arr1[i + OFFSET] == arr2[i + OFFSET]:
        print(i)
        break
else:
    print(-1)
    
