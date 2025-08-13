X, Y = map(int, input().split())

# Please write your code here.

import sys
max_n = -sys.maxsize

for num in range(X, Y+1):
    
    sum_n = 0
    for i in range(len(str(num))):
        sum_n += int(str(num)[i])
    
    max_n = max(max_n, sum_n)

print(max_n)