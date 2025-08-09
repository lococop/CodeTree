arr = list(map(int, input().split()))

sum = 0
cnt = 0
for i in range(10):
    if arr[i] >= 250:
        break
        
    if arr[i] < 250:
        sum += arr[i]
        cnt += 1
    

print(sum, sum/cnt)