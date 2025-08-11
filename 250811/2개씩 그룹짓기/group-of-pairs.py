n = int(input())
nums = list(map(int, input().split()))

# Please write your code here.
nums.sort()
import sys
max_n = -sys.maxsize
for i in range(n):
    if max_n < nums[i] + nums[n*2-i-1]:
        max_n = nums[i] + nums[n*2-i-1]

print(max_n)