n = int(input())
nums = list(map(int, input().split()))

# Please write your code here.
import sys
max_n = -sys.maxsize

for i in range(n):
    if nums[i] > max_n and nums.count(nums[i]) == 1:
        max_n = nums[i]

if max_n != -sys.maxsize:
    print(max_n)
else:
    print(-1)
    