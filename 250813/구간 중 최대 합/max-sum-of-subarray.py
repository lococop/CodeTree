n, k = map(int, input().split())
arr = list(map(int, input().split()))

# Please write your code here.

import sys

ans = -sys.maxsize

for i in range(n-k+1):
    
    total_sum = 0
    for j in range(i, i + k):
        total_sum += arr[j]
    
    ans = max(ans, total_sum)

print(ans)