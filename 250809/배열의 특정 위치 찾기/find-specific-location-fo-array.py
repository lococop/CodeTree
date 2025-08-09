arr = list(map(int, input().split()))

cnt2 = 0
cnt3 = 0
cnt = 0
for i in range(len(arr)):
    if (i+1) % 2 == 0:
        cnt2 += arr[i]
    if (i+1) % 3 == 0:
        cnt3 += arr[i]
        cnt += 1
    
print(cnt2, f"{cnt3/cnt:.1f}")