N, K = map(int, input().split())
num = [int(input()) for _ in range(N)]

# Please write your code here.

size = 1000000

import sys

max_n = -sys.maxsize

number = 0

for n in range(size+1):
    
    for i in range(N-(K+1)+1):

        cnt = 0
        for j in range(i, i+K+1):
            if n == num[j]:
                cnt += 1
        
        if max_n < cnt:
            number = n
            max_n = cnt
        elif max_n == cnt and number < n:
            number = n
            

print(number)