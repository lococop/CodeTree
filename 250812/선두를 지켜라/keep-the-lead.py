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




distance1 = 0
time1 = 0
for i in range(n):
    temp = v[i]/t[i]
    for j in range(time1+1, time1+t[i]+1):
        time1 += 1
        distance1 += temp
        arr1[j] = distance1

        


distance2 = 0
time2 = 0
for i in range(m):
    temp = v2[i]/t[i]
    for j in range(time2+1, time2+t2[i]+1):
        time2 += 1
        distance2 += temp
        arr2[j] = distance2



cnt = 0
for i in range(2, min_t+1):
    if (arr1[i] > arr2[i] and arr1[i-1] <= arr2[i-1]) or (arr1[i] < arr2[i] and arr1[i-1] >= arr2[i-1]):
        cnt += 1

print(cnt)
    