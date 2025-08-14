n = int(input())
arr = list(map(int, input().split()))

# Please write your code here.


import sys

min_sum = sys.maxsize

for i in range(n):

    arr[i] *= 2

    

    

    for j in range(n):

        remaining_list = []

        remaining_list = [elem for k, elem in enumerate(arr) if k != j]
        
        total_sum = 0
        for k in range(n-2):
            total_sum += abs(remaining_list[k] - remaining_list[k+1])
        
    
        min_sum = min(min_sum, total_sum)

    arr[i] //= 2

print(min_sum)
