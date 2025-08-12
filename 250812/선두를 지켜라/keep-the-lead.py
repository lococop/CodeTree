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






distance1 = 0
time1 = 0
for i in range(n):
    for j in range(time1+1, time1+t[i]+1):
        
        distance1 += v[i]
        arr1[j] = distance1
    time1 += t[i]

        

distance2 = 0
time2 = 0
for i in range(m):
    for j in range(time2+1, time2+t2[i]+1):
        
        distance2 += v2[i]
        arr2[j] = distance2
    time2 += t2[i]



cnt = 0
leader = 0
if arr1[1] > arr2[1]:
    leader = 1
elif arr2[1] > arr1[1]:
    leader = 2

new_leader = 0
for i in range(2, sum(t)+1):

    
    if (arr1[i] > arr2[i] and arr1[i-1] <= arr2[i-1]):
        new_leader = 1
        if leader != 0 and leader != new_leader:
            cnt += 1
        leader = 1

    if (arr1[i] < arr2[i] and arr1[i-1] >= arr2[i-1]):

        new_leader = 2
        if leader != 0 and leader != new_leader:
            cnt += 1
        leader = 2

print(cnt)
    