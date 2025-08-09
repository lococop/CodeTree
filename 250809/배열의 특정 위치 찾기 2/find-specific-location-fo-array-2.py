arr = list(map(int, input().split()))

sum_odd = 0
sum_even = 0

for i in range(len(arr)):
    if (i+1) % 2 != 0:
        sum_odd += arr[i]
    else:
        sum_even += arr[i]

print(abs(sum_even-sum_odd))
