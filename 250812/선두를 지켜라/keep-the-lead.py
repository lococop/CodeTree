n, m = map(int, input().split())

# Process A's movements
v = []
t = []
for _ in range(n):
    vi, ti = map(int, input().split())
    v.append(vi)
    t.append(ti)

# Process B's movements
v2 = []
t2 = []
for _ in range(m):
    vi, ti = map(int, input().split())
    v2.append(vi)
    t2.append(ti)

# Please write your code here.

Size = 1000000
arr1 = [0]*Size
arr2 = [0]*Size

sum1 = 0
sum2 = 0
for i in range(n):
    sum1 += v[i]*t[i]

for i in range(m):
    sum2 += v2[i]*t2[i]
         
min_t = min(sum1, sum2)




time1 = 0
distance1 = 0
for i in range(n):
    for _ in range(t[i]):
        time1 += 1
        distance1 += v[i]
        arr1[time1] = distance1

# B 이동 기록
time2 = 0
distance2 = 0
for i in range(m):
    for _ in range(t2[i]):
        time2 += 1
        distance2 += v2[i]
        arr2[time2] = distance2




cnt = 0
for i in range(2, min_t+1):
    if (arr1[i] > arr2[i] and arr1[i-1] <= arr2[i-1]) or (arr1[i] < arr2[i] and arr1[i-1] >= arr2[i-1]):
        cnt += 1

print(cnt)
    